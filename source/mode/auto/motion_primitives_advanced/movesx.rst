.. _auto_movesx:

movesx (Auto Mode)
----------------------

This is a function for moving the robot along a spline curve path that connects the current position to the target position (the last waypoint) via the waypoints of the task space.  
The input velocity/acceleration means the **maximum** velocity/acceleration in the path, and the **constant-speed** motion is performed with the input velocity according to the condition if the option for constant speed motion is selected.

.. figure:: /tutorials/images/mode/movesx_overview.png
   :alt: movesx
   :width: 80%
   :align: center

.. raw:: html
      
   <br>

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 800)

.. code-block:: cpp

    bool movesx(float fTargetPos[MAX_SPLINE_POINT][NUM_TASK],
                unsigned char nPosCount,
                float fTargetVel[2],
                float fTargetAcc[2],
                float fTargetTime = 0.f,
                MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
                MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
                SPLINE_VELOCITY_OPTION eVelOpt = SPLINE_VELOCITY_OPTION_DEFAULT)
    { 
        return _movesx(_rbtCtrl, fTargetPos, nPosCount, fTargetVel, fTargetAcc,
                       fTargetTime, eMoveMode, eMoveReference, eVelOpt);
    };

**Parameter** |br|

.. list-table::
   :widths: 22 18 15 45
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float \[MAX_SPLINE_POINT\]\[6\]
     - -
     - Maximum 100 waypoint information
   * - nPosCount
     - unsigned char
     - -
     - Number of valid waypoint
   * - fTargetVel
     - float\[2\]
     - -
     - Linear Velocity, Angular Velocity
   * - fTargetAcc
     - float\[2\]
     - -
     - Linear Acceleration, Angular Acceleration
   * - fTargetTime
     - float
     - 0.f
     - Reach Time \[sec\]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Enumeration Type
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - ``MOVE_REFERENCE_BASE``
     - Refer to the Definition of Enumeration Type
   * - eVelOpt
     - :ref:`SPLINE_VELOCITY_OPTION <enum_spline_velocity_option>` 
     - ``SPLINE_VELOCITY_OPTION_DEFAULT``
     - Refer to the Definition of Enumeration Type

.. Note::

   - If an argument is inputted to **fTargetVel** (e.g., ``fTargetVel ={30, 0}``), the input corresponds to the linear velocity of the motion, while the angular velocity is determined proportionally to the linear velocity.
   - If an argument is inputted to **fTargetAcc** (e.g., ``fTargetAcc ={60, 0}``), the input corresponds to the linear acceleration of the motion, while the angular acceleration is determined proportionally to the linear acceleration.
   - If **fTargetTime** is specified, values are processed based on **fTargetTime**, ignoring **fTargetVel** and **fTargetAcc**.
   - When **eMoveMode** is ``MOVE_MODE_RELATIVE``, each pos of the position list is defined as a relative coordinate for the preceding pos. (If position list=\[q1, q2, …,q(n-1), q(n)\], **q1** is the relative angle of the starting point, while **q(n)** is the relative coordinate of **q(n-1)**.)
   - This function does not support online blending of previous and subsequent motions.

.. Caution::

   The constant-velocity motion according to the distance and velocity between the input waypoints **cannot be used** if the ``SPLINE_VELOCITY_OPTION_CONST`` option (constant-velocity option) is selected for **eVelOpt**, and the motion is automatically switched to the variable-velocity motion (``eVelOpt = SPLINE_VELOCITY_OPTION_DEFAULT``) in that case.

**Return**

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

    // CASE 1 : Moves absolute coordinate standard (mode = MOVE_MODE_ABSOLUTE)
    float xpos[4][6];
    int   xposNum = 4;
    float tvel[2] = { 50, 100 };
    float tacc[2] = { 50, 100 };

    xpos[0][0]=559; xpos[0][1]=434.5; xpos[0][2]=651.5;
    xpos[0][3]=0;   xpos[0][4]=180;  xpos[0][5]=0;

    xpos[1][0]=559; xpos[1][1]=434.5; xpos[1][2]=251.5;
    xpos[1][3]=0;   xpos[1][4]=180;  xpos[1][5]=0;

    xpos[2][0]=559; xpos[2][1]=234.5; xpos[2][2]=251.5;
    xpos[2][3]=0;   xpos[2][4]=180;  xpos[2][5]=0;

    xpos[3][0]=559; xpos[3][1]=234.5; xpos[3][2]=451.5;
    xpos[3][3]=0;   xpos[3][4]=180;  xpos[3][5]=0;

    drfl.movesx(xpos, xposNum, tvel, tacc, 0, MOVE_MODE_ABSOLUTE);
    // Moves the spline curve that connects the waypoints defined in xpos
    // with a maximum linear/angular velocity of 50 and maximum acceleration of 100.

    // CASE 2 : Moves relative coordinate standard (mode = MOVE_MODE_RELATIVE)
    float xpos2[4][6];
    xpos2[0][0]=0;   xpos2[0][1]=+400; xpos2[0][2]=0;
    xpos2[0][3]=0;   xpos2[0][4]=0;    xpos2[0][5]=0;   // from start position -> x0

    xpos2[1][0]=0;   xpos2[1][1]=0;   xpos2[1][2]=+400;
    xpos2[1][3]=0;   xpos2[1][4]=0;   xpos2[1][5]=0;   // from x0 -> x1

    xpos2[2][0]=0;   xpos2[2][1]=+200; xpos2[2][2]=0;
    xpos2[2][3]=0;   xpos2[2][4]=0;    xpos2[2][5]=0;   // from x1 -> x2

    xpos2[3][0]=0;   xpos2[3][1]=0;    xpos2[3][2]=+200;
    xpos2[3][3]=0;   xpos2[3][4]=0;    xpos2[3][5]=0;   // from x2 -> x3

    drfl.movesx(xpos2, xposNum, tvel, tacc, 0, MOVE_MODE_RELATIVE);
    // Moves the spline curve that connects the relative waypoints in xpos2
    // with max velocity 50 (mm/sec, deg/sec) and max acceleration 100 (mm/sec2, deg/sec2).
