.. _struct_MACHINE_TENDING_FOCAS_PMC_DATA:

MACHINE_TENDING_FOCAS_PMC_DATA
==============================

This structure contains **typed PMC data buffers** returned from / sent to a CNC via the FOCAS interface.
Each array slot (index 0..4) represents one PMC data point for the corresponding type.

.. list-table::
   :widths: 12 30 18 10 30
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - (platform-dependent)
     - ``_PmcDataBool``
     - ``unsigned char``
     - 0 or 1
     - Boolean PMC value
   * - -
     - ``_PmcDataChar``
     - ``char[5]``
     - ASCII
     - Up to 5 characters
   * - -
     - ``_PmcDataShort``
     - ``short[5]``
     - -
     - Signed 16-bit values
   * - -
     - ``_PmcDataLong``
     - ``long[5]``
     - -
     - Signed long values *(size is platform-dependent)*
   * - -
     - ``_PmcDataFloat``
     - ``float[5]``
     - -
     - IEEE-754 single
   * - -
     - ``_PmcDataDouble``
     - ``double[5]``
     - -
     - IEEE-754 double

Size note: The total size is **platform-dependent** due to ``sizeof(long)`` and structure alignment.

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_FOCAS_PMC_DATA
   {
       unsigned char  _PmcDataBool;
       char           _PmcDataChar[5];
       short          _PmcDataShort[5];
       long           _PmcDataLong[5];
       float          _PmcDataFloat[5];
       double         _PmcDataDouble[5];
   } MACHINE_TENDING_FOCAS_PMC_DATA, *LPMACHINE_TENDING_FOCAS_PMC_DATA;