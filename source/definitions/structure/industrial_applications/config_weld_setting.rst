.. _struct_CONFIG_WELD_SETTING:
.. _struct_GET_WELDING_SETTING_RESPONSE:

CONFIG_WELD_SETTING
===================

This structure defines the **general welding configuration parameters**,  
including voltage, current, speed, and timing details for start/finish phases.  

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bVirtualMode``
     - ``unsigned char``
     - 0 or 1
     - **Virtual welding mode flag** |br|
       0: Physical welding |br|
       1: Virtual (simulation)
   * - 4
     - ``_fTargetVol``
     - ``float``
     - 
     - Target voltage(V)
   * - 8
     - ``_fTargetCur``
     - ``float``
     - 
     - Target current(A)
   * - 12
     - ``_fTargetVel``
     - ``float``
     - 
     - Target welding velocity(mm/s)
   * - 16
     - ``_fTargetMinVel``
     - ``float``
     - 
     - Minimum welding velocity(mm/s)
   * - 20
     - ``_fTargetMaxVel``
     - ``float``
     - 
     - Maximum welding velocity(mm/s)
   * - 24
     - ``_tDetail._fRs``
     - ``float``
     - 
     - Ratio Start value
   * - 28
     - ``_tDetail._fTss``
     - ``float``
     - 
     - Shielding gas pre-flow time(s)
   * - 32
     - ``_tDetail._fTas``
     - ``float``
     - 
     - Arc start delay time(s)
   * - 36
     - ``_tDetail._fTwc``
     - ``float``
     - 
     - Welding condition change time(s)
   * - 40
     - ``_tDetail._fRf``
     - ``float``
     - 
     - Ratio Finish value
   * - 44
     - ``_tDetail._fTaf``
     - ``float``
     - 
     - Arc finish delay time(s)
   * - 48
     - ``_tDetail._fTsf``
     - ``float``
     - 
     - Shielding gas post-flow time(s)

Total size: **52 bytes**

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_WELD_SETTING
   {
       /* disable: 0, enable: 1 (virtual welding mode) */
       unsigned char _bVirtualMode;

       /* welding parameters */
       float _fTargetVol;
       float _fTargetCur;
       float _fTargetVel;
       float _fTargetMinVel;
       float _fTargetMaxVel;

       /* timing and ratio details */
       struct {
           float _fRs;   // ratio start
           float _fTss;  // shielding gas pre-flow time (sec)
           float _fTas;  // arc start delay (sec)
           float _fTwc;  // welding condition change (sec)
           float _fRf;   // ratio finish
           float _fTaf;  // arc finish delay (sec)
           float _fTsf;  // shielding gas post-flow time (sec)
       } _tDetail;

   } CONFIG_WELD_SETTING, *LPCONFIG_WELD_SETTING;

   /* Alias for retrieval of welding configuration parameters */
   typedef CONFIG_WELD_SETTING
       GET_WELDING_SETTING_RESPONSE, *LPGET_WELDING_SETTING_RESPONSE;

.. note::
   - ``_bVirtualMode`` determines whether the welding operation is simulated.  
   - ``_tDetail`` includes pre/post gas flow and transition timings.  
   - Used for both **command configuration** and **response queries** (alias form).
