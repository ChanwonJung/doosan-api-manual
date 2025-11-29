.. _auto_movej:

movej (Auto Mode)
------------------------------------------

This is a function for moving the robot from the current joint location to target joint location in the robot controller.

.. figure:: /tutorials/images/mode/movej_overview.png
   :alt: movej
   :width: 80%
   :align: center

.. raw:: html
      
   <br>

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 771)

.. code-block:: cpp

   // motion control: joint move
   bool movej(float fTargetPos[NUM_JOINT],
              float fTargetVel,
              float fTargetAcc,
              float fTargetTime = 0.f,
              MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
              float fBlendingRadius = 0.f,
              BLENDING_SPEED_TYPE eBlendingType = BLENDING_SPEED_TYPE_DUPLICATE) {
       return _movej(_rbtCtrl, fTargetPos, fTargetVel, fTargetAcc,
                     fTargetTime, eMoveMode, fBlendingRadius, eBlendingType);
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
     - Target joint location for six axes
   * - fTargetVel
     - float
     - -
     - Velocity
   * - fTargetAcc
     - float
     - -
     - Acceleration
   * - fTargetTime
     - float
     - -
     - Reach Time [sec]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Enumeration Type
   * - fBlendingRadius
     - float
     - -
     - Radius for blending
   * - eBlendingType
     - :ref:`BLENDING_SPEED_TYPE <enum_blending_speed_type>` 
     - ``BLENDING_SPEED_TYPE_DUPLICATE``
     - Refer to the Definition of Enumeration Type

.. Note::

  - When ``fTargetTime`` is specified, ``fTargetVel`` and ``fTargetAcc`` are ignored, and the process is done based on ``fTargetTime``.

    .. figure:: /tutorials/images/mode/movej_overview2.png
      :alt: movej_overview2
      :width: 80%
      :align: center

    .. raw:: html
          
      <br>

.. Caution::

  If the following motion is blended with the conditions of ``eBlendingType`` being 
  ``BLENDING_SPEED_TYPE_DUPLICATE`` and ``fBlendingRadius > 0``, the preceding motion can 
  be terminated **after the following motion** is terminated first when the remaining 
  motion time (determined by remaining distance, velocity, and acceleration of the 
  preceding motion) is greater than the motion time of the following motion. 

      .. figure:: /tutorials/images/mode/movej_caution.png
        :alt: movej_caution
        :width: 80%
        :align: center

      .. raw:: html
            
        <br>

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

   // CASE 1
   float q0[6] = { 0, 0, 90, 0, 90, 0 };
   float jVel = 10;
   float jAcc = 20;
   drfl.movej(q0, jVel, jAcc);
   // Moves to the q0 joint angle with velocity 10(deg/sec) and acceleration 20(deg/sec2)

   // CASE 2
   float q0r[6] = { 0, 0, 90, 0, 90, 0 };
   float jTime = 5;
   drfl.movej(q0r, 0, 0, jTime);
   // Moves to the q0 joint angle with a reach time of 5 sec.

   // CASE 3
   float q0b[6] = { 0, 0, 90, 0, 90, 0 };
   float q1b[6] = { 90, 0, 90, 0, 90, 0 };
   float jVelb = 10;
   float jAccb = 20;
   float blending_radius = 50;
   drfl.movej(q0b, jVelb, jAccb, 0, MOVE_MODE_ABSOLUTE, blending_radius);
   // Moves to the q0 joint angle and is set to execute the next motion
   // when the distance from the location that corresponds to the q0 joint angle is 50 mm.
   drfl.movej(q1b, jVelb, jAccb, 0, MOVE_MODE_ABSOLUTE, 0, BLENDING_SPEED_TYPE_DUPLICATE);
   // Blends with the last motion to move to the q1 joint angle.

This example shows time-based and speed/acceleration-based **joint motions**, and a two-segment sequence using **blending radius** and **DUPLICATE** blending to smoothly connect moves.
