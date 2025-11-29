.. _enum_servo_mode:

SERVO_MODE
------------------------------------------
It is an enumerated constant that indicates the servo operation mode of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SMODE_SERVO_OFF
     - Servo Off mode

   * - 1
     - SMODE_SERVO_ON
     - Servo On mode

   * - 2
     - SMODE_HOLD
     - Hold mode

   * - 3
     - SMODE_POSITION_MODE
     - Position control mode

   * - 4
     - SMODE_TORQUE_MODE
     - Torque control mode

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum    
   {
       SMODE_SERVO_OFF = 0,
       SMODE_SERVO_ON,
       SMODE_HOLD, 
       SMODE_POSITION_MODE,
       SMODE_TORQUE_MODE,
   } SERVO_MODE;
