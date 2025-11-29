.. _auto_movesj:

movesj (Auto Mode)
------------------------------------------

This function moves the robot along a **spline curve** that connects the **current joint position**
to the **final joint position (last waypoint)** through a list of waypoints in **joint space**.
The input velocity/acceleration represent the **maximum velocity/acceleration along the path**;
actual accel/decel are automatically distributed according to each waypoint segment.

.. figure:: /tutorials/images/mode/movesj_overview.png
   :alt: movesj
   :width: 80%
   :align: center

.. raw:: html
      
   <br>

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 795)

.. code-block:: cpp

   bool movesj(float fTargetPos[MAX_SPLINE_POINT][NUM_JOINT],
               unsigned char nPosCount,
               float fTargetVel,
               float fTargetAcc,
               float fTargetTime = 0.f,
               MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE) {
       return _movesj(_rbtCtrl, fTargetPos, nPosCount, fTargetVel,
                      fTargetAcc, fTargetTime, eMoveMode);
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
     - Float\[MAX_SPLINE_POINT][6]
     - -
     - Waypoint list (maximum **100** waypoints)
   * - nPosCount
     - unsigned char
     - -
     - Number of valid waypoints
   * - fTargetVel
     - float / float\[6]
     - -
     - Velocity (scalar or per-joint)
   * - fTargetAcc
     - float / float\[6]
     - -
     - Acceleration (scalar or per-joint)
   * - fTargetTime
     - float
     - 0.f
     - Reach time [sec]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Enumeration Type

.. Note::

  - When ``fTargetTime`` is specified, motion is processed based on the **time**,
    ignoring ``fTargetVel`` and ``fTargetAcc``.
  - When ``eMoveMode`` is ``MOVE_MODE_RELATIVE``, each waypoint in the list is defined
    **relative to the previous waypoint** (e.g., if the list is \[q1, q2, …, q(n)],
    ``q1`` is relative to the start pose and ``q(n)`` is relative to ``q(n-1)``).
  - This function **does not support online blending** with previous/subsequent motions.

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

   // CASE 1 : Absolute coordinate input (mode = MOVE_MODE_ABSOLUTE)
   float jpos[4][6];
   float jvel = 10;
   float jacc = 10;
   int   jposNum = 4;

   // q0
   jpos[0][0]=0;   jpos[0][1]=0;   jpos[0][2]=-30; jpos[0][3]=0;  jpos[0][4]=-30; jpos[0][5]=0;
   // q1
   jpos[1][0]=90;  jpos[1][1]=0;   jpos[1][2]=0;   jpos[1][3]=0;  jpos[1][4]=0;   jpos[1][5]=0;
   // q2
   jpos[2][0]=0;   jpos[2][1]=0;   jpos[2][2]=-30; jpos[2][3]=0;  jpos[2][4]=-30; jpos[2][5]=0;
   // q3 (goal)
   jpos[3][0]=0;   jpos[3][1]=0;   jpos[3][2]=0;   jpos[3][3]=0;  jpos[3][4]=0;   jpos[3][5]=0;

   drfl.movesj(jpos, jposNum, jvel, jacc);
   // Moves the spline curve through absolute waypoints with max velocity 10(deg/s)
   // and max acceleration 10(deg/s^2).

   // CASE 2 : Relative angle input (mode = MOVE_MODE_RELATIVE)
   float rpos[4][6];
   jvel = 10; jacc = 10; jposNum = 4;

   // Relative waypoints (each is relative to the previous)
   rpos[0][0]=0;   rpos[0][1]=0;   rpos[0][2]=-30; rpos[0][3]=0;  rpos[0][4]=-30; rpos[0][5]=0;
   rpos[1][0]=90;  rpos[1][1]=0;   rpos[1][2]=0;   rpos[1][3]=0;  rpos[1][4]=0;   rpos[1][5]=0;
   rpos[2][0]=-90; rpos[2][1]=0;   rpos[2][2]=-30; rpos[2][3]=0;  rpos[2][4]=-30; rpos[2][5]=0;
   rpos[3][0]=0;   rpos[3][1]=0;   rpos[3][2]=30;  rpos[3][3]=0;  rpos[3][4]=30;  rpos[3][5]=0;

   drfl.movesj(rpos, jposNum, jvel, jacc, 0, MOVE_MODE_RELATIVE);

This example first runs a **spline in absolute joint coordinates** and then repeats using **relative waypoints**, where each row is applied w.r.t. the preceding joint state. Use ``fTargetTime`` when you need a fixed-duration spline regardless of velocity/acceleration limits.
