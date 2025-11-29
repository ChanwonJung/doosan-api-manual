.. _struct_MODBUS_REGISTER_MONITORING:

MODBUS_REGISTER_MONITORING
==========================

This is a structure information to monitor a single Modbus register value.  
It contains the Modbus I/O symbolic name and its corresponding register value.

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
     - Symbolic name of the Modbus I/O
   * - 32
     - ``_iRegValue``
     - ``unsigned short``
     - -
     - Current Modbus register value

Total size: 34 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MODBUS_REGISTER_MONITORING
   {
       /* modbus i/o name */
       char                        _szSymbol[MAX_SYMBOL_SIZE];
       /* modbus i/o value */
       unsigned short              _iRegValue;

   } MODBUS_REGISTER_MONITORING, *LPMODBUS_REGISTER_MONITORING;
