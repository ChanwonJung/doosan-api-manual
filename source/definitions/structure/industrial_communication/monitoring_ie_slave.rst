.. _struct_MONITORING_IE_SLAVE:

MONITORING_IE_SLAVE
===================

This structure provides a unified monitoring interface for **Industrial Ethernet (IE) slave devices**.  
It aggregates Modbus coil data, Modbus holding register data, and Industrial Ethernet GPR (General Purpose Register) information.  
This enables comprehensive monitoring of both digital and analog states from connected industrial devices.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tMbusCoil``
     - :ref:`MONITORING_MBUS_SLAVE_COIL <struct_MONITORING_MBUS_SLAVE_COIL>`
     - -
     - Modbus coil state monitoring (digital input/output, safety, and servo state)
   * - 12
     - ``_tMbusHoldingRegister``
     - :ref:`MONITORING_MBUS_SLAVE_HOILDING_REGISTER <struct_MONITORING_MBUS_SLAVE_HOILDING_REGISTER>`
     - -
     - Modbus holding register data, including analog I/O, GPR, and robot telemetry
   * - 418
     - ``_tIndustrialEthernetGPR``
     - :ref:`MONITORING_IE_GPR <struct_MONITORING_IE_GPR>`
     - -
     - Industrial Ethernet General Purpose Register (GPR) data for process communication

Total size: 882 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_IE_SLAVE
   {
       MONITORING_MBUS_SLAVE_COIL              _tMbusCoil;
       MONITORING_MBUS_SLAVE_HOILDING_REGISTER _tMbusHoldingRegister;
       MONITORING_IE_GPR                       _tIndustrialEthernetGPR;

   } MONITORING_IE_SLAVE, *LPMONITORING_IE_SLAVE;
