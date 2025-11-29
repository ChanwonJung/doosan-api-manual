.. _get_external_torque:

get_external_torque
------------------------------------------
This function retrieves the **external torque values** acting on each robot joint,  
as estimated by the torque sensors and dynamic model inside the controller.  
These values represent the external interaction torques due to contact, load, or environmental forces.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 733)

.. code-block:: cpp

    LPROBOT_FORCE get_external_torque() {
        return _get_external_torque(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_FORCE <struct_ROBOT_FORCE>`
     - Pointer to a  structure containing the **external torque** (interaction torque) of each joint (J1–J6). |br|
       Units: **N·m**

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume robot is connected and in operation mode

       LPROBOT_FORCE lpExtTq = drfl.get_external_torque();
       if (lpExtTq) {
           printf("External Torque Values [N·m]:\n");
           for (int i = 0; i < NUMBER_OF_JOINT; ++i) {
               printf("Joint %d: %.3f\n", i + 1, lpExtTq->_fTorque[i]);
           }
       } else {
           fprintf(stderr, "Failed to retrieve external torque data.\n");
       }

       return 0;
   }

This example queries and prints the **estimated external torque on each joint** in Newton-meters (N·m).  
These values are typically small when the robot is free of contact,  
but increase when external forces (e.g., collisions or human interaction) occur.
