.. _get_current_posj:

get_current_posj
------------------------------------------
This is a function for checking information on the current joint angle by axis of the robot in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 715)

.. code-block:: cpp

    LPROBOT_POSE get_current_posj() { 
        return _get_current_posj(_rbtCtrl); 
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_POSE <struct_robot_pose>`
     - Refer to the Definition of Structure

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx drfl;

        // Retrieve the current joint positions (in radians)
        LPROBOT_POSE lpPose = drfl.get_current_posj();

        if (lpPose != nullptr) {
            std::cout << "Current Joint Angles (rad):" << std::endl;
            for (int i = 0; i < NUMBER_OF_JOINT; ++i) {
                std::cout << "  Joint " << (i + 1) << ": " << lpPose->_fPos[i] << std::endl;
            }
        } else {
            std::cerr << "Failed to retrieve joint positions." << std::endl;
        }

        return 0;
    }

This example retrieves the **current joint angles** of all robot axes from the controller  
and prints them to the console.  
Each element in the returned `ROBOT_POSE` structure represents the **current position of a joint**  
in **radians** (or **degrees**, depending on the system configuration).  
This function is commonly used in motion monitoring, calibration routines,  
or when synchronizing the robot’s state with external systems.
