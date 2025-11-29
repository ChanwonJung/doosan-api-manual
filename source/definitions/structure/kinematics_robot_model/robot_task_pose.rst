.. _struct_ROBOT_TASK_POSE:

ROBOT_TASK_POSE
===============

This structure defines the **target task-space pose** of the robot,  
including six position/orientation values and a corresponding **solution space index**  
used for inverse kinematics.

.. list-table::
   :widths: 15 28 18 8 31
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[NUM_TASK]``
     - Six float values
     - Target task-space pose (X, Y, Z, Rx, Ry, Rz)
   * - 24
     - ``_iTargetSol``
     - ``unsigned char``
     - 0x00~0x07
     - Inverse kinematics **solution space index**

Total size: 25 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_TASK_POSE
   {
       float          _fTargetPos[NUM_TASK];  /* target pose (X, Y, Z, Rx, Ry, Rz) */
       unsigned char  _iTargetSol;            /* solution space index: 0 ~ 7 */
   } ROBOT_TASK_POSE, *LPROBOT_TASK_POSE;