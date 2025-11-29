.. _struct_MACHINE_TENDING_FOCAS_PMC:

MACHINE_TENDING_FOCAS_PMC
=========================

PMC (Programmable Machine Control) **header + payload** for FOCAS operations.  
The header specifies target address/type/range; the payload holds typed data buffers.

.. list-table::
   :widths: 12 30 18 10 30
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - (platform-dependent)
     - ``_ErrorCode``
     - ``short``
     - -
     - 0 on success; negative/positive for errors
   * - -
     - ``_hHandle``
     - ``unsigned short``
     - -
     - Active FOCAS session handle
   * - -
     - ``_iDataType``
     - ``short``
     - -
     - PMC data type selector (vendor-defined)
   * - -
     - ``_szAddressType``
     - ``char[2]``
     - e.g. "G", "D"
     - PMC address class (1-char + optional)
   * - -
     - ``_iStartAddressNum``
     - ``unsigned short``
     - -
     - Start address number (word/bit base)
   * - -
     - ``_iCount``
     - ``unsigned short``
     - -
     - Number of PMC items to read/write
   * - -
     - ``_iBitOffset``
     - ``unsigned char``
     - 0-7
     - Bit offset for bit-level access
   * - -
     - ``_tData``
     - :ref:`MACHINE_TENDING_FOCAS_PMC_DATA <struct_MACHINE_TENDING_FOCAS_PMC_DATA>`
     - -
     - Typed PMC payload buffers

Size note: The total size is **platform-dependent** (``sizeof(long)``, alignment).

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_FOCAS_PMC // PMC Information Header
   {
       short                          _ErrorCode;
       unsigned short                 _hHandle;
       short                          _iDataType;
       char                           _szAddressType[2];    // e.g., "G", "D"
       unsigned short                 _iStartAddressNum;
       unsigned short                 _iCount;              // Read & Write data count
       unsigned char                  _iBitOffset;
       MACHINE_TENDING_FOCAS_PMC_DATA _tData;               // typed buffers
   } MACHINE_TENDING_FOCAS_PMC, *LPMACHINE_TENDING_FOCAS_PMC;