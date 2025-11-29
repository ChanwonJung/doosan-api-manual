.. _struct_ANALOG_WELDING_ADJUST_SETTING:

ANALOG_WELDING_ADJUST_SETTING
=============================

This structure defines **real-time adjustment parameters** for analog welding control.  
It allows dynamic tuning of voltage, velocity, and weaving parameters during operation,  
supporting both preset and on-the-fly updates.

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
     - Adjustment mode |br|
       (0: Preset, 1: Real-time)
   * - 1
     - ``_bResetFlag``
     - ``unsigned char``
     - 0 or 1
     - **Reset behavior flag** |br|
       0: Keep current values |br|
       1: Apply new setting values
   * - 2
     - ``_fTargetVol``
     - ``float``
     - -
     - Target voltage (V)
   * - 6
     - ``_fFeedingVel``
     - ``float``
     - -
     - Wire feeding velocity (mm/s)
   * - 10
     - ``_fTargetVel``
     - ``float``
     - -
     - Welding travel velocity (mm/s)
   * - 14
     - ``_fOffsetY``
     - ``float``
     - -
     - Weaving offset along Y-axis (mm)
   * - 18
     - ``_fOffsetZ``
     - ``float``
     - -
     - Weaving offset along Z-axis (mm)
   * - 22
     - ``_fWidthRate``
     - ``float``
     - -
     - Weaving width scaling ratio

Total size: 26 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ANALOG_WELDING_ADJUST_SETTING
   {
       /* 0: Preset mode, 1: Real-time adjustment */
       unsigned char _bRealTime;

       /* 0: Keep current values, 1: Apply new settings */
       unsigned char _bResetFlag;

       /* Target voltage (V) */
       float _fTargetVol;

       /* Wire feeding velocity (mm/s) */
       float _fFeedingVel;

       /* Welding velocity (mm/s) */
       float _fTargetVel;

       /* Weaving offset along Y-axis (mm) */
       float _fOffsetY;

       /* Weaving offset along Z-axis (mm) */
       float _fOffsetZ;

       /* Weaving width scaling ratio */
       float _fWidthRate;

   } ANALOG_WELDING_ADJUST_SETTING, *LPANALOG_WELDING_ADJUST_SETTING;

.. note::
   - Enables **real-time process correction** during active welding.  
   - ``_fFeedingVel`` can be adjusted to control bead consistency dynamically.  
   - Commonly used in **adaptive welding systems** with sensor feedback or vision guidance.