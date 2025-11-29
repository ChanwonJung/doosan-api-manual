.. _enum_robot_control:

ROBOT_CONTROL
------------------------------------------

This is an enumeration type constant that can convert or change the operation status of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 20 75

   * - Rank
     - Constant Name
     - Description

   * - 0
     - CONTROL_INIT_CONFIG
     - It executes the function to convert from |br|
       STATE_NOT_READY to STATE_INITIALIZING, and only the |br|
       T/P application executes this function.

   * - 1
     - CONTROL_ENABLE_OPERATION
     - It executes the function to convert from |br|
       STATE_INITIALIZING to STATE_STANDBY, and only the |br|
       T/P application executes this function.

   * - 2
     - CONTROL_RESET_SAFET_STOP
     - It executes the function to convert from |br|
       STATE_SAFE_STOP to STATE_STANDBY. Program restart |br|
       can be set in the case of automatic mode.

   * - 3
     - CONTROL_RESET_SAFE_STOP
     - It executes the function to convert from |br|
       STATE_SAFE_STOP to STATE_STANDBY. Program restart |br|
       can be set in the case of automatic mode. |br|
       (Alias of CONTROL_RESET_SAFET_STOP)

   * - 4
     - CONTROL_RESET_SAFET_OFF
     - It executes the function to convert from STATE_SAFE_OFF |br|
       to STATE_STANDBY.

   * - 5
     - CONTROL_RESET_SAFE_OFF
     - It executes the function to convert from STATE_SAFE_OFF |br|
       to STATE_STANDBY. |br|
       (Alias of CONTROL_RESET_SAFET_OFF)

   * - 6
     - CONTROL_SERVO_ON
     - Alias of CONTROL_RESET_SAFET_OFF. |br|
       Used internally for backward compatibility with servo-on |br|
       control in earlier firmware.

   * - 7
     - CONTROL_RECOVERY_SAFE_STOP
     - It executes the S/W-based function to convert from |br|
       STATE_SAFE_STOP2 to STATE_RECOVERY.

   * - 8
     - CONTROL_RECOVERY_SAFE_OFF
     - It executes the S/W-based function to convert from |br|
       STATE_SAFE_OFF2 to STATE_RECOVERY.

   * - 9
     - CONTROL_RECOVERY_BACKDRIVE
     - It executes the H/W-based function to convert from |br|
       STATE_SAFE_OFF2 to STATE_RECOVERY. It cannot be |br|
       converted into STATE_STANDBY, and robot controller |br|
       power should be rebooted.

   * - 10
     - CONTROL_RESET_RECOVERY
     - It executes the function to convert from STATE_RECOVERY |br|
       to STATE_STANDBY.

   * - 11
     - CONTROL_LAST
     - Internal end marker of the ROBOT_CONTROL enumeration. |br|
       It does **not represent an actual control command**, but defines |br| 
       the total number of valid constants within this enumeration. |br| 
       Used internally for array size definition and boundary checking.


**Defined in:** ``DRFC.h``  

.. code-block:: cpp

    // robot control enumerated value
    typedef enum {
        CONTROL_INIT_CONFIG,
        CONTROL_ENABLE_OPERATION,
        CONTROL_RESET_SAFET_STOP,
        CONTROL_RESET_SAFE_STOP = CONTROL_RESET_SAFET_STOP,
        CONTROL_RESET_SAFET_OFF,
        CONTROL_RESET_SAFE_OFF = CONTROL_RESET_SAFET_OFF,
        CONTROL_SERVO_ON = CONTROL_RESET_SAFET_OFF,
        CONTROL_RECOVERY_SAFE_STOP,
        CONTROL_RECOVERY_SAFE_OFF,
        CONTROL_RECOVERY_BACKDRIVE,
        CONTROL_RESET_RECOVERY,
        CONTROL_LAST
    } ROBOT_CONTROL;
