.. _struct_MODBUS_DATA_LIST:

MODBUS_DATA_LIST
================

This structure defines a **collection of Modbus configuration entries**,  
each represented by a :ref:`MODBUS_DATA <struct_MODBUS_DATA>` structure.  
It is typically used when multiple Modbus devices or registers must be configured at once.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_nCount``
     - ``unsigned short``
     - -
     - Number of Modbus data
   * - 2
     - ``_tRegister``
     - :ref:`MODBUS_DATA <struct_MODBUS_DATA>` ``[MAX_MODBUS_TOTAL_REGISTERS]``
     - -
     - Refer to the Definition of Struct

Total size : 11,202 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MODBUS_DATA_LIST
   {
       /* Number of Modbus configurations */
       unsigned short  _nCount;

       /* Array of Modbus data entries */
       MODBUS_DATA     _tRegister[MAX_MODBUS_TOTAL_REGISTERS];

   } MODBUS_DATA_LIST, *LPMODBUS_DATA_LIST;