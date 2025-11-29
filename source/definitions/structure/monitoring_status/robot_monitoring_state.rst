.. _struct_ROBOT_MONITORING_STATE:

ROBOT_MONITORING_STATE
======================

This structure provides information on the robot’s **current control mode** and **control space**.  
It indicates whether the robot operates in position or torque control, and in joint or task space.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualMode``
     - ``unsigned char``
     - 0 ~ 1
     - **Actual Control Mode** |br| 0: Position Control |br| 1: Torque Control
   * - 1
     - ``_iActualSpace``
     - ``unsigned char``
     - 1 ~ 2
     - **Actual Control Space** |br| 1: Joint Space |br| 2: Task Space

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_STATE 
   {
       unsigned char _iActualMode;   /* position control: 0, torque control: 1 */
       unsigned char _iActualSpace;  /* joint space: 1, task space: 2 */
   } ROBOT_MONITORING_STATE, *LPROBOT_MONITORING_STATE;
