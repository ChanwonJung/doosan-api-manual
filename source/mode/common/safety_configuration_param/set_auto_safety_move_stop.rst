.. _set_auto_safety_move_stop:

set_auto_safety_move_stop
------------------------------------------
This function enables or disables the **automatic motion stop** behavior when a safety event occurs.  
If this option is enabled, the robot will automatically stop motion in case of collision,
safety zone violation, or other safety-related triggers without requiring a manual stop command.

This feature is useful for applications such as collaborative or palletizing robots,
where unexpected contact or area entry should immediately interrupt robot motion.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 929)

.. code-block:: cpp

    bool set_auto_safety_move_stop(bool bFuncEnable)
    {
        return _set_auto_safety_move_stop(_rbtCtrl, bFuncEnable);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bFuncEnable
     - bool
     - -
     - Option for enabling automatic motion stop:  |br|
       - true (1): Enable automatic stop on safety events  |br|
       - false (0): Disable (manual stop control only)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to apply the configuration
   * - 1
     - Success — automatic stop mode successfully applied

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <chrono>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx Drfl;

       // Enable automatic motion stop for safety events
       Drfl.set_auto_safety_move_stop(true);

       // Adjust collision sensitivity (optional)
       // A lower value increases responsiveness to minor impacts
       Drfl.change_collision_sensitivity(20.0f);

       // Execute motion command (example: MoveJ)
       // The robot will automatically stop if a safety event is triggered
       float targetPos[6] = {700, 0, 300, 180, 0, 180};
       float v[2] = {60, 60};
       float a[2] = {60, 60};
       // Drfl.movej(targetPos, v, a); // Example motion (pseudo-code)

       // Simulate motion process for 5 seconds
       std::this_thread::sleep_for(std::chrono::seconds(5));

       // Disable automatic motion stop after task is done
       Drfl.set_auto_safety_move_stop(false);

       return 0;
   }

This example enables the automatic motion stop function,  
executes a motion with adjusted collision sensitivity, and  
then disables the function after the motion is completed.  
If a safety event such as a collision or safety zone trigger occurs,  
the robot will automatically stop without any additional commands.
