.. _struct_READ_ENCODER_INPUT:

READ_ENCODER_INPUT
==================

This structure provides **real-time encoder input signals** from the robot controller, including strobe signals,  
raw encoder data, and reset signals. It is used for monitoring encoder status and for performing diagnostics.

.. list-table::
   :widths: 10 32 18 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualES``
     - ``unsigned char[NUM_ENCORDER]``
     - 0x00~0x01
     - **Encoder strobe** signal (2ch)
   * - 2
     - ``_iActualED``
     - ``unsigned int[NUM_ENCORDER]``
     - -
     - **Encoder raw** data (2ch, numeric)
   * - 10
     - ``_iActualER``
     - ``unsigned char[NUM_ENCORDER]``
     - 0x00~0x01
     - **Encoder reset** signal (2ch)

Total size: 12 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_ENCODER_INPUT
   {
       unsigned char _iActualES[NUM_ENCORDER];
       unsigned int  _iActualED[NUM_ENCORDER];
       unsigned char _iActualER[NUM_ENCORDER];
   } READ_ENCODER_INPUT, *LPREAD_ENCODER_INPUT;
