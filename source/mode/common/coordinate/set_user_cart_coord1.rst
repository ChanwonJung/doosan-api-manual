.. _set_user_cart_coord1:

set_user_cart_coord1
------------------------------------------
This function defines a **new user Cartesian coordinate system** using an input pose (`fTargetPos`)  
and a reference coordinate system (`eTargetRef`).  
Up to **20 user coordinate systems** can be created, either automatically or manually (IDs 101–120).  
Since coordinate systems set via this function are not persistent after program termination,  
it is recommended to register them within the Workcell configuration for long-term use.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 972)

.. code-block:: cpp

    int set_user_cart_coord(
        int iReqId,
        float fTargetPos[NUM_TASK],
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _set_user_cart_coord1(_rbtCtrl, iReqId, fTargetPos, eTargetRef);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iReqId
     - int
     - -
     - Requested coordinate ID |br|
       0: Auto-created by the system (next available ID) |br|
       101-120: Manual coordinate ID
   * - fTargetPos
     - float[6]
     - -
     - Target task position for six axes (X, Y, Z, Rx, Ry, Rz) defining the new user frame.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system from which the new user coordinate is defined.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - int
     - ID of the successfully created or modified user coordinate system (101–200). |br|  
       Returns negative on failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define a new user coordinate system using current robot pose
       float pose[6] = {200.0f, 30.0f, 500.0f, 0.0f, 0.0f, 0.0f};

       // Create coordinate system ID automatically
       int coord_id = drfl.set_user_cart_coord(0, pose, COORDINATE_SYSTEM_BASE);

       printf("New user coordinate system set with ID: %d\n", coord_id);
   }

This example creates a new user-defined Cartesian coordinate frame using a target pose  
relative to the base coordinate system and prints the assigned coordinate ID.
