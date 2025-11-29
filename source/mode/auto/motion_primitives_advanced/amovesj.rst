.. _auto_amovesj:

amovesj (Auto Mode)
------------------------------------------

As an asynchronous **movesj**, it operates the same as ``movesj()`` except for the asynchronous
process, and executes the next line by returning as soon as motion starts **without waiting** for
the termination of motion. |br|
A new motion command generated before the motion is terminated by
``amovesj()`` causes errors for security reasons. Therefore, the **termination** of the ``amovesj()``
motion must be confirmed using ``mwait()`` between ``amovesj()`` and the following motion command
before the new motion command is executed.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 797)

.. code-block:: cpp

   bool amovesj(float fTargetPos[MAX_SPLINE_POINT][NUM_JOINT],
                unsigned char nPosCount,
                float fTargetVel,
                float fTargetAcc,
                float fTargetTime = 0.f,
                MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE) {
       return _amovesj(_rbtCtrl, fTargetPos, nPosCount, fTargetVel,
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
     - Float[MAX_SPLINE_POINT][6]
     - -
     - Maximum 100 waypoint list
   * - nPosCount
     - unsigned char
     - -
     - Number of valid waypoints
   * - fTargetVel
     - float / float[6]
     - -
     - Velocity
   * - fTargetAcc
     - float / float[6]
     - -
     - Acceleration
   * - fTargetTime
     - float
     - 0.0
     - Reach Time [sec]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Constant and Enumeration Type

.. Note::

  - When ``fTargetTime`` is specified, values are processed based on ``fTargetTime``, ignoring ``fTargetVel`` and ``fTargetAcc``.
  - When ``eMoveMode`` is ``MOVE_MODE_RELATIVE``, each pos on the position list is defined as a **relative coordinate** for the preceding pos.  
    (If position list = [q1, q2, …, q(n-1), q(n)], q1 is the relative angle from the start point, while q(n) is the relative coordinate of q(n-1).)
  - This function does **not** support online blending of previous and subsequent motions.

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

   // D-Out 3 seconds after the spline motion through all points of jpos begins
   float jpos[4][6];
   float jvel = 10;
   float jacc = 10;
   int jposNum = 4;

   jpos[0][0]=0;  jpos[0][1]=0;  jpos[0][2]=-30; jpos[0][3]=0;  jpos[0][4]=-30; jpos[0][5]=0;
   jpos[1][0]=90; jpos[1][1]=0;  jpos[1][2]=0;   jpos[1][3]=0;  jpos[1][4]=0;   jpos[1][5]=0;
   jpos[2][0]=0;  jpos[2][1]=0;  jpos[2][2]=-30; jpos[2][3]=0;  jpos[2][4]=-30; jpos[2][5]=0;
   jpos[3][0]=0;  jpos[3][1]=0;  jpos[3][2]=0;   jpos[3][3]=0;  jpos[3][4]=0;   jpos[3][5]=0;

   drfl.amovesj(jpos, jposNum, jvel, jacc);
   Sleep(3000);
   drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);

This asynchronously executes a **joint spline** through four waypoints and toggles a digital output 3 seconds after start.  
Use ``mwait()`` before issuing the next motion to ensure the spline has finished.
