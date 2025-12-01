.. _struct_ROBOT_MONITORING_USER:

ROBOT_MONITORING_USER
=====================

This structure provides real-time monitoring data of the robot  
in the **user coordinate system**. It includes the active user coordinate number,  
its parent frame, task-space values (position, velocity, force/torque),  
and the 3×3 orientation rotation matrix.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualUCN``
     - ``unsigned char``
     - 0 ~ 255
     - Actual user coordinate number.
   * - 1
     - ``_iParent``
     - ``unsigned char``
     - 0 or 2
     - Parent frame |br| 
       (0: Base frame, 2: World frame)
   * - 2
     - ``_fActualPos``
     - ``float[2][6]``
     - -
     - Position actual values |br|
       (0: tool frame, 1: flange frame)
   * - 50
     - ``_fActualVel``
     - ``float[6]``
     - -
     - Actual velocity values in user coordinates.
   * - 74
     - ``_fActualETT``
     - ``float[6]``
     - -
     - External task force/torque (Fx, Fy, Fz, Tx, Ty, Tz).
   * - 98
     - ``_fTargetPos``
     - ``float[6]``
     - -
     - Target position in user coordinate frame.
   * - 122
     - ``_fTargetVel``
     - ``float[6]``
     - -
     - Target velocity in user coordinate frame.
   * - 146
     - ``_fRotationMatrix``
     - ``float[3][3]``
     - -
     - 3x3 rotation matrix representing orientation of the tool in user coordinates.

Total size: 182 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_USER
   {
       unsigned char _iActualUCN;                     /* actual user coord no */
       unsigned char _iParent;                        /* base:0, world:2 */
       float         _fActualPos[2][NUMBER_OF_JOINT]; /* Position Actual (0:tool,1:flange) */
       float         _fActualVel[NUMBER_OF_JOINT];    /* Velocity Actual */
       float         _fActualETT[NUMBER_OF_JOINT];    /* External Task Force/Torque */
       float         _fTargetPos[NUMBER_OF_JOINT];    /* Target Position */
       float         _fTargetVel[NUMBER_OF_JOINT];    /* Target Velocity */
       float         _fRotationMatrix[3][3];          /* Rotation Matrix */
   } ROBOT_MONITORING_USER, *LPROBOT_MONITORING_USER;
