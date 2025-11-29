.. _struct_CONFIG_ANALOG_WELDING_SETTING:

CONFIG_ANALOG_WELDING_SETTING
=============================

This structure defines **analog welding operation settings**,  
including target voltage, current, velocity, and time-related parameters  
for both the start and end phases of the welding process.  
It allows precise configuration of welding behavior such as gas release,  
arc rise/fall times, and voltage transitions.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iVirtualWelding``
     - ``unsigned char``
     - 0 or 1
     - **Welding mode flag** |br|
       0: Real Welding |br|
       1: Virtual Welding
   * - 1
     - ``_fTargetVoltage``
     - ``float``
     - -
     - Target voltage (V)
   * - 5
     - ``_fTargetCurrent``
     - ``float``
     - -
     - Target current (A)
   * - 9
     - ``_fTargetVel``
     - ``float``
     - -
     - Target travel velocity (mm/s)
   * - 13
     - ``_fMinVel``
     - ``float``
     - -
     - Minimum allowed velocity (mm/s)
   * - 17
     - ``_fMaxVel``
     - ``float``
     - -
     - Maximum allowed velocity (mm/s)
   * - 21
     - ``_tDetail._fRs``
     - ``float``
     - -
     - Ratio start — initial power ratio
   * - 25
     - ``_tDetail._fTss``
     - ``float``
     - -
     - Shielding gas pre-flow time (sec)
   * - 29
     - ``_tDetail._fTas``
     - ``float``
     - -
     - Arc start current rise time (sec)
   * - 33
     - ``_tDetail._fTwc``
     - ``float``
     - -
     - Welding condition change time (sec)
   * - 37
     - ``_tDetail._fRf``
     - ``float``
     - -
     - Ratio finish — final power ratio
   * - 41
     - ``_tDetail._fTaf``
     - ``float``
     - -
     - Arc current decay time (sec)
   * - 45
     - ``_tDetail._fTsf``
     - ``float``
     - -
     - Shielding gas post-flow time (sec)
   * - 49
     - ``_tDetail._fStartVoltage``
     - ``float``
     - -
     - Start voltage condition (V)
   * - 53
     - ``_tDetail._fEndVoltage``
     - ``float``
     - -
     - End voltage condition (V)
   * - 57
     - ``_fTargetFeedingSpeed``
     - ``float``
     - -
     - Wire feeding speed (mm/s)

Total size: 61 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_ANALOG_WELDING_SETTING
   {
       /* 0: Real welding, 1: Virtual welding */
       unsigned char _iVirtualWelding;

       /* Target voltage (V) */
       float _fTargetVoltage;

       /* Target current (A) */
       float _fTargetCurrent;

       /* Target welding velocity (mm/s) */
       float _fTargetVel;

       /* Minimum velocity (mm/s) */
       float _fMinVel;

       /* Maximum velocity (mm/s) */
       float _fMaxVel;

       /* Detailed welding phase timing parameters */
       struct
       {
           float _fRs;             /* Ratio start */
           float _fTss;            /* Shielding gas pre-flow time */
           float _fTas;            /* Arc start current rise time */
           float _fTwc;            /* Welding condition change time */
           float _fRf;             /* Ratio finish */
           float _fTaf;            /* Arc end current decay time */
           float _fTsf;            /* Shielding gas post-flow time */
           float _fStartVoltage;   /* Start voltage condition */
           float _fEndVoltage;     /* End voltage condition */
       } _tDetail;

       /* Wire feeding speed (mm/s) */
       float _fTargetFeedingSpeed;

   } CONFIG_ANALOG_WELDING_SETTING, *LPCONFIG_ANALOG_WELDING_SETTING;

.. note::
   - ``_iVirtualWelding`` allows testing and parameter verification without actual arc ignition.  
   - ``_tDetail`` provides **fine-grained control** over the welding sequence timing.  
   - Adjusting **_fRs**, **_fRf**, and **_fTwc** helps manage smooth transitions during weld start and stop.  
   - Typical applications include **MIG/MAG welding systems** and **robotic process optimization**.
