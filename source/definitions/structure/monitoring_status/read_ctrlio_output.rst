.. _struct_READ_CTRLIO_OUTPUT:

READ_CTRLIO_OUTPUT
==================

This structure provides **real-time output data** from the robot controller, including digital and analog outputs.  
It includes signals for controlling robot actuators or other hardware components requiring output control.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetDO``
     - ``unsigned char[NUM_DIGITAL]``
     - -
     - Digital outputs (16 channels)
   * - 16
     - ``_fTargetAO``
     - ``float[NUM_ANALOG]``
     - -
     - Analog outputs (2 channels, numeric)

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_CTRLIO_OUTPUT
   {
       unsigned char _iTargetDO[NUM_DIGITAL]; /* Digital Output data (16) */
       float         _fTargetAO[NUM_ANALOG];  /* Analog Output data (2) */
   } READ_CTRLIO_OUTPUT, *LPREAD_CTRLIO_OUTPUT;
