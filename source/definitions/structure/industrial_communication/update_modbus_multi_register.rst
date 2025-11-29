.. _struct_UPDATE_MODBUS_MULTI_REGISTER:

UPDATE_MODBUS_MULTI_REGISTER
============================

This is a structure information to update multiple Modbus register values within a single Modbus device.  
It includes the Modbus I/O symbolic name, the number of registers, and their corresponding register values.

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
     - Number of Modbus registers to update
   * - 33
     - ``_iRegValue``
     - ``unsigned short[MAX_MODBUS_REGISTER_PER_DEVICE]``
     - -
     - Array containing Modbus register values to be updated

Total size: 134 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _UPDATE_MODBUS_MULTI_REGISTER
   {
       /* modbus i/o name */
       char                        _szSymbol[MAX_SYMBOL_SIZE];
       /* register count */
       unsigned char               _iRegCount;
       /* modbus i/o value */
       unsigned short              _iRegValue[MAX_MODBUS_REGISTER_PER_DEVICE];
       /* register start address (not used) */
       //unsigned short              _iRegIndex;
       /* Slave ID (not used) */
       //unsigned int                _iSlaveID;

   } UPDATE_MODBUS_MULTI_REGISTER, *LPUPDATE_MODBUS_MULTI_REGISTER;
