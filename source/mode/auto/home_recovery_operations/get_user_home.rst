.. _auto_get_user_home:

get_user_home (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_user_home <get_user_home>`  
during **Auto (Run)** operations to retrieve the **user-defined home pose**  
stored in the robot controller.

The user home pose is typically configured beforehand using  
:ref:`set_user_home <auto_set_user_home>` and is often used as a safe return  
position during automated workflows.

**Typical usage**

- Retrieve the saved home position before executing a homing or return-to-base motion.  
- Log the home pose for debugging, calibration, or system validation.  
- Check the current stored home pose after an operator updates it on the teach pendant.  
- Use as a reference point for workspace initialization or task resets.  

.. Note::

   - Returns a pointer to :ref:`ROBOT_POSE <struct_ROBOT_POSE>`.  
   - Always validate the returned pointer before accessing pose values.  

**Example: Reading and Printing the User-Defined Home Position**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Retrieve the user-defined home pose
       LPROBOT_POSE home = drfl.get_user_home();

       if (!home) {
           std::cout << "Failed to retrieve user home pose." << std::endl;
           return -1;
       }

       // 2) Print the home pose values
       std::cout << "User Home Position:" << std::endl;
       std::cout << "X:  " << home->_fTargetPos[0] << std::endl;
       std::cout << "Y:  " << home->_fTargetPos[1] << std::endl;
       std::cout << "Z:  " << home->_fTargetPos[2] << std::endl;
       std::cout << "Rx: " << home->_fTargetPos[3] << std::endl;
       std::cout << "Ry: " << home->_fTargetPos[4] << std::endl;
       std::cout << "Rz: " << home->_fTargetPos[5] << std::endl;

       return 0;
   }

In this example, the program retrieves the saved user home pose  
and prints the Cartesian coordinates and orientation values,  
allowing the automation system to confirm or log the reference position  
before moving the robot.

**Tips**

- Ideal for verifying the home pose before executing a return-to-home sequence.  
- Useful when operators frequently update home positions in the field.  
- Combine with motion functions such as ``movej`` or ``amovel`` to automate homing routines.  
- Log home pose values to ensure consistent setup across shifts or production cycles.  
