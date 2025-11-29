.. _struct_WEAVING_OFFSET:

WEAVING_OFFSET
==============

This structure defines **offset parameters** for the weaving pattern during welding.  
It specifies the displacement along Y and Z axes from the main welding path,  
allowing flexible control over bead shape and arc stability.

.. list-table::
   :widths: 10 30 20 8 32
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
     - Weaving offset along the **Y-axis** (mm)
   * - 4
     - ``_fOffsetZ``
     - ``float``
     - -
     - Weaving offset along the **Z-axis** (mm)

Total size: **8 bytes**

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WEAVING_OFFSET
   {
       /* weaving offset Y (mm) */
       float _fOffsetY;

       /* weaving offset Z (mm) */
       float _fOffsetZ;

   } WEAVING_OFFSET, *LPWEAVING_OFFSET;

.. note::
   - Adjusts the **welding torch oscillation** relative to the path.  
   - Typically used with sinusoidal or trapezoidal weaving patterns.  
   - Increasing the offset enlarges bead width or improves fusion.