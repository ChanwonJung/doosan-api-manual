.. _struct_CONFIG_ZIGZAG_WEAVING_SETTING:

CONFIG_ZIGZAG_WEAVING_SETTING
==============================

This structure defines the **zigzag weaving motion parameters**  
used in welding processes to generate a repeating back-and-forth path pattern.  
It includes weaving offsets, path gradient, and cycle timing.

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
     - Weaving gradient angle (degrees)
   * - 12
     - ``_fWeavingWidth``
     - ``float``
     - -
     - Width of the zigzag pattern (mm)
   * - 16
     - ``_fWeavingCycle``
     - ``float``
     - -
     - Period of one weaving cycle (seconds)

Total size: 20 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_ZIGZAG_WEAVING_SETTING
   {
       /* Offset along Y-axis (mm) */
       float _fOffsetY;
       /* Offset along Z-axis (mm) */
       float _fOffsetZ;
       /* Weaving gradient angle (degrees) */
       float _fGradient;
       /* Zigzag weaving width (mm) */
       float _fWeavingWidth;
       /* Zigzag weaving cycle period (sec) */
       float _fWeavingCycle;

   } CONFIG_ZIGZAG_WEAVING_SETTING, *LPCONFIG_ZIGZAG_WEAVING_SETTING;

.. note::
   - ``CONFIG_TRAPEZOID_WEAVING_SETTING`` is used for **complex trapezoidal oscillation patterns**,  
     where motion includes acceleration and delay phases.  
   - ``CONFIG_ZIGZAG_WEAVING_SETTING`` provides a simpler **repetitive back-and-forth pattern**.  
   - Both structures are used in **welding path generation** for bead shaping and heat distribution control.