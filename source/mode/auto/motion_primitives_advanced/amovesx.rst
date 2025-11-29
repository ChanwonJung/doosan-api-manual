.. _auto_amovesx:

amovesx (Auto Mode)
------------------------------------------

As an asynchronous **movesx**, this function operates the same as ``movesx()``  
except for the asynchronous process. It returns immediately after motion starts  
without waiting for its termination.  |br|
Because of this, a new motion command issued before the completion of ``amovesx()``  
will cause a safety error. Always confirm motion termination using ``mwait()``  
before executing the next command.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 801)

.. code-block:: cpp

   bool amovesx(float fTargetPos[MAX_SPLINE_POINT][NUM_TASK],
                unsigned char nPosCount,
                float fTargetVel[2],
                float fTargetAcc[2],
                float fTargetTime = 0.f,
                MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
                MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
                SPLINE_VELOCITY_OPTION eVelOpt = SPLINE_VELOCITY_OPTION_DEFAULT) {
       return _amovesx(_rbtCtrl, fTargetPos, nPosCount, fTargetVel,
                       fTargetAcc, fTargetTime, eMoveMode, eMoveReference, eVelOpt);
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
     - float[MAX_SPLINE_POINT][6]
     - -
     - Maximum 100 waypoint information
   * - nPosCount
     - unsigned char
     - -
     - Number of valid waypoints
   * - fTargetVel
     - float[2]
     - -
     - Linear and Angular Velocity
   * - fTargetAcc
     - float[2]
     - -
     - Linear and Angular Acceleration
   * - fTargetTime
     - float
     - 0.0
     - Reach time [sec]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Absolute or Relative movement mode
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - ``MOVE_REFERENCE_BASE``
     - Coordinate reference system (BASE / TOOL)
   * - eVelOpt
     - :ref:`SPLINE_VELOCITY_OPTION <enum_spline_velocity_option>` 
     - ``SPLINE_VELOCITY_OPTION_DEFAULT``
     - Velocity profile option for spline motion |br|
       (default: variable velocity spline)

.. Note::

  - If ``fTargetVel`` is given (e.g., ``{30, 0}``), 
    the first element represents **linear velocity**,  
    and the second represents **angular velocity** (determined proportionally to linear velocity).  
  - If ``fTargetAcc`` is given (e.g., ``{60, 0}``),  
    the first element defines **linear acceleration**,  
    and the second represents **angular acceleration** (proportional to linear acceleration).  
  - If ``fTargetTime`` is specified, the motion is executed based on time,  
    ignoring both ``fTargetVel`` and ``fTargetAcc``.  
  - When ``eMoveMode`` is ``MOVE_MODE_RELATIVE``,  
    each waypoint is defined **relative** to the previous waypoint.  
    (For example, in list [q1, q2, q3], q2 is relative to q1, q3 to q2, etc.)  
  - This function does **not support online blending** of previous and subsequent motions.

.. Caution::

  - When using ``SPLINE_VELOCITY_OPTION_CONST`` for ``eVelOpt`` (constant velocity spline),  
    the constant-speed profile cannot be applied if distance or velocity between input waypoints  
    does not allow uniform motion.  
    In such cases, the motion automatically switches to ``SPLINE_VELOCITY_OPTION_DEFAULT``.

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

   // Execute an asynchronous Cartesian spline motion through multiple waypoints.
   // D-Out is triggered 3 seconds after the spline motion starts.

   float xpos[4][6];
   int xposNum = 4;
   float tvel[2] = { 50, 50 };
   float tacc[2] = { 100, 100 };

   xpos[0][0]=559; xpos[0][1]=434.5; xpos[0][2]=651.5; xpos[0][3]=0; xpos[0][4]=180; xpos[0][5]=0;
   xpos[1][0]=559; xpos[1][1]=484.5; xpos[1][2]=251.5; xpos[1][3]=0; xpos[1][4]=180; xpos[1][5]=0;
   xpos[2][0]=559; xpos[2][1]=234.5; xpos[2][2]=251.5; xpos[2][3]=0; xpos[2][4]=180; xpos[2][5]=0;
   xpos[3][0]=559; xpos[3][1]=134.5; xpos[3][2]=451.5; xpos[3][3]=0; xpos[3][4]=180; xpos[3][5]=0;

   drfl.amovesx(xpos, xposNum, tvel, tacc, 0, MOVE_MODE_ABSOLUTE);
   Sleep(3000);
   drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);

This example performs an **asynchronous spline motion** through four TCP waypoints  
and activates a digital output 3 seconds after motion starts.  
The next command should only be issued after verifying completion with ``mwait()``.
