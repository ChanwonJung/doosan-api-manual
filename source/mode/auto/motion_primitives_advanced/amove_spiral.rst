.. _auto_amove_spiral:

amove_spiral (Auto Mode)
------------------------------------------

As an asynchronous version of :ref:`move_spiral <auto_move_spiral>`,  
this function initiates the spiral motion and immediately returns without waiting for completion.  
It allows other program lines to execute while the spiral motion continues in the background.  
Since a new motion command issued before ``amove_spiral()`` terminates may cause an error,  
it is recommended to use ``mwait()`` between motions for safe sequencing.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 805)

.. code-block:: cpp

   bool amove_spiral(TASK_AXIS eTaskAxis,
                     float fRevolution,
                     float fMaximuRadius,
                     float fMaximumLength,
                     float fTargetVel[2],
                     float fTargetAcc[2],
                     float fTargetTime = 0.f,
                     MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_TOOL) {
       return _amove_spiral(_rbtCtrl, eTaskAxis, fRevolution, fMaximuRadius,
                            fMaximumLength, fTargetVel, fTargetAcc,
                            fTargetTime, eMoveReference);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eTaskAxis
     - :ref:`TASK_AXIS <enum_task_axis>`  
     - -
     - Axis perpendicular to the spiral surface  
       (defines the rotation plane of the spiral)
   * - fRevolution
     - float
     - -
     - Total number of spiral turns [revolutions]
   * - fMaximuRadius
     - float
     - -
     - Final spiral radius [mm]
   * - fMaximumLength
     - float
     - -
     - Distance moved along the axis direction [mm]  
       (negative = opposite direction)
   * - fTargetVel
     - float[2]
     - -
     - Linear velocity and angular velocity [mm/s, deg/s]
   * - fTargetAcc
     - float[2]
     - -
     - Linear acceleration and angular acceleration [mm/s², deg/s²]
   * - fTargetTime
     - float
     - 0.0
     - Total motion execution time [sec]
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - ``MOVE_REFERENCE_TOOL``
     - Coordinate frame reference for the spiral motion (BASE / TOOL)

.. Note::

  - ``fRevolution`` defines the number of turns for the spiral path.  
  - ``fMaximuRadius`` specifies the outermost radius reached during motion.  
  - ``fMaximumLength`` represents the travel distance along the spiral axis.  
  - ``fTargetVel`` and ``fTargetAcc`` define the linear/angular motion profile.  
  - When ``fTargetTime`` is set, the spiral follows time-based control,  
    ignoring both ``fTargetVel`` and ``fTargetAcc``.  
  - ``eTaskAxis`` determines which plane the spiral expands in (e.g., XY for Z-axis selection).  
  - ``eMoveReference`` determines whether motion is relative to the **BASE** or **TOOL** frame.  
  - The motion termination must be confirmed using ``mwait()`` before executing the next command.  
  - Online blending with other motions is **not supported**.

.. Caution::

  - If the spiral’s computed angular acceleration exceeds the safe threshold,  
    a safety error will be triggered.  
    To prevent this, reduce ``fTargetVel``, ``fTargetAcc``, or ``fTargetTime``.

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

   // Trigger D-Out signal 3 seconds after the spiral motion begins
   float rev = 3;      // Revolutions
   float rmax = 30;    // Maximum radius [mm]
   float lmax = 50;    // Length along Z-axis [mm]
   float tvel[2] = {50, 50};
   float tacc[2] = {100, 100};

   drfl.amove_spiral(TASK_AXIS_Z, rev, rmax, lmax, tvel, tacc);
   Sleep(3000);
   drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);

This example performs an **asynchronous spiral motion** along the Z-axis (in TOOL frame),  
gradually expanding the spiral radius up to 30 mm while ascending 50 mm.  
The digital output activates 3 seconds after the motion starts,  
and subsequent commands should wait for completion using ``mwait()``.
