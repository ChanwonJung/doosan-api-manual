.. _struct_CONFIG_DIGITAL_WELDING_CONDITION:

CONFIG_DIGITAL_WELDING_CONDITION
================================

This structure defines all **parameter settings** for digital welding mode operation,  
including process type, speed limits, correction factors, and optional extended values.  
It is used to configure a digital welding controller before execution.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_cVirtualWelding``
     - ``unsigned char``
     - 0 or 1
     - Virtual mode flag |br|
       (0: Real, 1: Virtual)
   * - 1
     - ``_fTargetVel``
     - ``float``
     - -
     - Target welding velocity (mm/s)
   * - 5
     - ``_fMinVelLimit``
     - ``float``
     - -
     - Minimum velocity limit
   * - 9
     - ``_fMaxVelLimit``
     - ``float``
     - -
     - Maximum velocity limit
   * - 13
     - ``_nWeldingMode`` ~ ``_nWMopt1``
     - ``unsigned int``
     - -
     - **Mode options** |br|
       ``_nWeldingMode``: Base process |br|
       ``_n2t2tSpecial``: 2T/2T special function |br|
       ``_nPulseMode``: Pulse control |br|
       ``_nWMopt1``: User-defined welding option
   * - 29
     - ``_cSimulation``
     - ``unsigned char``
     - 0 or 1
     - Simulation flag |br|
       (0: Disabled, 1: Enabled)
   * - 30
     - ``_cTSopt1``, ``_cTSopt2``
     - ``unsigned char``
     - 0 or 1
     - Test signal options
   * - 32
     - ``_nJobNumber`` ~ ``_nSynergicID``
     - ``unsigned int``
     - -
     - Job number, Synergic ID
   * - 40
     - ``_fWireFeedSpeed`` ~ ``_fDynamicCorrection``
     - ``float``
     - -
     - **Core process values** |br|
       wire speed, arc length, dynamic response
   * - 52
     - ``_fOption1`` ~ ``_fOption15``
     - ``float[15]``
     - -
     - Extended user-defined options 1~15

Total size: 112 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_CONDITION
   {
       unsigned char _cVirtualWelding;
       float _fTargetVel;
       float _fMinVelLimit;
       float _fMaxVelLimit;
       unsigned int _nWeldingMode;
       unsigned int _n2t2tSpecial;
       unsigned int _nPulseMode;
       unsigned int _nWMopt1;
       unsigned char _cSimulation;
       unsigned char _cTSopt1;
       unsigned char _cTSopt2;
       unsigned int _nJobNumber;
       unsigned int _nSynergicID;
       float _fWireFeedSpeed;
       float _fArclengthCorrection;
       float _fDynamicCorrection;
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
       float _fOption11;
       float _fOption12;
       float _fOption13;
       float _fOption14;
       float _fOption15;

   } CONFIG_DIGITAL_WELDING_CONDITION, *LPCONFIG_DIGITAL_WELDING_CONDITION;

.. note::
   - Provides a complete **digital representation of welding parameters**.  
   - Includes both base process control and up to 15 extended options.  
   - Commonly used in **fully digital power source communication** protocols.