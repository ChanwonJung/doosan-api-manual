.. _struct_READ_CTRLIO_INPUT_EX:

READ_CTRLIO_INPUT_EX
====================

This structure provides detailed **real-time input signals** from the robot controller, including digital inputs,  
analog inputs, switch states, safety inputs, and analog input modes. It is used to monitor various input signals  
and their corresponding modes for robot operation and diagnostics.

.. list-table::
   :widths: 10 32 18 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualDI``
     - ``unsigned char[NUM_DIGITAL]``
     - 0x00~0x01
     - Digital **inputs** (16ch, on/off)
   * - 16
     - ``_fActualAI``
     - ``float[NUM_ANALOG]``
     - -
     - **Analog inputs** (2ch, numeric)
   * - 24
     - ``_iActualSW``
     - ``unsigned char[NUM_SWITCH]``
     - 0x00~0x01
     - **Switch inputs** (3ch, incl. direct-teach button)
   * - 27
     - ``_iActualSI``
     - ``unsigned char[NUM_SAFETY_IN]``
     - 0x00~0x01
     - **Safety** inputs (2ch)
   * - 29
     - ``_iActualAT``
     - ``unsigned char[NUM_ANALOG]``
     - 0x00~0x01
     - **Analog input mode** (per channel; e.g., 0: V, 1: I)

Total size: 31 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_CTRLIO_INPUT_EX
   {
       unsigned char _iActualDI[NUM_DIGITAL];
       float         _fActualAI[NUM_ANALOG];
       unsigned char _iActualSW[NUM_SWITCH];
       unsigned char _iActualSI[NUM_SAFETY_IN];
       unsigned char _iActualAT[NUM_ANALOG];
   } READ_CTRLIO_INPUT_EX, *LPREAD_CTRLIO_INPUT_EX;
