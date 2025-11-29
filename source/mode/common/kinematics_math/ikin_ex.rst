.. _ikin_extension:

ikin (extension)
------------------------------------------
This function returns the joint position corresponding iSolutionSpace, which is equivalent to the robot pose in the operating space, among 8 joint shapes.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 667)

.. code-block:: cpp

    LPINVERSE_KINEMATIC_RESPONSE ikin(
        float fSourcePos[NUM_TASK],
        unsigned char iSolutionSpace,
        COORDINATE_SYSTEM eTargetRef,
        unsigned char iRefPosOpt
    ) {
        return _ikin_ex(_rbtCtrl, fSourcePos, iSolutionSpace, eTargetRef, iRefPosOpt);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fSourcePos
     - float[6]
     - -
     - Target task location for six axes (TCP pose to be solved for).
   * - iSolutionSpace
     - unsigned char
     - -
     - Solution space index (0–7) selecting one of eight IK configurations.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for the TCP.
   * - iRefPosOpt
     - unsigned char
     - -
     - Reference-pose option used by the extended IK solver (implementation-specific option).

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPINVERSE_KINEMATIC_RESPONSE <struct_inverse_kinematic_response>`
     - Extended inverse-kinematics response including the solved joint position (and related meta data).

**Example**

.. code-block:: cpp

   float x6[6] = { 370.9f, 719.7f, 651.5f, 90.f, -180.f, 0.f };
   LPINVERSE_KINEMATIC_RESPONSE res = drfl.ikin(x6, 2, COORDINATE_SYSTEM_BASE, 0);

   float q[6] = {0};
   for (int i = 0; i < 6; ++i) {
       q[i] = res->_fJoint[i];   // copy solved joints
   }
   drfl.movej(q, 60, 30);

This example solves IK for the TCP pose `x6` in the **BASE** frame with **solution space = 2** and **ref-pose option = 0**.  
The solved joint values are copied from `res->_fJoint` into `q`, then executed via `movej(q, 60, 30)` (velocity 60, acceleration 30).  
Use different solution spaces (0–7) to select another valid joint configuration for the same TCP pose.
