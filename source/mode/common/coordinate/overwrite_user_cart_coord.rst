.. _overwrite_user_cart_coord:

overwrite_user_cart_coord
------------------------------------------
This function **updates an existing user coordinate system** (`iReqId`) with a new pose (`fTargetPos`)  
and reference coordinate (`eTargetRef`).  
If `bTargetUpdate` is set to `true`, the update also synchronizes with the **Teach Pendant (TP)**,  
allowing global updates across both the controller and TP environment.

If `bTargetUpdate` is `false`, the coordinate system update only applies locally within the  
current program execution and is not saved after termination.

This function is supported in **M2.5 version or higher**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 979)

.. code-block:: cpp

    int overwrite_user_cart_coord(
        bool bTargetUpdate,
        int iReqId,
        float fTargetPos[NUM_TASK],
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _overwrite_user_cart_coord(_rbtCtrl, bTargetUpdate, iReqId, fTargetPos, eTargetRef);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bTargetUpdate
     - bool
     - -
     - **Determines whether the coordinate update is local or global** |br|
       0: Local update (temporary; program-only)  |br|
       1: Global update (synchronized with Teach Pendant)
   * - iReqId
     - int
     - -
     - Target coordinate ID to be overwritten. |br| 
       Must reference an existing user coordinate system.
   * - fTargetPos
     - float[6]
     - -
     - Target position and orientation values (X, Y, Z, Rx, Ry, Rz) for the updated coordinate.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for defining the new user coordinate frame

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - int
     - Returns the coordinate ID (101–200) on success. |br|
       Returns a negative value if update fails.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Create a user coordinate
       float pose1[6] = {50.0f, 40.0f, 50.0f, 0.0f, 0.0f, 0.0f};
       int user_id = drfl.set_user_cart_coord(0, pose1, COORDINATE_SYSTEM_BASE);

       // Step 2. Prepare a new pose for overwriting
       float pose2[6] = {100.0f, 150.0f, 200.0f, 45.0f, 180.0f, 0.0f};

       // Step 3. Overwrite the coordinate globally
       int result = drfl.overwrite_user_cart_coord(true, user_id, pose2);

       printf("Overwrite Result: %d\n", result);
   }

This example first creates a user-defined coordinate system,  
then overwrites its position and orientation with new values,  
synchronizing the change globally across the Teach Pendant and controller.
