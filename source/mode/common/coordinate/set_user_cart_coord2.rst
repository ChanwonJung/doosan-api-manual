.. _set_user_cart_coord2:

set_user_cart_coord2 (3-point method)
------------------------------------------
This function defines a **new user Cartesian coordinate system** using **three input poses**  
(`fTargetPos[0]`, `fTargetPos[1]`, and `fTargetPos[2]`) and an **origin position** (`fTargetOrg`)  
relative to the reference coordinate system (`eTargetRef`).  

The three input poses specify the orientation and alignment of the new coordinate axes: |br| 
- The **X-axis** is determined by the vector from pose₁ → pose₂. |br|
- The **Z-axis** is calculated as the cross-product of the vectors (pose₂ − pose₁) × (pose₃ − pose₁). |br| 
- The **Y-axis** is computed as the cross-product of Z × X.  

Up to **20 user coordinate systems** can be created (IDs 101–120).  
Since coordinate systems set by this function are not persistent after program termination,  
it is recommended to register them within the Workcell configuration for long-term use.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 973)

.. code-block:: cpp

    int set_user_cart_coord(
        float fTargetPos[3][NUM_TASK],
        float fTargetOrg[3],
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _set_user_cart_coord2(_rbtCtrl, fTargetPos, fTargetOrg, eTargetRef);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[3][6]
     - -
     - Three target task positions defining the plane of the new user coordinate |br|
       - Pose #1: reference start point  |br|
       - Pose #2: defines X-axis direction  |br|
       - Pose #3: defines the plane for Z-axis orientation |br|
   * - fTargetOrg
     - float[3]
     - -
     - Origin position (X, Y, Z) of the new user coordinate system.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system from which the new coordinate is defined. 

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - int
     - ID of the successfully created coordinate system (101–200). |br|
       Returns negative on failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define three poses to establish the coordinate plane
       float x1[6] = {0.0f, 200.0f, 700.0f, 0.0f, 0.0f, 0.0f};
       float x2[6] = {0.0f, 700.0f, 0.0f, 0.0f, 0.0f, 0.0f};
       float x3[6] = {0.0f, 200.0f, 0.0f, 0.0f, 0.0f, 0.0f};

       // Set the origin position
       float org[3] = {10.0f, 30.0f, 15.0f};

       // Register a new user coordinate system based on the three poses
       int coord_id = drfl.set_user_cart_coord({x1, x2, x3}, org, COORDINATE_SYSTEM_BASE);

       printf("User coordinate created with ID: %d\n", coord_id);
   }

This example defines a user Cartesian coordinate frame using three task-space poses  
and an origin offset, then registers it relative to the base coordinate system.
