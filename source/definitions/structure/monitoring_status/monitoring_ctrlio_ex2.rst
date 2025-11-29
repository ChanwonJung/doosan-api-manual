.. _struct_MONITORING_CTRLIO_EX2:

MONITORING_CTRLIO_EX2
=====================

This structure provides the current I/O state installed in the controller’s **Safety board (EX2)**.  
It aggregates input, output, and encoder sections, plus a reserved area.

.. list-table::
   :widths: 10 32 18 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tInput``
     - :ref:`READ_CTRLIO_INPUT_EX2 <struct_READ_CTRLIO_INPUT_EX2>`
     - -
     - I/O Information (#1): **Digital/Analog/Switch/Safety/Analog-mode**
   * - 31
     - ``_tOutput``
     - :ref:`READ_CTRLIO_OUTPUT_EX2 <struct_READ_CTRLIO_OUTPUT_EX2>`
     - -
     - I/O Information (#2): **Digital/Analog/Analog-mode** 
   * - 57
     - ``_tEncoder``
     - :ref:`READ_ENCODER_INPUT <struct_READ_ENCODER_INPUT>`
     - -
     - I/O Information (#3): **Encoder strobe/raw/reset**
   * - 69
     - ``_szReserved``
     - ``unsigned char[24]``
     - -
     - **Reserved Space** (size: 24 B)

Total size: 93 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_CTRLIO_EX2
   {
       READ_CTRLIO_INPUT_EX2  _tInput;     /* 31 bytes */
       READ_CTRLIO_OUTPUT_EX2 _tOutput;    /* 26 bytes */
       READ_ENCODER_INPUT     _tEncoder;   /* 12 bytes */
       unsigned char          _szReserved[24];
   } MONITORING_CTRLIO_EX2, *LPMONITORING_CTRLIO_EX2;
