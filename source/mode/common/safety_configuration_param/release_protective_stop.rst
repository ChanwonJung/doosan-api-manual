.. _release_protective_stop:

release_protective_stop
------------------------------------------
This function releases the **protective stop** state in the robot controller.  
When a protective stop is triggered due to a collision, external safety device,  
or system fault, this function clears the stop condition and allows the robot  
to resume operation.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 910)

.. code-block:: cpp

    bool release_protective_stop(RELEASE_MODE eReleaseMode)
    {
        return _release_protective_stop(_rbtCtrl, eReleaseMode);
    };

**Parameter**

.. list-table::
   :widths: 20 25 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eReleaseMode
     - :ref:`RELEASE_MODE <enum_release_mode>`
     - -
     - Mode for releasing protective stop

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to release protective stop
   * - 1
     - Success — protective stop released successfully

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Enable auto safety move stop for protection
        Drfl.set_auto_safety_move_stop(true);

        // Simulate a motion task that might trigger a protective stop
        float target[6] = {500, 200, 400, 180, 0, 180};
        float vel[2] = {60, 60};
        float acc[2] = {60, 60};
        // Drfl.movej(target, vel, acc);

        // Assume a collision or external force triggered a protective stop
        std::this_thread::sleep_for(std::chrono::seconds(3));
        std::cout << "Protective stop triggered due to collision!" << std::endl;

        // Release the protective stop condition
        Drfl.release_protective_stop(RELEASE_MODE_RELEASE);
        std::cout << "Protective stop released. Resuming operation..." << std::endl;

        // Re-enable servo to resume normal operation
        // Drfl.servo_on(true);

        return 0;
    }

This example demonstrates how to recover from a **protective stop** event  
triggered by an external collision or safety system.  
After calling `release_protective_stop(RELEASE_MODE_RELEASE)`,  
the robot can safely resume motion by re-enabling the servo.
