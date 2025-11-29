.. _ikin_add_iter_threshold:

ikin (with iteration threshold)
------------------------------------------
This function returns the joint position corresponding to the target TCP position (`fSourcePos`)  
while allowing the user to specify iteration thresholds for the IK solver.  
This extended version provides finer control over the numerical convergence behavior  
compared to the standard `ikin()` function.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 668)

.. code-block:: cpp

    LPINVERSE_KINEMATIC_RESPONSE ikin(
        float fSourcePos[NUM_TASK],
        unsigned char iSolutionSpace,
        COORDINATE_SYSTEM eTargetRef,
        float fIterThreshold[NUMBER_OF_ITER_THRESHOULD]
    ) {
        return _ikin_add_iter_threshold(_rbtCtrl, fSourcePos, iSolutionSpace, eTargetRef, fIterThreshold);
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
     - Target TCP position (x, y, z, Rx, Ry, Rz) in task space.
   * - iSolutionSpace
     - unsigned char
     - -
     - Solution space index (0–7). |br|
       Selects one of eight inverse-kinematics configurations.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for the TCP pose. 
   * - fIterThreshold
     - float[NUMBER_OF_ITER_THRESHOULD]
     - -
     - Iteration threshold values used in the IK solver to define |br|
       convergence precision or tolerance for each joint dimension.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPINVERSE_KINEMATIC_RESPONSE <struct_inverse_kinematic_response>`
     - Extended inverse-kinematics response structure containing the calculated |br|
       joint positions and solver convergence information.  

**Example**

.. code-block:: cpp

   float tcp_target[6] = { 400.0f, 500.0f, 600.0f, 90.0f, 0.0f, 180.0f };
   float iter_th[NUMBER_OF_ITER_THRESHOULD] = { 0.01f, 0.01f, 0.01f, 0.001f, 0.001f, 0.001f };

   LPINVERSE_KINEMATIC_RESPONSE result =
       drfl.ikin(tcp_target, 2, COORDINATE_SYSTEM_BASE, iter_th);

   float q_solved[6] = { 0 };
   for (int i = 0; i < 6; ++i)
       q_solved[i] = result->_fJoint[i];

   drfl.movej(q_solved, 60, 30);

In this example, the function calculates an **inverse kinematics solution**  
with a tighter iteration threshold, improving solver precision when working with  
high-accuracy motion requirements or sensitive tasks such as calibration or assembly.
