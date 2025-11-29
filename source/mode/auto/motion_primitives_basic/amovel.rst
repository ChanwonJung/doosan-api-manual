.. _auto_amovel:

amovel (Auto Mode)
------------------------------------------

As an asynchronous **movel**, it operates the same as the :ref:`movel <auto_movel>` function except for not having the
``fBlendingRadius`` argument for blending. However, the command **returns immediately** when motion starts and executes
the next line **without waiting** for the termination of motion due to the asynchronous type.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 777)

.. code-block:: cpp

   bool amovel(float fTargetPos[NUM_TASK],
               float fTargetVel[2],
               float fTargetAcc[2],
               float fTargetTime = 0.f,
               MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
               MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
               BLENDING_SPEED_TYPE eBlendingType = BLENDING_SPEED_TYPE_DUPLICATE,
               DR_MV_APP eAppType = DR_MV_APP_NONE) {
       return _amovel(_rbtCtrl, fTargetPos, fTargetVel, fTargetAcc,
                      fTargetTime, eMoveMode, eMoveReference, eBlendingType, eAppType);
   }

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
     - Target TCP Position for six axes
   * - fTargetVel
     - float[2]
     - -
     - Linear Velocity, Angular Velocity
   * - fTargetAcc
     - float[2]
     - -
     - Linear Acceleration, Angular Acceleration
   * - fTargetTime
     - float
     - -
     - Reach Time [sec] |br|
       * If the time is specified, values are processed based on time, ignoring vel and acc.
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Enumeration Type
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - ``MOVE_REFERENCE_BASE``
     - Refer to the Definition of Enumeration Type
   * - eBlendingType
     - :ref:`BLENDING_SPEED_TYPE <enum_blending_speed_type>` 
     - ``BLENDING_SPEED_TYPE_DUPLICATE``
     - Refer to the Definition of Enumeration Type

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

   // D-out 2 seconds after the motion starts with x1
   float x1[6]  = { 559, 434.5, 651.5, 0, 180, 0 };
   float tvel[2] = { 50, 50 };
   float tacc[2] = { 100, 100 };
   drfl.amovel(x1, tvel, tacc);
   Sleep(2000);
   drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);

This example starts an **asynchronous linear TCP motion** to pose `x1`, then toggles a digital output 2 seconds after motion start.
Because it’s asynchronous, program flow continues immediately after `amovel()` is issued.
