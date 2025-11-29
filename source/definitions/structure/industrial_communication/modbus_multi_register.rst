.. _struct_MODBUS_MULTI_REGISTER:

MODBUS_MULTI_REGISTER
=====================

This is a structure information to store multiple Modbus register values within a single device.  
It includes symbol name, register count, register values, starting register address, and slave ID.

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
     - Modbus I/O symbolic name
   * - 32
     - ``_iRegCount``
     - ``unsigned char``
     - -
     - Number of registers
   * - 33
     - ``_iRegValue``
     - ``unsigned short[MAX_MODBUS_REGISTER_PER_DEVICE]``
     - -
     - Register values
   * - 133
     - ``_iRegIndex``
     - ``unsigned short``
     - -
     - Starting register address
   * - 135
     - ``_iSlaveID``
     - ``unsigned int``
     - -
     - Slave device ID

Total size: 140 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MODBUS_MULTI_REGISTER
   {
       /* modbus i/o name */
       char                        _szSymbol[MAX_SYMBOL_SIZE];
       /* register count */
       unsigned char               _iRegCount;
       /* modbus i/o value */
       unsigned short              _iRegValue[MAX_MODBUS_REGISTER_PER_DEVICE];
       /* register start address */
       unsigned short              _iRegIndex;
       /* Slave ID */
       unsigned int                _iSlaveID;

   } MODBUS_MULTI_REGISTER, *LPMODBUS_MULTI_REGISTER;
