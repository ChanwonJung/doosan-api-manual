.. _struct_ROBOT_MONITORING_JOINT:

ROBOT_MONITORING_JOINT
======================

This structure provides real-time joint monitoring data of the robot.  
Each field contains an array of values corresponding to each joint (``NUM_JOINT`` = 6).

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
     - ``float[6]``
     - -
     - Position actual value in INC units.
   * - 24
     - ``_fActualAbs``
     - ``float[6]``
     - -
     - Position actual value in ABS units.
   * - 48
     - ``_fActualVel``
     - ``float[6]``
     - -
     - Actual velocity of each joint.
   * - 72
     - ``_fActualErr``
     - ``float[6]``
     - -
     - Position error of each joint.
   * - 96
     - ``_fTargetPos``
     - ``float[6]``
     - -
     - Target position command value.
   * - 120
     - ``_fTargetVel``
     - ``float[6]``
     - -
     - Target velocity command value.

Total size: 144 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_JOINT 
   {
       float _fActualPos[NUM_JOINT];  /* Position Actual Value in INC */
       float _fActualAbs[NUM_JOINT];  /* Position Actual Value in ABS */
       float _fActualVel[NUM_JOINT];  /* Velocity Actual Value */
       float _fActualErr[NUM_JOINT];  /* Joint Error */
       float _fTargetPos[NUM_JOINT];  /* Target Position */
       float _fTargetVel[NUM_JOINT];  /* Target Velocity */
   } ROBOT_MONITORING_JOINT, *LPROBOT_MONITORING_JOINT;
