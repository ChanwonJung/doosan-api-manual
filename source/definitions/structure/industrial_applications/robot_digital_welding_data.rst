.. _struct_ROBOT_DIGITAL_WELDING_DATA:
.. _struct_MONITORING_DIGITAL_WELDING:

ROBOT_DIGITAL_WELDING_DATA
==========================

Digital welding telemetry including targets/actuals, weaving offsets, rich status, and diagnostics.
``MONITORING_DIGITAL_WELDING`` is a typedef alias of this structure.

.. list-table::
   :widths: 10 30 18 8 34
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
     - Arc ON DO state
   * - 33
     - ``_iGasOnDO``
     - ``unsigned char``
     - 0~1
     - Gas ON DO state
   * - 34
     - ``_iInchPDO``
     - ``unsigned char``
     - 0~1
     - Inching plus DO state
   * - 35
     - ``_iInchNPO``
     - ``unsigned char``
     - 0~1
     - Inching minus DO state
   * - 36
     - ``_iStatus``
     - ``unsigned char``
     - 0~1
     - Welding status (e.g., Start/Finish)
   * - 37
     - ``_iBlowOut``
     - ``unsigned char``
     - 0~1
     - Blow-out flag
   * - 40
     - ``_fFeedingVel``
     - ``float``
     - mm/s
     - Commanded wire feeding velocity
   * - 44
     - ``_fActualFeedingVel``
     - ``float``
     - mm/s
     - Measured wire feeding velocity
   * - 48
     - ``_iErrorNumber``
     - ``int``
     - -
     - Error number (vendor-specific)
   * - 52
     - ``_fWireStick``
     - ``float``
     - -
     - Wire stick value
   * - 56
     - ``_iError``
     - ``int``
     - -
     - Error code (bitmask or code)
   * - 60
     - ``_fOption1``
     - ``float``
     - -
     - Optional telemetry #1
   * - 64
     - ``_fOption2``
     - ``float``
     - -
     - Optional telemetry #2
   * - 68
     - ``_fOption3``
     - ``float``
     - -
     - Optional telemetry #3
   * - 72
     - ``_fOption4``
     - ``float``
     - -
     - Optional telemetry #4
   * - 76
     - ``_fOption5``
     - ``float``
     - -
     - Optional telemetry #5
   * - 80
     - ``_fOption6``
     - ``float``
     - -
     - Optional telemetry #6
   * - 84
     - ``_fOption7``
     - ``float``
     - -
     - Optional telemetry #7
   * - 88
     - ``_fOption8``
     - ``float``
     - -
     - Optional telemetry #8
   * - 92
     - ``_fOption9``
     - ``float``
     - -
     - Optional telemetry #9
   * - 96
     - ``_fOption10``
     - ``float``
     - -
     - Optional telemetry #10
   * - 100
     - ``_iCurrentFlow``
     - ``unsigned char``
     - 0~1
     - Current flow status
   * - 101
     - ``_iProcessActive``
     - ``unsigned char``
     - 0~1
     - Process active status
   * - 102
     - ``_iMachineryReady``
     - ``unsigned char``
     - 0~1
     - Welding machine ready status
   * - 104
     - ``_fVoltageCorrection``
     - ``float``
     - -
     - Voltage correction value
   * - 108
     - ``_fDynamicCorrection``
     - ``float``
     - -
     - Dynamic correction value

Total size: 112 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_DIGITAL_WELDING_DATA
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
       float _fFeedingVel;
       float _fActualFeedingVel;
       int   _iErrorNumber;
       float _fWireStick;
       int   _iError;
       float _fOption1;
       float _fOption2;
       float _fOption3;
       float _fOption4;
       float _fOption5;
       float _fOption6;
       float _fOption7;
       float _fOption8;
       float _fOption9;
       float _fOption10;
       unsigned char _iCurrentFlow;
       unsigned char _iProcessActive;
       unsigned char _iMachineryReady;
       float _fVoltageCorrection;
       float _fDynamicCorrection;
   } ROBOT_DIGITAL_WELDING_DATA, *LPROBOT_DIGITAL_WELDING_DATA;

   typedef ROBOT_DIGITAL_WELDING_DATA
       MONITORING_DIGITAL_WELDING, *LPMONITORING_DIGITAL_WELDING;