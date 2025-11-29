.. _set_ref_coord:

set_ref_coord
------------------------------------------
This function sets the **reference coordinate system** used for motion commands.  
All subsequent Cartesian movements and operations will be executed relative to  
the coordinate system specified by `eTargetCoordSystem`.

If not explicitly changed, the reference coordinate defaults to the **base coordinate system**.  
This function is frequently used when switching between **base**, **tool**, or **user-defined** frames  
to ensure positional accuracy during complex motion planning.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 976)

.. code-block:: cpp

    bool set_ref_coord(COORDINATE_SYSTEM eTargetCoordSystem) {
        return _set_ref_coord(_rbtCtrl, eTargetCoordSystem);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eTargetCoordSystem
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - The reference coordinate system to set. |br| 
       Common values include:  |br|
       - `COORDINATE_SYSTEM_BASE` : Robot base frame  |br|
       - `COORDINATE_SYSTEM_TOOL` : Current tool frame  |br|
       - `COORDINATE_SYSTEM_USER` : User-defined coordinate frame

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed to set the reference coordinate system
   * - 1
     - Successfully set the reference coordinate system

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define a Cartesian move in base coordinates
       float p1[6] = {0.f, 0.f, 90.f, 0.f, 90.f, 0.f};
       drfl.movej(p1, 60, 30);

       // Create a custom user coordinate system
       float vec[2][3] = {{-1.f, 1.f, 1.f}, {1.f, 1.f, 0.f}};
       float org[3] = {370.9f, -419.7f, 651.5f};
       int user_id = drfl.set_user_cart_coord(vec, org);

       // Change reference coordinate to the user frame
       drfl.set_ref_coord((COORDINATE_SYSTEM)user_id);
   }

This example defines a new user coordinate system and  
sets it as the reference frame, so all subsequent motion commands  
(e.g., ``movej`` or ``movel``) are executed relative to this user-defined coordinate system.
