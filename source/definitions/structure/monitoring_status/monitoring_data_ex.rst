.. _struct_MONITORING_DATA_EX:

MONITORING_DATA_EX
==================

This is structure information for checking robot operation data information of the robot controller, and is composed of the following information on seven operations.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tCtrl``
     - :ref:`MONITORING_CONTROL_EX <struct_ROBOT_MONITORING_DATA_EX>`
     - -
     - Operation Info #1~#6 (State/Joint/Task/Torque/World/User)
   * - 809
     - ``_tMisc``
     - :ref:`struct_MONITORING_MISC`
     - -
     - Operation Info #7 (Other I/O: time/IO/brake/buttons/current/temp)

**Union A — Force-control payload** (shares the same 120 B)

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 903
     - ``_tMiscEx._tCtrlEx``
     - :ref:`struct_MONITORING_FORCECONTROL`
     - -
     - **Uses Union A region** when force-control is enabled.
   * - 903
     - ``_tMiscEx._szReserved1``
     - ``unsigned char[120]``
     - -
     - **Uses the same memory as above** when feature is not used (padding).

**Union B — A-Model payload** (shares the same 64 B)

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 1023
     - ``_tModel._tAModel``
     - :ref:`struct_ROBOT_MONITORING_AMODEL`
     - -
     - **Uses Union B region** when A-Model payload is provided.
   * - 1023
     - ``_tModel._szReserved``
     - ``unsigned char[64]``
     - -
     - **Same memory** as above when not used.

**Union C — Flange I/O config** (shares the same 56 B)

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 1087
     - ``_tFlangeIo._tConfig``
     - :ref:`struct_MONITORING_FLANGE_IO_CONFIG`
     - -
     - **Uses Union C region** when flange I/O config is provided.
   * - 1087
     - ``_tFlangeIo._szReserved``
     - ``unsigned char[56]``
     - -
     - **Same memory** as above when not used.

Total size: 1143 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_DATA_EX
   {
       MONITORING_CONTROL_EX  _tCtrl;   // 809 B
       MONITORING_MISC        _tMisc;   // 94 B

       union { MONITORING_FORCECONTROL       _tCtrlEx;  unsigned char _szReserved1[120]; } _tMiscEx;
       union { MONITORING_AMODEL             _tAModel;  unsigned char _szReserved[64];  } _tModel;
       union { MONITORING_FLANGE_IO_CONFIG   _tConfig;  unsigned char _szReserved[56];  } _tFlangeIo;
   } MONITORING_DATA_EX, *LPMONITORING_DATA_EX;

.. note::
   - **Union = shared memory**. In each union group (A/B/C) **only one member is valid at a time**.
   - If a feature is disabled, the corresponding union member is exposed as a **reserved byte array** of the same size.
   - This preserves packet size/offsets across firmware versions while enabling future expansion.