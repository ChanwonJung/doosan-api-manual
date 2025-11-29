.. _struct_READ_CTRLIO_INPUT:

READ_CTRLIO_INPUT
=================

This structure provides **real-time input data** from the robot controller, including signals for digital inputs,  
analog inputs, switches, safety inputs, encoders, and raw encoder data. It aggregates the various input signals  
needed for robot operation and diagnostics.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualDI``
     - ``unsigned char[NUM_DIGITAL]``
     - -
     - Digital inputs (16 channels)
   * - 16
     - ``_fActualAI``
     - ``float[NUM_ANALOG]``
     - -
     - Analog inputs (2 channels, numeric)
   * - 24
     - ``_iActualSW``
     - ``unsigned char[NUM_SWITCH]``
     - -
     - Switch inputs (3 channels)
   * - 27
     - ``_iActualSI``
     - ``unsigned char[NUM_SAFETY_IN]``
     - -
     - Safety inputs (2 channels)
   * - 29
     - ``_iActualEI``
     - ``unsigned char[NUM_ENCORDER]``
     - -
     - Encoder inputs (2 channels, on/off)
   * - 31
     - ``_iAcutualED``
     - ``unsigned int[NUM_ENCORDER]``
     - -
     - Encoder raw data (2 channels, numeric)

Total size: 39 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_CTRLIO_INPUT
   {
       unsigned char _iActualDI[NUM_DIGITAL];  /* Digital Input data (16) */
       float         _fActualAI[NUM_ANALOG];   /* Analog Input data (2) */
       unsigned char _iActualSW[NUM_SWITCH];   /* Switch input data (3) */
       unsigned char _iActualSI[NUM_SAFETY_IN];/* Safety Input data (2) */
       unsigned char _iActualEI[NUM_ENCORDER]; /* Encoder Input data (2) */
       unsigned int  _iAcutualED[NUM_ENCORDER];/* Encoder raw data (2) */
   } READ_CTRLIO_INPUT, *LPREAD_CTRLIO_INPUT;
