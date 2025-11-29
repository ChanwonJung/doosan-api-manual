.. _struct_ROBOT_MONITORING_TASK:

ROBOT_MONITORING_TASK
=====================

This structure provides real-time task-space monitoring data of the robot.  
It contains actual and target task values for tool & flange frames, task errors,  
IK solution space index, and a 3×3 rotation matrix for orientation representation.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fActualPos``
     - ``float[2][6]``
     - -
     - Position actual value (0: tool, 1: flange)
   * - 48
     - ``_fActualVel``
     - ``float[6]``
     - -
     - Actual task velocity values.
   * - 72
     - ``_fActualErr``
     - ``float[6]``
     - -
     - Task-space position/orientation error.
   * - 96
     - ``_fTargetPos``
     - ``float[6]``
     - -
     - Target position in task-space coordinates.
   * - 120
     - ``_fTargetVel``
     - ``float[6]``
     - -
     - Target velocity in task-space coordinates.
   * - 144
     - ``_iSolutionSpace``
     - ``unsigned char``
     - 0 ~ 255
     - Inverse Kinematics solution space index.
   * - 148
     - ``_fRotationMatrix``
     - ``float[3][3]``
     - -
     - Rotation matrix (3×3) representing tool orientation.

Total size: 184 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_TASK 
   {
       float         _fActualPos[2][NUMBER_OF_JOINT];  /* Position Actual Value (0: tool, 1: flange) */
       float         _fActualVel[NUMBER_OF_JOINT];     /* Velocity Actual Value */
       float         _fActualErr[NUMBER_OF_JOINT];     /* Task Error */
       float         _fTargetPos[NUMBER_OF_JOINT];     /* Target Position */
       float         _fTargetVel[NUMBER_OF_JOINT];     /* Target Velocity */
       unsigned char _iSolutionSpace;                  /* Solution Space Index */
       float         _fRotationMatrix[3][3];           /* Rotation Matrix (3x3) */
   } ROBOT_MONITORING_TASK, *LPROBOT_MONITORING_TASK;
