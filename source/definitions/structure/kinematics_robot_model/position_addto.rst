.. _struct_POSITION_ADDTO:

POSITION_ADDTO
===============

This structure defines the **position addition operation** data used to apply  
an offset to a given pose or coordinate.  
It specifies both the **reference pose** and the **offset values** to be added  
in each axis (joint or Cartesian space).

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Base position (original pose before applying offset)
   * - 24
     - ``_fTargetVal``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Offset values to be added (ΔX, ΔY, ΔZ, ΔRx, ΔRy, ΔRz)

Total size: 48 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _POSITION_ADDTO
   {
       /* Base target pose */
       float _fTargetPos[NUMBER_OF_JOINT];

       /* Offset values to add (ΔX, ΔY, ΔZ, ΔRx, ΔRy, ΔRz) */
       float _fTargetVal[NUMBER_OF_JOINT];

   } POSITION_ADDTO, *LPPOSITION_ADDTO;
