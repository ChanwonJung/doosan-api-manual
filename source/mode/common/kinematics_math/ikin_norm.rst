.. _ikin_norm:

ikin_norm
------------------------------------------
This function performs inverse kinematics with normalization applied to the resulting joint angles.  
It calculates the joint position corresponding to the given TCP pose (`fSourcePos`)  
and adjusts the output to remain within normalized joint limits,  
ensuring consistent solutions across different configurations.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 669)

.. code-block:: cpp

    LPINVERSE_KINEMATIC_RESPONSE ikin_norm(
        float fSourcePos[NUM_TASK],
        unsigned char iSolutionSpace,
        COORDINATE_SYSTEM eTargetRef,
        unsigned char iRefPosOpt
    ) {
        return _ikin_norm(_rbtCtrl, fSourcePos, iSolutionSpace, eTargetRef, iRefPosOpt);
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
     - Target TCP position in task space (x, y, z, Rx, Ry, Rz).
   * - iSolutionSpace
     - unsigned char
     - -
     - Solution space index (0-7) selecting one of eight valid IK configurations.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for the TCP.
   * - iRefPosOpt
     - unsigned char
     - -
     - Reference pose option used by the normalized IK solver (e.g., |br|
       to constrain solutions within a specified configuration neighborhood).

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - LPINVERSE_KINEMATIC_RESPONSE
     - Normalized inverse-kinematics response structure containing |br|
       the calculated and normalized joint positions. |br|
       Refer to the definition of the structure in the **Structures** section.

**Example**

.. code-block:: cpp

   float tcp_pose[6] = { 500.0f, 400.0f, 300.0f, 180.0f, 0.0f, 90.0f };
   LPINVERSE_KINEMATIC_RESPONSE res = drfl.ikin_norm(tcp_pose, 1, COORDINATE_SYSTEM_BASE, 0);

   float q_normalized[6] = {0};
   for (int i = 0; i < 6; ++i)
       q_normalized[i] = res->_fJoint[i];   // normalized joint angles

   drfl.movej(q_normalized, 50, 20);

In this example, the target TCP pose `tcp_pose` is solved for **solution space 1** in the **BASE** frame.  
The resulting joint angles are **normalized** (e.g., within ±π range) to prevent discontinuities.  
This is useful when performing continuous path motions or calibration that require consistent joint states.
