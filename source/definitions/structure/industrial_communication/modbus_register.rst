.. _struct_MODBUS_REGISTER:

MODBUS_REGISTER
===============

A single Modbus I/O entry containing the I/O **symbol name** and its **current value**.

.. list-table::
   :widths: 10 28 18 8 36
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
     - Modbus I/O name |br| 
       (null-terminated if shorter; **e.g., 32 bytes** in legacy manual)
   * - 32
     - ``_iValue``
     - ``unsigned short``
     - -
     - Modbus I/O value (raw 16-bit register)

Total size: 34 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MODBUS_REGISTER
   {
       char           _szSymbol[MAX_SYMBOL_SIZE]; /* modbus i/o name */
       unsigned short _iValue;                    /* modbus i/o value */
   } MODBUS_REGISTER, *LPMODBUS_REGISTER;