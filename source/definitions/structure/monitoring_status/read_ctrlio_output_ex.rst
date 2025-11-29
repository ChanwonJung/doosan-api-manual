.. _struct_READ_CTRLIO_OUTPUT_EX:

READ_CTRLIO_OUTPUT_EX
=====================

This structure provides **real-time output signals** from the robot controller, including digital outputs,  
analog outputs, and analog output modes. It aggregates the output control signals necessary for robot operations.

.. list-table::
   :widths: 10 32 18 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetDO``
     - ``unsigned char[NUM_DIGITAL]``
     - 0x00~0x01
     - Digital **outputs** (16ch, on/off)
   * - 16
     - ``_fTargetAO``
     - ``float[NUM_ANALOG]``
     - -
     - **Analog outputs** (2ch, numeric)
   * - 24
     - ``_iTargetAT``
     - ``unsigned char[NUM_ANALOG]``
     - 0x00~0x01
     - **Analog output mode** (per channel)

Total size: 26 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_CTRLIO_OUTPUT_EX
   {
       unsigned char _iTargetDO[NUM_DIGITAL];
       float         _fTargetAO[NUM_ANALOG];
       unsigned char _iTargetAT[NUM_ANALOG];
   } READ_CTRLIO_OUTPUT_EX, *LPREAD_CTRLIO_OUTPUT_EX;
