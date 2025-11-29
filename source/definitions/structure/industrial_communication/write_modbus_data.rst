.. _struct_WRITE_MODBUS_DATA:
.. _struct_WRITE_MODBUS_TCP_DATA:

WRITE_MODBUS_DATA
=================

This is a structure information to define a **Modbus TCP write configuration**,  
used for transmitting data from the robot controller to an external Modbus slave device via Ethernet (TCP/IP).

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
     - ``_szIpAddr``
     - ``char[16]``
     - -
     - Target device IP address (IPv4 string)
   * - 48
     - ``_iPort``
     - ``unsigned short``
     - -
     - TCP port number (e.g., 502)
   * - 52
     - ``_iSlaveID``
     - ``int``
     - -
     - Slave device ID (1-255)
   * - 56
     - ``_iRegType``
     - ``unsigned char``
     - -
     - **Register type** |br|
       0: Coil, 1: Discrete Input |br|
       2: Holding Register, 3: Input Register
   * - 58
     - ``_iRegIndex``
     - ``unsigned short``
     - -
     - Register address (index)
   * - 60
     - ``_iRegValue``
     - ``unsigned short``
     - -
     - Register value (0-65535)

Total size: 64 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WRITE_MODBUS_DATA
   {
       /* symbol name */
       char                        _szSymbol[MAX_SYMBOL_SIZE];
       /* tcp address */
       char                        _szIpAddr[16];
       /* tcp port */
       unsigned short              _iPort;
       /* Slave ID*/
       int                         _iSlaveID;
       /* i/o type */
       unsigned char               _iRegType;
       /* register address */
       unsigned short              _iRegIndex;
       /* register value */
       unsigned short              _iRegValue;

   } WRITE_MODBUS_DATA, *LPWRITE_MODBUS_DATA;

   typedef WRITE_MODBUS_DATA
       WRITE_MODBUS_TCP_DATA, *LPWRITE_MODBUS_TCP_DATA;
