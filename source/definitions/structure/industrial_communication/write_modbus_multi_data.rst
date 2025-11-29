.. _struct_WRITE_MODBUS_MULTI_DATA:
.. _sturct_WRITE_MODBUS_TCP_MULTI_DATA:

WRITE_MODBUS_MULTI_DATA
=======================

This is a structure information to define a Modbus TCP multi-register write request,  
including target address, slave information, register start index, and count.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szSymbol``
     - ``char[MAX_SYMBOL_SIZE]``
     - -
     - Symbol name
   * - 32
     - ``_szIpAddr``
     - ``char[16]``
     - -
     - IPv4 string (null-terminated)
   * - 48
     - ``_iPort``
     - ``unsigned short``
     - -
     - TCP port
   * - 52
     - ``_iSlaveID``
     - ``int``
     - -
     - Slave ID
   * - 56
     - ``_iRegType``
     - ``unsigned char``
     - -
     - Register type
   * - 58
     - ``_iRegIndex``
     - ``unsigned short``
     - -
     - Start register address
   * - 60
     - ``_iRegCount``
     - ``unsigned char``
     - -
     - Number of registers

Total size: 64 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WRITE_MODBUS_MULTI_DATA
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
       /* register start address */
       unsigned short              _iRegIndex;
       /* register count */
       unsigned char               _iRegCount;

   } WRITE_MODBUS_MULTI_DATA, *LPWRITE_MODBUS_MULTI_DATA;

   typedef WRITE_MODBUS_MULTI_DATA
        WRITE_MODBUS_TCP_MULTI_DATA, *LPWRITE_MODBUS_TCP_MULTI_DATA;