.. _struct_WRITE_SERIAL_BURST:
.. _struct_GPIO_SETOUTPUT_BURST:

WRITE_SERIAL_BURST
==================

This structure defines a **burst output configuration** for writing multiple GPIO ports simultaneously.  
It is mainly used when sending bulk digital output commands to the robot’s control box or arm modules.  
Each burst operation specifies a location, port count, and port data array.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iLocation``
     - ``unsigned char``
     - 0 or 1
     - **Target hardware location** |br|
       0: Control Box |br|
       1: Arm-mounted I/O
   * - 2
     - ``_iCount``
     - ``unsigned short``
     - 0~16
     - Number of GPIO ports included in this burst operation.
   * - 4
     - ``_tPort[MAX_DIGITAL_BURST_SIZE]``
     - :ref:`GPIO_PORT <struct_GPIO_PORT>`
     - -
     - Array containing the configuration of each output port.

Total size: 132 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WRITE_SERIAL_BURST
   {
       /* Target device location (0: control box, 1: arm I/O) */
       unsigned char _iLocation;

       /* Number of GPIO ports included in the burst */
       unsigned short _iCount;

       /* I/O port data array */
       GPIO_PORT _tPort[MAX_DIGITAL_BURST_SIZE];

   } WRITE_SERIAL_BURST, *LPWRITE_SERIAL_BURST;

   /* Alias for setting multiple GPIO outputs simultaneously */
   typedef WRITE_SERIAL_BURST
       GPIO_SETOUTPUT_BURST, *LPGPIO_SETOUTPUT_BURST;
