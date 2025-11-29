.. _struct_READ_CTRLIO_OUTPUT_EX2:

READ_CTRLIO_OUTPUT_EX2
======================

This structure provides **real-time output signals** from the robot controller, including digital outputs,  
analog outputs, and analog output modes specific to **EX2**. It is used for controlling actuator outputs in real time.

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
     - ``unsigned char[NUM_DIGITAL_V3]``
     - 0x00~0x01
     - Digital **outputs** (on/off)
   * - 16
     - ``_fTargetAO``
     - ``float[NUM_ANALOG]``
     - -
     - **Analog outputs** (numeric)
   * - 24
     - ``_iTargetAT``
     - ``unsigned char[NUM_ANALOG]``
     - 0x00~0x01
     - **Analog output mode** per channel

Total size: 26 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_CTRLIO_OUTPUT_EX2
   {
       unsigned char _iTargetDO[NUM_DIGITAL_V3];
       float         _fTargetAO[NUM_ANALOG];
       unsigned char _iTargetAT[NUM_ANALOG];
   } READ_CTRLIO_OUTPUT_EX2, *LPREAD_CTRLIO_OUTPUT_EX2;
