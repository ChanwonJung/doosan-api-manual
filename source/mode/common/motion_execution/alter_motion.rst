.. _alter_motion:

alter_motion
------------------------------------------
This function applies an **incremental adjustment** to the active motion trajectory  
after :ref:`enable_alter_motion <enable_alter_motion>` has been successfully activated.  
It allows fine control of the robot’s end-effector position and orientation in real time  
by sending small delta pose values at each control cycle.

Each call to `alter_motion()` modifies the current trajectory based on the provided `fTargetPos` offsets.  
The input values correspond to **X, Y, Z, Rx, Ry, Rz** displacements and rotations,  
which are interpreted according to the reference frame configured in `enable_alter_motion()`.

This function is available in **M2.4 version or higher**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 982)

.. code-block:: cpp

    bool alter_motion(float fTargetPos[NUM_TASK]) {
        return _alter_motion(_rbtCtrl, fTargetPos);
    };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Array representing incremental motion values for the current cycle. |br|
       Order: **[X, Y, Z, Rx, Ry, Rz]** |br|
       Units: **mm** for translation, **deg** for rotation.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed to apply alter motion.
   * - 1
     - Successfully applied the incremental motion.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   // Thread continuously sending small incremental poses
   void ThreadFunc() {
       CDRFLEx drfl;
       float delta[6] = {10.0f, 0.0f, 0.0f, 10.0f, 0.0f, 0.0f};  // ΔX=10mm, ΔRx=10°
       while (true) {
           drfl.alter_motion(delta);
           std::this_thread::sleep_for(std::chrono::milliseconds(20));  // must match enable_alter_motion cycle
       }
   }

   int main() {
       CDRFLEx drfl;

       // 1) Start background thread for continuous alter motion
       std::thread th(ThreadFunc);

       // 2) Enable alter motion mode (20 ms cycle)
       float limitDpos[2] = {50.0f, 90.0f};
       float limitDposPer[2] = {5.0f, 50.0f};
       drfl.enable_alter_motion(20, PATH_MODE_DPOS, COORDINATE_SYSTEM_BASE,
                                limitDpos, limitDposPer);

       // 3) Let it run for a while to apply incremental corrections
       std::this_thread::sleep_for(std::chrono::seconds(3));

       // 4) Stop alter motion mode safely
       drfl.disable_alter_motion();
       th.detach();

       return 0;
   }

**Caution**

- ``alter_motion()`` can be executed **only inside a user thread**.  
- The update rate must match the cycle time set in :ref:`enable_alter_motion <enable_alter_motion>`.  
- Input values follow **fixed XYZ notation**, and must not exceed configured limits (`fLimitDpos`, `fLimitDposPer`).
