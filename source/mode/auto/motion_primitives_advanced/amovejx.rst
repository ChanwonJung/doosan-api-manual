.. _auto_amovejx:

amovejx (Auto Mode)
------------------------------------------

This function performs **joint-space motion with an additional solution space index**,  
allowing the robot to reach the same Cartesian target using different inverse kinematic solutions.  
It is particularly useful for robots with multiple valid joint configurations for the same TCP position.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 792)

.. code-block:: cpp

   bool amovejx(float fTargetPos[NUM_JOINT],
                unsigned char iSolutionSpace,
                float fTargetVel,
                float fTargetAcc,
                float fTargetTime = 0.f,
                MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
                MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
                BLENDING_SPEED_TYPE eBlendingType = BLENDING_SPEED_TYPE_DUPLICATE) {
       return _amovejx(_rbtCtrl, fTargetPos, iSolutionSpace, fTargetVel,
                       fTargetAcc, fTargetTime, eMoveMode, eMoveReference, eBlendingType);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Target joint position for each of the six robot axes.
   * - iSolutionSpace
     - unsigned char
     - -
     - Specifies the solution space index for inverse kinematics. |br| 
       This determines which joint configuration is selected for reaching the same Cartesian target.
   * - fTargetVel
     - float
     - -
     - Joint velocity [deg/sec].
   * - fTargetAcc
     - float
     - -
     - Joint acceleration [deg/sec²].
   * - fTargetTime
     - float
     - 0.f
     - Motion completion time [sec].  
       If specified, velocity and acceleration are ignored.
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Specifies whether the movement is in absolute or relative mode.
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - ``MOVE_REFERENCE_BASE``
     - Coordinate reference of the motion (BASE or TOOL).
   * - eBlendingType
     - :ref:`BLENDING_SPEED_TYPE <enum_blending_speed_type>` 
     - ``BLENDING_SPEED_TYPE_DUPLICATE``
     - Determines blending behavior with subsequent motions.

.. Note::

  - The ``iSolutionSpace`` parameter defines the **specific kinematic configuration** among multiple valid joint-space solutions that reach the same Cartesian pose.  
    This helps control which arm posture (e.g., elbow-up/elbow-down) is used.
  - If ``fTargetTime`` is specified, the motion ignores ``fTargetVel`` and ``fTargetAcc``.
  - Use blending (``eBlendingType``) to connect sequential ``amovejx`` or ``movej`` motions smoothly.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

   // CASE 1 — Move using specific solution space (e.g., elbow-up)
   float q1[6] = { 0, -30, 60, 0, 90, 0 };
   unsigned char sol_space = 1;   // Select solution space index
   float jVel = 30;               // Joint velocity [deg/sec]
   float jAcc = 60;               // Joint acceleration [deg/sec²]
   drfl.amovejx(q1, sol_space, jVel, jAcc);
   // Moves to the target joint position using solution space 1.

   // CASE 2 — Time-based motion using same target with different configuration
   float q2[6] = { 0, -60, 120, 0, 90, 0 };
   unsigned char sol_alt = 2;     // Alternative kinematic configuration
   float move_time = 5.0f;
   drfl.amovejx(q2, sol_alt, 0, 0, move_time);
   // Moves to the target in 5 seconds with solution space 2.

   // CASE 3 — Blended transition between two configurations
   float q3[6] = { 0, -45, 90, 0, 90, 0 };
   drfl.amovejx(q1, sol_space, jVel, jAcc, 0, MOVE_MODE_ABSOLUTE, MOVE_REFERENCE_BASE, BLENDING_SPEED_TYPE_DUPLICATE);
   drfl.amovejx(q3, sol_alt, jVel, jAcc);
   // Smoothly transitions between two motion paths using blending.

This example demonstrates **multi-solution joint motion control**,  
allowing posture switching or smooth transitions between kinematic configurations in auto mode.
