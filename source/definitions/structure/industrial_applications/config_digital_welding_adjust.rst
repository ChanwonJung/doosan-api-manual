.. _struct_CONFIG_DIGITAL_WELDING_ADJUST:

CONFIG_DIGITAL_WELDING_ADJUST
=============================

This structure defines **adjustable parameters** for real-time modification  
of digital welding conditions during operation.  
It enables the robot or controller to dynamically tune the welding parameters  
without restarting the process.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bRealTime``
     - ``unsigned char``
     - 0 or 1
     - **Adjustment type** |br|
       0: Preset |br|
       1: Real-time adjustment
   * - 1
     - ``_bResetFlag``
     - ``unsigned char``
     - 0 or 1
     - **Determines if parameters reset to default** |br|
       0: Keep current value |br|
       1: Reset to set value
   * - 2
     - ``_fFeedingVel`` ~ ``_fTargetVel``
     - ``float``
     - -
     - Target feeding and travel velocities (mm/sec)
   * - 10
     - ``_fOffsetY``, ``_fOffsetZ``
     - ``float``
     - -
     - Weaving offset adjustments
   * - 18
     - ``_fWidthRate``
     - ``float``
     - -
     - Weaving width ratio
   * - 22
     - ``_fDynamicCor``
     - ``float``
     - -
     - Dynamic correction factor
   * - 26
     - ``_fVoltageCor``
     - ``float``
     - -
     - Voltage correction factor
   * - 30
     - ``_nJobNumber``, ``_nSynergicID``
     - ``int``
     - -
     - Program and synergic identifiers

Total size: 34 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_ADJUST
   {
       unsigned char _bRealTime;
       unsigned char _bResetFlag;
       float _fFeedingVel;
       float _fTargetVel;
       float _fOffsetY;
       float _fOffsetZ;
       float _fWidthRate;
       float _fDynamicCor;
       float _fVoltageCor;
       int _nJobNumber;
       int _nSynergicID;
   } CONFIG_DIGITAL_WELDING_ADJUST, *LPCONFIG_DIGITAL_WELDING_ADJUST;

.. note::
   - Used for **fine-tuning active welding conditions** without halting the process.  
   - ``_fDynamicCor`` adjusts arc responsiveness, while ``_fVoltageCor`` modifies voltage balance.  
   - Supports **adaptive welding applications** where real-time compensation is required.