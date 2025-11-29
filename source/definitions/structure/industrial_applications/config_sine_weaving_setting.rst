.. _struct_CONFIG_SINE_WEAVING_SETTING:

CONFIG_SINE_WEAVING_SETTING
============================

This structure defines the **sinusoidal weaving motion parameters**,  
used to generate smooth, continuous sine-wave oscillations for welding patterns.  
It includes offsets, gradients, weaving width, and cycle time configuration.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fOffsetY``
     - ``float``
     - -
     - Weaving offset in **Y-direction** (mm)
   * - 4
     - ``_fOffsetZ``
     - ``float``
     - -
     - Weaving offset in **Z-direction** (mm)
   * - 8
     - ``_fGradient``
     - ``float``
     - -
     - Weaving path gradient angle (degrees)
   * - 12
     - ``_fWeavingWidth``
     - ``float``
     - -
     - Sine-wave weaving amplitude (mm)
   * - 16
     - ``_fWeavingCycle``
     - ``float``
     - -
     - Sine-wave weaving cycle duration (seconds)

Total size: 20 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_SINE_WEAVING_SETTING
   {
       /* Offset along Y-axis (mm) */
       float _fOffsetY;
       /* Offset along Z-axis (mm) */
       float _fOffsetZ;
       /* Gradient of weaving path (degrees) */
       float _fGradient;
       /* Amplitude of sine wave (mm) */
       float _fWeavingWidth;
       /* Cycle time of sine wave (seconds) */
       float _fWeavingCycle;

   } CONFIG_SINE_WEAVING_SETTING, *LPCONFIG_SINE_WEAVING_SETTING;

.. note::
   - ``CONFIG_CIRCULE_WEAVING_SETTING`` generates **elliptical or circular paths** by combining two phase-shifted waveforms.  
   - ``CONFIG_SINE_WEAVING_SETTING`` defines a **1D sinusoidal oscillation**, typically along a single plane.  
   - Both structures are commonly used in **welding bead shaping and heat control**.