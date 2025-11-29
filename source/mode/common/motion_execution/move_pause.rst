.. _move_pause:

move_pause
------------------------------------------
This function temporarily suspends the currently active robot motion in the robot controller.  
If there is no active motion, the function call is ignored.

**Definition** |br|  
``DRFLEx.h`` within class `CDRFLEx`, public section (line 764)

.. code-block:: cpp

    bool move_pause() { return _move_pause(_rbtCtrl); };

**Parameter** |br|  
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error occurred while attempting to pause motion.
   * - 1
     - Successfully paused the current motion.

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

This example demonstrates how to **temporarily pause** a robot’s motion.  
When the robot’s 3rd joint reaches 45°, the motion is suspended for 5 seconds using ``move_pause()``,  
and then resumed using ``move_resume()``.
