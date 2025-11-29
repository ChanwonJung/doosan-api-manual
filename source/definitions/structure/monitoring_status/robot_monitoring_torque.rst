.. _struct_ROBOT_MONITORING_TORQUE:

ROBOT_MONITORING_TORQUE
=======================

This structure provides real-time torque-related monitoring data of each robot joint,  
including dynamic torque, torque sensor readings, and external torque/force values.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fDynamicTor``
     - ``float[6]``
     - -
     - Dynamic torque values calculated from robot dynamics.
   * - 24
     - ``_fActualJTS``
     - ``float[6]``
     - -
     - Actual joint torque sensor readings.
   * - 48
     - ``_fActualEJT``
     - ``float[6]``
     - -
     - External joint torque values (filtered).
   * - 72
     - ``_fActualETT``
     - ``float[6]``
     - -
     - External task-space force/torque (Fx, Fy, Fz, Tx, Ty, Tz).

Total size: 96 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_TORQUE 
   {
       float _fDynamicTor[NUM_JOINT];   /* Dynamics Torque */
       float _fActualJTS[NUM_JOINT];    /* Joint Torque Sensor Value */
       float _fActualEJT[NUM_JOINT];    /* External Joint Torque */
       float _fActualETT[NUM_JOINT];    /* External Task Force/Torque */
   } ROBOT_MONITORING_TORQUE, *LPROBOT_MONITORING_TORQUE;
