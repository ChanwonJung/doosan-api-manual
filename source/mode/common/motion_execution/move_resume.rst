.. _move_resume:

move_resume
------------------------------------------
This is a function for resuming the robot motion that was temporarily suspended by the move_pause function in the robot controller. It is ignored if there is no active robot path motion.

**Definition** |br|  
``DRFLEx.h`` within class `CDRFLEx`, public section (line 766)

.. code-block:: cpp

    bool move_resume() { return _move_resume(_rbtCtrl); };

**Parameter** |br|  
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error occurred while attempting to resume motion.
   * - 1
     - Successfully resumed the previously paused motion.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Define target joint position
        float j1[NUM_JOINT] = {0, 0, 90, 0, 0, 90};

        // Start asynchronous joint motion
        Drfl.movej(j1, 20, 40);

        while (true) {
            // Get current joint position
            LPPOSE pPose = Drfl.get_current_posx();

            // Pause motion if the 3rd joint exceeds 45 degrees
            if (pPose->_fTargetPos[2] >= 45) {
                Drfl.move_pause();  // Temporarily suspend motion
                std::this_thread::sleep_for(std::chrono::seconds(5)); // Wait for 5 seconds
                break;
            }
        }

        // Resume motion
        Drfl.move_resume();

        return 0;
    }

This example demonstrates how to **resume** a robot’s motion that was previously suspended using ``move_pause()``.  
After pausing for 5 seconds, the robot continues its motion seamlessly using ``move_resume()``.
