.. _struct_MONITORING_CTRLIO_EX:

MONITORING_CTRLIO_EX
====================

This is structure information for checking I/O current state information installed in the control box of the robot controller, and is composed of the following fields.

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
     - :ref:`READ_CTRLIO_INPUT_EX <struct_READ_CTRLIO_INPUT_EX>`
     - -
     - I/O Information (#1): **Digital/Analog/Switch/Safety/Analog-mode**
   * - 31
     - ``_tOutput``
     - :ref:`READ_CTRLIO_OUTPUT_EX <struct_READ_CTRLIO_OUTPUT_EX>`
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
     - **Reserved Space**

Total size: 93 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_CTRLIO_EX
   {
       READ_CTRLIO_INPUT_EX  _tInput;     /* 31 bytes */
       READ_CTRLIO_OUTPUT_EX _tOutput;    /* 26 bytes */
       READ_ENCODER_INPUT    _tEncoder;   /* 12 bytes */
       unsigned char         _szReserved[24];
   } MONITORING_CTRLIO_EX, *LPMONITORING_CTRLIO_EX;
