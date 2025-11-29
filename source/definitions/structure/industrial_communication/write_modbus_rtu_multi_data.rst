.. _struct_WRITE_MODBUS_RTU_DATA:

WRITE_MODBUS_RTU_DATA
=====================

This is a structure information to define Modbus RTU write configuration,  
used for transmitting data to external Modbus slave devices via serial communication (RS-485/RS-232).

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szSymbol``
     - ``char[32]``
     - -
     - Symbol name (32-byte identifier)
   * - 32
     - ``_szttyPort``
     - ``char[16]``
     - -
     - Serial (TTY) port name (e.g., ``/dev/ttyUSB0``, ``COM3``)
   * - 48
     - ``_iSlaveID``
     - ``int``
     - -
     - Slave device ID (1–255)
   * - 52
     - ``_iBaudRate``
     - ``int``
     - -
     - Baud rate (e.g., 9600, 115200)
   * - 56
     - ``_iByteSize``
     - ``int``
     - -
     - Data bits (7 or 8)
   * - 60
     - ``_szParity``
     - ``char``
     - -
     - Parity (N/E/O)
   * - 61
     - ``_iStopBit``
     - ``int``
     - -
     - Stop bits (1 or 2)
   * - 65
     - ``_iRegType``
     - ``unsigned char``
     - -
     - Register type |br| 
       (0: Coil, 1: DI, 2: Holding, 3: Input)
   * - 66
     - ``_iRegIndex``
     - ``unsigned short``
     - -
     - Register address (index)
   * - 68
     - ``_iRegValue``
     - ``unsigned short``
     - -
     - Register value (0-65535)

Total size: 72 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WRITE_MODBUS_RTU_DATA
   {
       /* symbol name */
       char            _szSymbol[MAX_SYMBOL_SIZE];
       /* tty device */
       char            _szttyPort[16];
       /* Slave ID*/
       int             _iSlaveID;
       /* Baud Rate */
       int             _iBaudRate;
       /* Byte size */
       int             _iByteSize;
       /* Parity */
       char            _szParity;
       /* Stop bit */
       int             _iStopBit;
       /* i/o type */
       unsigned char   _iRegType;
       /* register address */
       unsigned short  _iRegIndex;
       /* register value */
       unsigned short  _iRegValue;

   } WRITE_MODBUS_RTU_DATA, *LPWRITE_MODBUS_RTU_DATA;
