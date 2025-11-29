.. _struct_ROBOT_ALALOG_WELDING_DATA:
.. _struct_MONITORING_ALALOG_WELDING:

ROBOT_ALALOG_WELDING_DATA
=========================

Extended analog-welding telemetry including **blow-out state** and **feeding velocity**.

.. list-table::
   :widths: 12 30 20 8 30
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iAdjAvail``
     - ``unsigned char``
     - 0~1
     - Adjustment available flag
   * - 4
     - ``_fTargetVol``
     - ``float``
     - V
     - Target voltage
   * - 8
     - ``_fTargetCur``
     - ``float``
     - A
     - Target current
   * - 12
     - ``_fTargetVel``
     - ``float``
     - mm/s
     - Target welding speed
   * - 16
     - ``_fActualVol``
     - ``float``
     - V
     - Actual voltage
   * - 20
     - ``_fActualCur``
     - ``float``
     - A
     - Actual current
   * - 24
     - ``_fOffsetY``
     - ``float``
     - mm
     - Weaving offset Y
   * - 28
     - ``_fOffsetZ``
     - ``float``
     - mm
     - Weaving offset Z
   * - 32
     - ``_iArcOnDO``
     - ``unsigned char``
     - 0~1
     - Arc ON DO
   * - 33
     - ``_iGasOnDO``
     - ``unsigned char``
     - 0~1
     - Gas ON DO
   * - 34
     - ``_iInchPDO``
     - ``unsigned char``
     - 0~1
     - Inching plus DO
   * - 35
     - ``_iInchNPO``
     - ``unsigned char``
     - 0~1
     - Inching minus DO
   * - 36
     - ``_iStatus``
     - ``unsigned char``
     - 0~1
     - Welding status
   * - 37
     - ``_iBlowOut``
     - ``unsigned char``
     - 0~1
     - Blow-out flag
   * - 40
     - ``_iFeedingVel``
     - ``float``
     - mm/s
     - Wire feeding velocity

Total size: 44 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_ALALOG_WELDING_DATA
   {
       unsigned char _iAdjAvail;
       float _fTargetVol;
       float _fTargetCur;
       float _fTargetVel;
       float _fActualVol;
       float _fActualCur;
       float _fOffsetY;
       float _fOffsetZ;
       unsigned char _iArcOnDO;
       unsigned char _iGasOnDO;
       unsigned char _iInchPDO;
       unsigned char _iInchNPO;
       unsigned char _iStatus;
       unsigned char _iBlowOut;
       float _iFeedingVel;
   } ROBOT_ALALOG_WELDING_DATA, *LPROBOT_ALALOG_WELDING_DATA;

.. code-block:: cpp

   /* Alias used for streaming/monitoring */
   typedef ROBOT_ALALOG_WELDING_DATA
       MONITORING_ALALOG_WELDING, *LPMONITORING_ALALOG_WELDING;