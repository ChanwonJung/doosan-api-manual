.. _constants_motion_configuration_size:

2.1.6 Motion / Configuration Size Limits
----------------------------------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **Name**
     - **Value**
     - **Description**
   * - MAX_MODBUS_TOTAL_REGISTERS
     - 100
     - Maximum total number of Modbus registers that can be managed.
   * - MAX_MOVEB_POINT
     - 50
     - Maximum number of via-points for blended motion (``moveb``).
   * - MAX_SPLINE_POINT
     - 100
     - Maximum number of points for spline-based motion (``movesj``, ``movesx``).
   * - MAX_SERIAL
     - 32
     - Maximum number of serial ports or configurations tracked.
   * - MAX_CONFIG_TCP_SIZE
     - 50
     - Maximum number of TCP configuration entries that can be stored.
   * - MAX_CONFIG_TOOL_SIZE
     - 50
     - Maximum number of tool configuration entries that can be stored.
   * - MAX_USER_COORD_MONITORING_EXT_FORCE_SIZE
     - 10
     - Maximum number of user coordinates monitored for external force.
   * - NUM_REMOTE_CONTROL
     - 8
     - Number of remote control channels supported.