.. _struct_ROBOT_MONITORING_DATA:
.. _struct_MONITORING_CONTROL:

ROBOT_MONITORING_DATA
=====================

This structure aggregates monitoring sections (state, joint, task, torque) into one packet.

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
     - Torque and External Force Information
   * - 423
     - Other Robot-related Input Information
     - **see table below**
     - -
     - Internal supplemental data

Total size: 519 bytes

Other Robot-related Input Information is composed of other robot-related input/output information as follows.  
(Reference-only; not part of the public SDK structure.)

.. list-table::
   :widths: 10 28 15 10 37
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - Time Information
     - ``double``
     - -
     - Internal clock counter
   * - 8
     - I/O Information (#1)
     - ``unsigned char[6]``
     - -
     - Six digital **inputs** (edge)
   * - 14
     - I/O Information (#2)
     - ``unsigned char[6]``
     - -
     - Six digital **outputs** (edge)
   * - 20
     - Brake Information
     - ``unsigned char[6]``
     - -
     - Six brake states (0: released, 1: locked)
   * - 26
     - Button Information
     - ``unsigned int[5]``
     - -
     - Five robot buttons on/off
   * - 46
     - Current Information
     - ``float[6]``
     - -
     - Six motors' current consumption
   * - 70
     - Temperature Information
     - ``float[6]``
     - -
     - Six inverters temperature
   * - 94
     - Reserved (padding)
     - ``unsigned char[2]``
     - -
     - Padding to align the block size to **96 B**

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_DATA
   {
       ROBOT_MONITORING_STATE   _tState;    /* 2 bytes */
       ROBOT_MONITORING_JOINT   _tJoint;    /* 144 bytes */
       ROBOT_MONITORING_TASK    _tTask;     /* 181 bytes (packed layout as per controller manual) */
       ROBOT_MONITORING_TORQUE  _tTorque;   /* 96 bytes */
   } MONITORING_CONTROL, *LPMONITORING_CONTROL;
