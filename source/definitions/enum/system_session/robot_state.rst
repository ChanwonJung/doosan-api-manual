.. _enum_robot_state:

ROBOT_STATE
------------------------------------------

This is an enumeration type constant that refers to the operation status of 
robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 20 85

   * - Rank
     - Constant Name
     - Description

   * - 0
     - STATE_INITIALIZING
     - This is a state of automatic entrance of T/P application, and is |br|
       an initialization condition for the setting of various parameters.

   * - 1
     - STATE_STANDBY
     - This is an operable basis state, and is a command standby state.

   * - 2
     - STATE_MOVING
     - A command operation state that is automatically converted while |br|
       the robot is moving after the receipt of commands. |br|
       Once moving is done, the state is automatically converted |br|
       into a command standby state.

   * - 3
     - STATE_SAFE_OFF
     - This is a robot pause mode caused by functional and operational |br|
       error, and is a servo off state (a state in which motor and brake |br|
       power is cut off after control pause).

   * - 4
     - STATE_TEACHING
     - Direct teaching state.

   * - 5
     - STATE_SAFE_STOP
     - This is a robot pause mode caused by functional and operational |br| 
       error, and is a safety stop state (a state in which only control |br|
       pause was executed, and a temporary program pause state in the |br|
       case of automatic mode).

   * - 6
     - STATE_EMERGENCY_STOP
     - Emergency stop state.

   * - 7
     - STATE_HOMMING
     - Homing Mode state (hardware-based array state of robot).

   * - 8
     - STATE_RECOVERY
     - Recovery mode state for moving robot into the operation range |br| 
       when that robot has stopped due to errors such as getting out of |br|
       robot operation range.

   * - 9
     - STATE_SAFE_STOP2
     - A state in which conversion into recovery mode is needed due to |br| 
       getting out of robot operation range, although it is the same as |br|
       the STATE_SAFE_STOP state.

   * - 10
     - STATE_SAFE_OFF2
     - A state in which conversion into recovery mode is needed due to |br|
       getting out of robot operation range, although it is the same as |br| 
       the STATE_SAFE_OFF state.

   * - 11
     - STATE_RESERVED1
     - Reservation used.

   * - 12
     - STATE_RESERVED2
     - Reservation used.

   * - 13
     - STATE_RESERVED3
     - Reservation used.

   * - 14
     - STATE_RESERVED4
     - Reservation used.

   * - 15
     - STATE_NOT_READY
     - State for initialization after boot-up of robot controller. |br| 
       It is converted into the initialization state by the T/P application.

   * - 16
     - STATE_LAST
     - Indicates the **final enumerator marker** used internally by the API. |br| 
       It does not represent an operational state of the robot, but simply |br| 
       defines the **total number of valid states** in this enumeration. |br| 
       (Used for boundary checking and array size definitions.)

**Defined in:** ``DRFC.h``  

  .. code-block:: cpp

      // robot state enumerated value
      typedef enum {
          STATE_INITIALIZING,
          STATE_STANDBY,
          STATE_MOVING,
          STATE_SAFE_OFF,
          STATE_TEACHING,
          STATE_SAFE_STOP,
          STATE_EMERGENCY_STOP,
          STATE_HOMMING,
          STATE_RECOVERY,
          STATE_SAFE_STOP2,
          STATE_SAFE_OFF2,
          STATE_RESERVED1,
          STATE_RESERVED2,
          STATE_RESERVED3,
          STATE_RESERVED4,
          STATE_NOT_READY = 15,
          STATE_LAST,
      } ROBOT_STATE;