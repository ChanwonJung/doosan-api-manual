.. _set_user_cart_coord3:

set_user_cart_coord3 (vector method)
------------------------------------------
This function defines a **new user Cartesian coordinate system** using two input direction vectors  
(`fTargetVec[0]`, `fTargetVec[1]`) and an **origin position** (`fTargetOrg`) relative to a  
reference coordinate system (`eTargetRef`).  

- `fTargetVec[0]` defines the **X-axis** direction vector. |br|
- `fTargetVec[1]` defines the **Y-axis** reference vector.  |br|

The **Z-axis** is automatically computed as the cross-product of X × Y, ensuring orthogonality. 
If the provided vectors are not perfectly orthogonal, the system internally normalizes them to  
construct a valid right-handed coordinate frame.

This function is available in **M2.5 hotfix version or higher** and allows up to **20 user coordinate systems**.  
Coordinate systems created with this function are temporary and will be removed after program termination;  
for persistence, register them in the Workcell configuration.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 974)

.. code-block:: cpp

    int set_user_cart_coord(
        float fTargetVec[2][3],
        float fTargetOrg[3],
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _set_user_cart_coord3(_rbtCtrl, fTargetVec, fTargetOrg, eTargetRef);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetVec
     - float[2][3]
     - -
     - Two 3D vectors defining the coordinate orientation: |br|
       - **Vector 1** → X-axis direction |br| 
       - **Vector 2** → Y-axis reference direction
   * - fTargetOrg
     - float[3]
     - -
     - Origin position (X, Y, Z) of the user coordinate system.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system from which the new coordinate frame is defined.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - int
     - ID of the successfully created coordinate system (101–200).  |br|
       Returns negative on failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define X and Y direction vectors for the new coordinate frame
       float vec[2][3] = {
           {1.0f, 1.0f, 1.0f},   // X-axis vector
           {1.0f, 0.0f, 0.0f}    // Y-axis reference vector
       };

       // Define the origin position
       float org[3] = {370.0f, -45.0f, 521.5f};

       // Create a new user coordinate system using vector method
       int coord_id = drfl.set_user_cart_coord(vec, org, COORDINATE_SYSTEM_BASE);

       printf("User coordinate (vector method) created with ID: %d\n", coord_id);
   }

This example defines a new user Cartesian coordinate frame using two direction vectors  
and an origin position, then registers it relative to the base coordinate system.
