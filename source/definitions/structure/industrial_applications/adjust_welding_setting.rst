.. _struct_ADJUST_WELDING_SETTING:

ADJUST_WELDING_SETTING
=======================

This structure defines the **adjustable parameters for welding operation**,  
allowing both preset and real-time modification of welding variables such as  
voltage, current, velocity, and weaving offsets.  
It is used to fine-tune welding performance dynamically during or before operation.

.. list-table::
   :widths: 10 28 22 8 32
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
     - **Operation mode flag** |br|
       0: Preset mode |br|
       1: Real-time adjustment
   * - 1
     - ``_bResetFlag``
     - ``unsigned char``
     - 0 or 1
     - **Reset control flag** |br|
       0: Maintain current value |br|
       1: Reset
   * - 2
     - ``_fTargetVol``
     - ``float``
     - -
     - Target voltage value (V)
   * - 6
     - ``_fTargetCur``
     - ``float``
     - -
     - Target current value (A)
   * - 10
     - ``_fTargetVel``
     - ``float``
     - -
     - Target welding velocity (mm/s)
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
     - Weaving width scaling rate (percentage multiplier)

Total size: 26 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ADJUST_WELDING_SETTING
   {
       /* Mode selection: preset(0) or real-time(1) */
       unsigned char _bRealTime;

       /* Reset flag: keep current(0) or apply new setting(1) */
       unsigned char _bResetFlag;

       /* Target voltage (V) */
       float _fTargetVol;

       /* Target current (A) */
       float _fTargetCur;

       /* Target welding velocity (mm/s) */
       float _fTargetVel;

       /* Weaving offset along Y-axis (mm) */
       float _fOffsetY;

       /* Weaving offset along Z-axis (mm) */
       float _fOffsetZ;

       /* Weaving width scaling factor (ratio) */
       float _fWidthRate;

   } ADJUST_WELDING_SETTING, *LPADJUST_WELDING_SETTING;

.. note::
   - ``_bRealTime`` enables **on-the-fly welding parameter control**,  
     useful for adaptive welding applications.  
   - ``_bResetFlag`` allows either retaining the current welding state  
     or fully reinitializing to new preset values.  
   - The combination of **voltage**, **current**, and **velocity** defines the welding heat input,  
     while **_fOffsetY/Z** and **_fWidthRate** tune the oscillation path geometry.
