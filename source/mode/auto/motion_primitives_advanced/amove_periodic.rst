.. _auto_amove_periodic:

amove_periodic (Auto Mode)
------------------------------------------

As an asynchronous ``move_periodic()``, this function operates the same way as ``move_periodic()``  
except that it executes the next line immediately after the motion starts, without waiting for termination.  
A new motion command generated before the previous one ends must be separated by ``mwait()`` for safety.

This command performs a **cyclic motion** based on the **sine function** of each axis (parallel or rotation)  
in the specified reference coordinate (``eMoveReference``).  
The attributes of the motion (amplitude, period, acceleration/deceleration time, and total repetitions)  
are defined by the respective input parameters.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 809)

.. code-block:: cpp

   bool amove_periodic(float fAmplitude[NUM_TASK],
                       float fPeriodic[NUM_TASK],
                       float fAccelTime,
                       unsigned int nRepeat,
                       MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_TOOL) {
       return _amove_periodic(_rbtCtrl, fAmplitude, fPeriodic, fAccelTime, nRepeat, eMoveReference);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Range**
     - **Description**
   * - fAmplitude
     - float[6]
     - -
     - ≥ 0
     - Amplitude (motion between -fAmplitude and +fAmplitude) [mm] or [deg]
   * - fPeriodic
     - float[6]
     - -
     - ≥ 0
     - Period (time for one cycle) [sec]
   * - fAccelTime
     - float
     - -
     - ≥ 0
     - Acceleration/Deceleration time [sec]
   * - nRepeat
     - unsigned char
     - -
     - > 0
     - Repetition count
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>`
     - ``MOVE_REFERENCE_TOOL``
     - -
     - Refer to the Definition of Enumeration Type

.. Note::

  - ``fAmplitude`` defines the amplitude for each axis (x, y, z, rx, ry, rz).  
    Axes with no periodic motion must have an amplitude of ``0``.
  - ``fPeriodic`` defines the time to complete one full motion cycle for each axis.  
    Each value corresponds to the same order as the axes (x, y, z, rx, ry, rz).
  - ``fAccelTime`` specifies the acceleration/deceleration time at both the beginning and end of the periodic motion.  
    The maximum of (``period * 1/4``) is applied. Errors occur if acceleration/deceleration time exceeds ½ of the total motion time.
  - ``nRepeat`` determines how many full cycles are repeated.  
    The axis with the largest period determines total motion time.
  - If the motion ends normally, the remaining axes may stop before the reference axis terminates to maintain return to the start position.  
    If not, the deceleration path may slightly deviate.
  - ``eMoveReference`` specifies whether the periodic motion is executed in **TOOL** or **BASE** coordinates.
  - To adjust excessive velocity, use:  
    ``velocity = Amplitude(fAmplitude) * 2 * π(3.14) / Period(fPeriodic)`` |br|
    *e.g., Max velocity = 62.83 mm/s if amp=10 mm, period=1 s*
  - This function **does not support online blending** between previous and next motions.

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

   // Repeats the X-axis (10 mm amplitude, 1 sec period) motion and
   // Y-axis rotation (0.5 deg amplitude, 1 sec period), repeated 5 times.
   // Sets the Digital Output channel 1 after 1 second.
   float fAmplitude[NUM_TASK] = {10, 0, 0, 0, 0.5, 0};
   float fPeriod[NUM_TASK] = {1, 1, 1, 1, 1, 1};
   drfl.amove_periodic(fAmplitude, fPeriod, 0.5, 5, MOVE_REFERENCE_TOOL);
   Sleep(1000);
   drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);
   drfl.mwait();

This example generates a **sinusoidal periodic motion** on X and rotation-Y axes within the TOOL coordinate frame.  
After 1 second, Digital Output 1 is triggered while the robot continues its periodic trajectory.
