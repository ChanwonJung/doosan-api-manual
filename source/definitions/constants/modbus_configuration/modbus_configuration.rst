.. _constants_modbus_configuration:

2.1.7 Modbus Configuration Constants
----------------------------------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **Name**
     - **Value**
     - **Description**
   * - MAX_MODBUS_BURST_SIZE
     - 32
     - Maximum number of Modbus registers processed in a single burst.
   * - MAX_MODBUS_SLAVE_DEVICES
     - 5
     - Maximum number of Modbus slave devices supported.
   * - MAX_MODBUS_REGISTER_PER_DEVICE
     - 50
     - Maximum number of registers that can be configured per Modbus slave device.
   * - MAX_MODBUS_SLAVE_TOTAL_GPR
     - 128
     - Maximum total number of global process registers across all Modbus slaves.
