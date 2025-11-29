.. _struct_MONITORING_MODBUS:

MONITORING_MODBUS
=================

This structure provides the current **Modbus I/O** states registered in the robot controller.  
It aggregates the count and an array of Modbus registers.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iRegCount``
     - ``unsigned short``
     - -
     - Number of Modbus I/O signals currently registered
   * - 2
     - ``_tRegister``
     - :ref:`MODBUS_REGISTER[] <struct_MODBUS_REGISTER>`
     - -
     - Modbus I/O signal information array (each entry size = 34 bytes)

Total size: 3402 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_MODBUS
   {
       unsigned short  _iRegCount;  /* modbus i/o count */
       MODBUS_REGISTER _tRegister[MAX_MODBUS_TOTAL_REGISTERS]; /* modbus i/o values */
   } MONITORING_MODBUS, *LPMONITORING_MODBUS;

.. note::
   - Each ``MODBUS_REGISTER`` occupies **(MAX_SYMBOL_SIZE + 2)** bytes.
   - Example (legacy manual): if ``MAX_SYMBOL_SIZE = 32`` and ``MAX_MODBUS_TOTAL_REGISTERS = 100``,
     then each register = **34 B**, so total size = **2 + 100×34 = 3402 B**.
   - The ``_iRegCount`` value (0..MAX_MODBUS_TOTAL_REGISTERS) indicates how many leading entries
     in ``_tRegister`` are valid.
