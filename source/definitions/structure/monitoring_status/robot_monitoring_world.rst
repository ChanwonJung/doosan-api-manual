.. _struct_ROBOT_MONITORING_WORLD:

ROBOT_MONITORING_WORLD
======================

This structure provides real-time monitoring data of the robot  
in the **world coordinate system**. It includes world-to-base transformation,  
task-space position/velocity, external force/torque, and orientation matrix.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fActualW2B``
     - ``float[6]``
     - -
     - World-to-Base transformation vector (X, Y, Z, Rx, Ry, Rz).
   * - 24
     - ``_fActualPos``
     - ``float[2][6]``
     - -
     - Position actual value (0: tool frame, 1: flange frame).
   * - 72
     - ``_fActualVel``
     - ``float[6]``
     - -
     - Actual velocity in the world coordinate system.
   * - 96
     - ``_fActualETT``
     - ``float[6]``
     - -
     - External task force/torque (Fx, Fy, Fz, Tx, Ty, Tz).
   * - 120
     - ``_fTargetPos``
     - ``float[6]``
     - -
     - Target task-space position in world coordinates.
   * - 144
     - ``_fTargetVel``
     - ``float[6]``
     - -
     - Target task-space velocity in world coordinates.
   * - 168
     - ``_fRotationMatrix``
     - ``float[3][3]``
     - -
     - 3x3 rotation matrix representing tool orientation relative to world frame.

Total size: 204 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_WORLD
   {
       float _fActualW2B[NUMBER_OF_JOINT];       /* World to Base Relation */
       float _fActualPos[2][NUMBER_OF_JOINT];    /* Position Actual Value (0:tool, 1:flange) */
       float _fActualVel[NUMBER_OF_JOINT];       /* Velocity Actual Value */
       float _fActualETT[NUMBER_OF_JOINT];       /* External Task Force/Torque */
       float _fTargetPos[NUMBER_OF_JOINT];       /* Target Position */
       float _fTargetVel[NUMBER_OF_JOINT];       /* Target Velocity */
       float _fRotationMatrix[3][3];             /* Rotation Matrix */
   } ROBOT_MONITORING_WORLD, *LPROBOT_MONITORING_WORLD;
