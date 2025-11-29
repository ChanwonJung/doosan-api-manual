.. _enum_robot_mode:

ROBOT_MODE
------------------------------------------
This is an enumeration type constant that refers to the operation mode of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - ROBOT_MODE_MANUAL
     - Manual mode for direct teaching or jog control of the robot.

   * - 1
     - ROBOT_MODE_AUTONOMOUS
     - Autonomous (automatic) mode for executing programmed motions.

   * - 2
     - ROBOT_MODE_RECOVERY
     - Recovery mode used to restore the robot from an error or safety stop condition.

   * - 3
     - ROBOT_MODE_BACKDRIVE
     - Backdrive mode that allows manual movement of robot joints without servo power.

   * - 4
     - ROBOT_MODE_MEASURE
     - Measurement mode for verifying or calibrating robot positions and torques.

   * - 5
     - ROBOT_MODE_INITIALIZE
     - Initialization mode for system setup and pre-operation configuration.

   * - 6
     - ROBOT_MODE_LAST
     - Internal end marker of the ROBOT_MODE enumeration. |br|
       It does **not represent an actual operation mode**, but defines |br| 
       the total number of valid mode constants within this enumeration.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       ROBOT_MODE_MANUAL,
       ROBOT_MODE_AUTONOMOUS,
       ROBOT_MODE_RECOVERY,
       ROBOT_MODE_BACKDRIVE,
       ROBOT_MODE_MEASURE,
       ROBOT_MODE_INITIALIZE,
       ROBOT_MODE_LAST,
   } ROBOT_MODE;