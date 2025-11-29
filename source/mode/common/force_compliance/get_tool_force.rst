.. _get_tool_force:

get_tool_force
------------------------------------------
This function retrieves the **force and moment applied at the robot tool center point (TCP)**.  
The force is expressed relative to the specified coordinate system (default: BASE).  
Internally, it is estimated using joint torque sensors and the robot's dynamic model.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 735)

.. code-block:: cpp

    LPROBOT_FORCE get_tool_force(COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE) {
        return _get_tool_force(_rbtCtrl, eTargetRef);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system in which the TCP force is expressed. 

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_FORCE <struct_ROBOT_FORCE>`
     - Pointer to a structure containing the **estimated TCP force (Fx, Fy, Fz)** and **moment (Mx, My, Mz)**.  |br|
       Force unit: **N**, Moment unit: **N·m**

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume robot connection and operation mode initialized

       LPROBOT_FORCE lpForce = drfl.get_tool_force(COORDINATE_SYSTEM_BASE);
       if (lpForce) {
           printf("Tool Force and Moment (Base Coordinate)\n");
           printf("Force  [N]:  Fx=%.2f  Fy=%.2f  Fz=%.2f\n",
                  lpForce->_fForce[0],
                  lpForce->_fForce[1],
                  lpForce->_fForce[2]);
           printf("Moment [N·m]: Mx=%.3f  My=%.3f  Mz=%.3f\n",
                  lpForce->_fTorque[0],
                  lpForce->_fTorque[1],
                  lpForce->_fTorque[2]);
       } else {
           fprintf(stderr, "Failed to retrieve tool force.\n");
       }

       return 0;
   }

This example prints the **current force and torque applied at the TCP**,  
expressed in the **base coordinate system**. |br| 
It can be used for: |br|

- Detecting contact with objects (e.g., surface alignment)
- Measuring external forces during force-control applications
- Validating compliance and impedance control responses
