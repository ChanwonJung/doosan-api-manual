.. _disable_alter_motion:

disable_alter_motion
------------------------------------------
This function **deactivates the alter motion mode** that was previously enabled by  
:ref:`enable_alter_motion <enable_alter_motion>`.  
It stops the incremental path adjustment process and returns the robot to standard trajectory control.  
After this function is executed, additional calls to :ref:`alter_motion <alter_motion>` will be ignored  
until alter motion mode is re-enabled.

This function is available in **M2.4 version or higher**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 981)

.. code-block:: cpp

    bool disable_alter_motion() {
        return _disable_alter_motion(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed to deactivate alter motion mode.
   * - 1
     - Successfully disabled alter motion mode.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   // Thread routine continuously sending small delta corrections
   void ThreadFunc() {
       CDRFLEx drfl;
       float delta[6] = {10.0f, 0, 0, 10.0f, 0, 0};
       while (true) {
           drfl.alter_motion(delta);
           std::this_thread::sleep_for(std::chrono::milliseconds(20));
       }
   }

   int main() {
       CDRFLEx drfl;

       // 1) Start a separate thread to run alter motion continuously
       std::thread th(ThreadFunc);

       // 2) Enable alter motion mode (prepare fine-tuning control)
       float limitDpos[2] = {50.0f, 90.0f};
       float limitDposPer[2] = {5.0f, 50.0f};
       drfl.enable_alter_motion(5, PATH_MODE_DPOS, COORDINATE_SYSTEM_BASE,
                                limitDpos, limitDposPer);

       // ... Fine-tuning in progress ...

       // 3) Disable alter motion mode to restore normal control
       drfl.disable_alter_motion();

       th.detach(); // clean up background thread
       return 0;
   }

This example shows how to **terminate an active alter motion session**.  
After calling `disable_alter_motion()`, all incremental control inputs are ignored,  
and the robot resumes standard motion execution. |br|
It is recommended to ensure all alter motion threads are safely terminated  
before disabling the mode to prevent redundant API calls.
