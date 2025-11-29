.. _struct_CONFIG_CIRCULE_WEAVING_SETTING:

CONFIG_CIRCULE_WEAVING_SETTING
===============================

This structure defines the **circular weaving motion parameters**  
used for generating oscillatory circular patterns during welding operations.  
It specifies weaving offsets, gradients, width, and time cycle parameters,  
allowing smooth circular weaving control.

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
     - Weaving gradient or inclination angle (degrees)
   * - 12
     - ``_fwWdt[2]``
     - ``float[2]``
     - -
     - Weaving width parameters (**amplitude**) for two circular axes
   * - 20
     - ``_fwT[2]``
     - ``float[2]``
     - -
     - Weaving cycle durations (**periods**) for both circular components

Total size: 28 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_CIRCULE_WEAVING_SETTING
   {
       /* Weaving offset along Y-axis (mm) */
       float _fOffsetY;
       /* Weaving offset along Z-axis (mm) */
       float _fOffsetZ;
       /* Gradient of the circular path (degrees) */
       float _fGradient;
       /* Weaving width (amplitude) for two circular axes */
       float _fwWdt[2];
       /* Weaving cycle time for each axis (seconds) */
       float _fwT[2];

   } CONFIG_CIRCULE_WEAVING_SETTING, *LPCONFIG_CIRCULE_WEAVING_SETTING;