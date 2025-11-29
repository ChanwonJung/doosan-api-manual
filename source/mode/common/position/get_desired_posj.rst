.. _get_desired_posj:

get_desired_posj
------------------------------------------
This is a function for checking information on the desired joint angle by axis of the robot in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 721)

.. code-block:: cpp

    LPROBOT_POSE get_desired_posj() { 
        return _get_desired_posj(_rbtCtrl); 
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
    #include <cmath>
    using namespace DRAFramework;

    int main() {
        CDRFLEx drfl;

        // Retrieve the desired joint positions (target values commanded by controller)
        LPROBOT_POSE lpDesired = drfl.get_desired_posj();
        LPROBOT_POSE lpCurrent = drfl.get_current_posj();

        if (lpDesired && lpCurrent) {
            std::cout << "Comparing Desired vs Current Joint Angles:" << std::endl;
            for (int i = 0; i < NUMBER_OF_JOINT; ++i) {
                float error = std::fabs(lpDesired->_fPos[i] - lpCurrent->_fPos[i]);
                std::cout << "  Joint " << (i + 1)
                          << " | Desired: " << lpDesired->_fPos[i]
                          << " | Current: " << lpCurrent->_fPos[i]
                          << " | Error: " << error << std::endl;
            }
        } else {
            std::cerr << "Failed to retrieve joint position data." << std::endl;
        }

        return 0;
    }

This example retrieves both the **desired joint angles** (commanded by the motion controller)  
and the **current joint angles** (actual feedback from encoders), then compares them.  
The difference between these values represents the **motion tracking error** during movement.  
This function is particularly useful for **real-time monitoring, trajectory debugging,  
or fine-tuning controller response accuracy** in dynamic applications.
