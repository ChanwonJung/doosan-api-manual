.. _get_user_cart_coord:

get_user_cart_coord
------------------------------------------
This function retrieves the **pose and reference coordinate system** of the specified user coordinate system (`iReqId`).  
It returns detailed information such as the coordinate’s origin, orientation, and base reference.  

This function is available in **M2.5 or higher** versions.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 978)

.. code-block:: cpp

    LPUSER_COORDINATE get_user_cart_coord(int iReqId) {
        return _get_user_cart_coord(_rbtCtrl, iReqId);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iReqId
     - int
     - -
     - The ID of the user coordinate system to be retrieved. |br|
       Must correspond to a valid user coordinate previously defined using ``<set_user_cart_coord>``.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPUSER_COORDINATE <struct_USER_COORDINATE>` *
     - Pointer to the structure containing the user coordinate information.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define and register a new user coordinate system
       float pos[6] = {10.0f, 20.0f, 30.0f, 0.0f, 0.0f, 0.0f};
       int coord_id = drfl.set_user_cart_coord(0, pos);

       // Retrieve the coordinate system information
       LPUSER_COORDINATE coord = drfl.get_user_cart_coord(coord_id);

       printf("User Coord ID: %d | Origin: (%.2f, %.2f, %.2f)\n",
              coord_id,
              coord->_fOriginPos[0], coord->_fOriginPos[1], coord->_fOriginPos[2]);
   }

This example creates a user-defined coordinate system, retrieves its stored  
pose and reference information using the coordinate ID, and prints the origin position.
