.. _struct_CONFIG_TRAPEZOID_WEAVING_SETTING:

CONFIG_TRAPEZOID_WEAVING_SETTING
=================================

This structure defines the **trapezoidal weaving motion parameters**  
used for welding applications.  
It specifies weaving offsets, gradients, time constants, and pattern geometry,  
allowing precise control over the weld path oscillation.

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
     - ``_fwPT1[2]``
     - ``float[2]``
     - -
     - Weaving wPT1 X, Y Coordinate
   * - 20
     - ``_fwPT2[2]``
     - ``float[2]``
     - -
     - Weaving wPT2 X, Y Coordinate
   * - 28
     - ``_fwT1``
     - ``float``
     - -
     - Time constant for first weaving segment
   * - 32
     - ``_fwT2``
     - ``float``
     - -
     - Time constant for second weaving segment
   * - 36
     - ``_fwTAcc1``
     - ``float``
     - -
     - Acceleration duration for first segment
   * - 40
     - ``_fwTAcc2``
     - ``float``
     - -
     - Acceleration duration for second segment
   * - 44
     - ``_fwTTD1``
     - ``float``
     - -
     - Transition delay for first segment
   * - 48
     - ``_fwTTD2``
     - ``float``
     - -
     - Transition delay for second segment

Total size: 52 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TRAPEZOID_WEAVING_SETTING
   {
       /* Weaving offset along Y-axis (mm) */
       float _fOffsetY;
       /* Weaving offset along Z-axis (mm) */
       float _fOffsetZ;
       /* Gradient of weaving pattern (degrees) */
       float _fGradient;
       /* Trapezoidal pattern point 1 (X, Y) */
       float _fwPT1[2];
       /* Trapezoidal pattern point 2 (X, Y) */
       float _fwPT2[2];
       /* Time parameters */
       float _fwT1;
       float _fwT2;
       /* Acceleration parameters */
       float _fwTAcc1;
       float _fwTAcc2;
       /* Transition delays */
       float _fwTTD1;
       float _fwTTD2;

   } CONFIG_TRAPEZOID_WEAVING_SETTING, *LPCONFIG_TRAPEZOID_WEAVING_SETTING;
