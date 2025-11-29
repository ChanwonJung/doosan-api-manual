.. _struct_WRITE_MODBUS_BURST:
.. _struct_MODBUS_REGISTER_BURST:

WRITE_MODBUS_BURST
==================

This is a structure information to store multiple Modbus I/O register values for a **burst write or monitoring operation**.  
Each entry in the register list is represented by the :ref:`MODBUS_REGISTER_MONITORING <struct_MODBUS_REGISTER_MONITORING>` structure.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iCount``
     - ``unsigned short``
     - -
     - Number of Modbus registers in the burst
   * - 2
     - ``_tRegister``
     - :ref:`MODBUS_REGISTER_MONITORING <struct_MODBUS_REGISTER_MONITORING>` [MAX_MODBUS_BURST_SIZE]
     - -
     - Array of Modbus register entries

Total size: 1090 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WRITE_MODBUS_BURST
   {
       /* modbus i/o count */
       unsigned short              _iCount;
       /* modbus i/o values */
       MODBUS_REGISTER_MONITORING  _tRegister[MAX_MODBUS_BURST_SIZE];

   } WRITE_MODBUS_BURST, *LPWRITE_MODBUS_BURST;

   typedef WRITE_MODBUS_BURST
       MODBUS_REGISTER_BURST, *LPMODBUS_REGISTER_BURST;