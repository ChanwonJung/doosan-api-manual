.. _change_collision_sensitivity:

change_collision_sensitivity
------------------------------------------
This function configures the **collision sensitivity** of the robot controller. |br|
A higher sensitivity value makes the robot more responsive to small contact forces,  
while a lower value allows for greater tolerance before triggering a collision stop.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 915)

.. code-block:: cpp

    bool change_collision_sensitivity(float fSensitivity)
    {
        return _change_collision_sensitivity(_rbtCtrl, fSensitivity);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fSensitivity
     - float
     - -
     - Collision sensitivity level (range: **0–100**) |br|
       0: Minimum sensitivity (less reactive)  |br|
       100: Maximum sensitivity (most reactive)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to set collision sensitivity.
   * - 1
     - Success — sensitivity successfully applied.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Enable automatic motion stop for safety
        Drfl.set_auto_safety_move_stop(true);

        // Set collision sensitivity to 20 (range: 0~100)
        // A lower value increases sensitivity (e.g., for human-collaborative tasks)
        Drfl.change_collision_sensitivity(20.0f);

        // Example motion (pseudo-code)
        // The robot will stop automatically upon detecting an external force
        float target[6] = {500, 100, 300, 180, 0, 180};
        float v[2] = {60, 60};
        float a[2] = {60, 60};
        // Drfl.movej(target, v, a);

        // Wait to simulate motion duration
        std::this_thread::sleep_for(std::chrono::seconds(5));

        // Restore default sensitivity after task
        Drfl.change_collision_sensitivity(50.0f);

        return 0;
    }

This example enables automatic safety motion stop and  
adjusts the collision sensitivity to **20**, which makes the robot  
more responsive to external contact. After the motion is finished,  
the sensitivity is reset to a normal level (**50**) for standard operation.
