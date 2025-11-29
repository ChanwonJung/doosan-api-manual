.. _struct_ROBOT_MONITORING_DATA_EX:

ROBOT_MONITORING_DATA_EX
========================

This structure aggregates extended monitoring sections (state, joint, task, torque, world, user) into one packet.  
It excludes controller-internal “Other” blocks and reserved areas.

.. list-table::
   :widths: 10 28 15 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tState``
     - :ref:`ROBOT_MONITORING_STATE <struct_ROBOT_MONITORING_STATE>`
     - -
     - Control-related Information
   * - 2
     - ``_tJoint``
     - :ref:`ROBOT_MONITORING_JOINT <struct_ROBOT_MONITORING_JOINT>`
     - -
     - Joint Space Information
   * - 146
     - ``_tTask``
     - :ref:`ROBOT_MONITORING_TASK <struct_ROBOT_MONITORING_TASK>`
     - -
     - Task Space Information
   * - 327
     - ``_tTorque``
     - :ref:`ROBOT_MONITORING_TORQUE <struct_ROBOT_MONITORING_TORQUE>`
     - -
     - Torque & External Force Information
   * - 423
     - ``_tWorld``
     - :ref:`ROBOT_MONITORING_WORLD <struct_ROBOT_MONITORING_WORLD>`
     - -
     - World Space Information
   * - 627
     - ``_tUser``
     - :ref:`ROBOT_MONITORING_USER <struct_ROBOT_MONITORING_USER>`
     - -
     - User Space Information

Total size: 809 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_DATA_EX
   {
       ROBOT_MONITORING_STATE      _tState;   /* 2 bytes   */
       /* joint */
       ROBOT_MONITORING_JOINT      _tJoint;   /* 144 bytes */
       /* task */
       ROBOT_MONITORING_TASK       _tTask;    /* 181 bytes */
       /* torque */
       ROBOT_MONITORING_TORQUE     _tTorque;  /* 96 bytes  */
       /* world */
       ROBOT_MONITORING_WORLD      _tWorld;   /* 204 bytes */
       /* user */
       ROBOT_MONITORING_USER       _tUser;    /* 182 bytes */
   } ROBOT_MONITORING_DATA_EX, *LPROBOT_MONITORING_DATA_EX;

   typedef ROBOT_MONITORING_DATA_EX
       MONITORING_CONTROL_EX, *LPMONITORING_CONTROL_EX;
