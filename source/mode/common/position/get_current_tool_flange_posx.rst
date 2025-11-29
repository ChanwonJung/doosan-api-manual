.. _get_current_tool_flange_posx:

get_current_tool_flange_posx
------------------------------------------
This is a function for checking information on the tool flange pose of the robot in the robot controller.  
At this time, the posture is based on `eTargetRef`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 723)

.. code-block:: cpp

    LPROBOT_POSE get_current_tool_flange_posx() { 
        return _get_current_tool_flange_posx(_rbtCtrl); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Target coordinate reference frame.

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

        // Retrieve current flange pose relative to the base coordinate system
        LPROBOT_POSE lpCurrentFlange = drfl.get_current_tool_flange_posx(COORDINATE_SYSTEM_BASE);

        // Retrieve desired pose relative to the tool coordinate system
        LPROBOT_POSE lpDesiredFlange = drfl.get_desired_posx(COORDINATE_SYSTEM_TOOL);

        if (lpCurrentFlange && lpDesiredFlange) {
            std::cout << "Current Flange Pose (Base Frame):" << std::endl;
            std::cout << "  X: " << lpCurrentFlange->_fX << ", Y: " << lpCurrentFlange->_fY
                      << ", Z: " << lpCurrentFlange->_fZ << std::endl;
            std::cout << "  Rx: " << lpCurrentFlange->_fRx << ", Ry: " << lpCurrentFlange->_fRy
                      << ", Rz: " << lpCurrentFlange->_fRz << std::endl;

            std::cout << "\nDesired Flange Pose (Tool Frame):" << std::endl;
            std::cout << "  X: " << lpDesiredFlange->_fX << ", Y: " << lpDesiredFlange->_fY
                      << ", Z: " << lpDesiredFlange->_fZ << std::endl;
            std::cout << "  Rx: " << lpDesiredFlange->_fRx << ", Ry: " << lpDesiredFlange->_fRy
                      << ", Rz: " << lpDesiredFlange->_fRz << std::endl;

            // Simple positional deviation check (Euclidean distance)
            float deltaX = lpDesiredFlange->_fX - lpCurrentFlange->_fX;
            float deltaY = lpDesiredFlange->_fY - lpCurrentFlange->_fY;
            float deltaZ = lpDesiredFlange->_fZ - lpCurrentFlange->_fZ;
            float distanceError = std::sqrt(deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ);

            std::cout << "\nTranslation Error (mm): " << distanceError << std::endl;
        } else {
            std::cerr << "Failed to retrieve flange pose data." << std::endl;
        }

        return 0;
    }

In this example, the **current flange pose** is obtained in the **base coordinate frame**,  
while the **desired TCP pose** is retrieved relative to the **tool coordinate frame**.  
Both poses include **Cartesian position (X, Y, Z)** and **orientation (Rx, Ry, Rz)**.  
The example calculates the **translational deviation** between the two poses,  
which can be used to assess **trajectory accuracy**, **tool calibration**, or **alignment performance**.
