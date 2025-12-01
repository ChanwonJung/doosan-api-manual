1.1.2 History of Document Creation/Revision
---------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 70 15

   * - **Revision No.**
     - **Creation / Revision Pages and Contents**
     - **Revision Date**

   * - 1.33.1
     - Update API Manual to Sphinx Theme |br| |br|

       Modify version information: GL013301 |br| |br|

       **Update Features**

       - Support for Ubuntu 24.04 Version
       - Added Tutorial (Chapter 6)
       - Added TroubleShooting (Chapter 7)
       - Restructing of the API navigation tree

       **Updated Functions**
       
       - Added missing functions
       - Added DH parameter function: ``get_robot_link_info``

       **Update Definition**

       - Added missing Structures
       - Added DH paramter Structure: ``ROBOT_LINK_INFO``
     - 2025.12.01
   * - 1.33
     - Modify version information: GL013300 |br| |br|
       **Update Features**

       - All Auto modes are modified to switch to move (light-up) mode during safety events.
       - Fixed the issue where force control monitoring within Monitoring was not displaying correctly.
       - Updated ``flange_serial`` command for Flange Version rev2.

       **Updated Functions**

       - Added LED control functions:

         - ``state_led_reset``
         - ``set_state_led_off``
         - ``set_state_led_color``
         - ``get_state_led_rule``
       - I/O Control Functions:

         - ``flange_serial_open``
         - ``flange_serial_close``
     - 2025-09-03

   * - 1.32
     - **Update Features**

       - Add welding-related APIs

       **Update Definition**

       - Add multiple structs:

         - ``ROBOT_WELDING_DATA``
         - ``WELDING_CHANNEL``
         - ``CONFIG_WELDING_INTERFACE``
         - ``CONFIG_WELD_SETTING``
         - ``GET_WELDING_SETTING_RESPONSE``
         - ``ADJUST_WELDING_SETTING``
         - ``CONFIG_TRAPEZOID_WEAVING_SETTING`` 
         - ``CONFIG_ZIGZAG_WEAVING_SETTING``
         - ``CONFIG_CIRCULAR_WEAVING_SETTING``
         - ``CONFIG_SINE_WEAVING_SETTING``
         - ``CONFIG_WELDING_DETAIL_INFO``
         - ``CONFIG_ANALOG_WELDING_INTERFACE``
         - ``CONFIG_ANALOG_WELDING_SETTING``
         - ``ANALOG_WELDING_ADJUST_SETTING``
         - ``CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA``
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS``
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_MODE``
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_TEST`` 
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION``
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_OPTION``
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2``
         - ``CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING``
         - ``DIGITAL_WELDING_RESET``
         - ``CONFIG_DIGITAL_WELDING_MODE``
         - ``CONFIG_DIGITAL_WELDING_CONDITION``
         - ``CONFIG_DIGITAL_WELDING_ADJUST``
         - ``MEASURE_TCP_WELDING``
         - ``TACK_WELDING_SETTING``
         - ``DIGITAL_FORCE_WRITE_DATA``
         - ``ROBOT_DIGITAL_WELDING_DATA``
         - ``DIGITAL_WELDING_COMM_STATE``

       **Update Functions**

       - Add monitoring functions:

         - ``set_on_monitoring_welding_data``
         - ``set_on_monitoring_analog_welding_data``
         - ``set_on_monitoring_digital_welding_data``

       - Add weaving functions:

         - ``app_weld_weave_cond_trapezoidal``
         - ``app_weld_weave_cond_zigzag``
         - ``app_weld_weave_cond_circular``
         - ``app_weld_weave_cond_sinusoidal``

       - Add analog interface functions:

         - ``app_weld_enable_analog``
         - ``app_weld_set_weld_cond_analog``
         - ``app_weld_adj_welding_cond_analog``

       - Add Ethernet/IP functions:

         - ``app_weld_set_interface_eip_m2r_process``
         - ``app_weld_set_interface_eip_r2m_mode``
         - ``app_weld_set_interface_eip_r2m_process``
         - ``app_weld_set_interface_eip_r2m_test``
         - ``app_weld_set_interface_eip_r2m_condition``
         - ``app_weld_set_interface_eip_r2m_option``
         - ``app_weld_set_interface_eip_m2r_process2``
         - ``app_weld_set_interface_eip_m2r_monitoring``
     - 2024-01-15

   * - 1.31
     - **Update Features**

       - Add option of Controller (``#define DRCF_VERSION``)

       **Update Definition**

       - Add ``MONITORING_CTRLIO_EX2``
       - Add ``READ_CTRLIO_INPUT_EX2``
       - Add ``READ_CTRLIO_OUTPUT_EX2``
       - Update ``GPIO_CTRLBOX_DIGITAL_INDEX`` for v3 controller
       - Add ``SAFETY_CONFIGURATION_EX2_V3``

       **Update Functions**

       - Update ``get_safety_configuration_ex``
       - Update ``get_safety_configuration`` (new feature)
       - Remove ``SetOnMonitoringData`` (duplicate)
       - Remove ``SetOnMonitoringCtrlIO`` (duplicate)
     - 2024-12-03

   * - 1.30
     - **Update Features**

       - Add Arm64 Drfl Binary
       - Support for Ubuntu 22.04 Version
       - Improve Realtime Performance
       - Fix Blending Motion Related Issues
       - Change return value of ``flange_serial_read``

       **Update Definition**

       - Add enums: ``MOVE_ORIENTATION``, ``SPIRAL_DIR``, ``ROT_DIR``, ``DR_SERVOJ_TYPE``
       - Add structs: ``SAFETY_CONFIGURATION_EX2``, ``CONFIG_SAFETY_IO_OP``
       - Add parameters for adjusting speed/acceleration of each axis in ``movej``
       - Add extended ``movejx``, ``amovej``, ``amovejx``, ``servoj``

       **Update Functions**

       - Add ``get_safety_configuration (Extension)``
       - Update ``ikin (Add_iter_threshold)``, ``ikin_norm``
       - Update ``movec (Extension)``, ``amovec (Extension)``
       - Update ``move_spiral (Extension)``, ``amove_spiral (Extension)``, ``servoj (Extension)``
     - 2024-11-27

   * - 1.29
     - Add ``query_modbus_data_list``
     - 2023-03-24

   * - 1.28
     - Fix ``enum.ROBOT_STATE`` description |br| |br|
       Add contents of ``enum.ROBOT_MODE`` |br| |br|
       Delete duplicate ``enum.ROBOT_SPACE`` |br| |br|
       Add ``set_palletizing_mode`` command |br| |br|
       Add ``move_home`` notice
     - 2023-02-20

   * - 1.27
     - Fixed ``drl_stop`` function parameter: ``enum.STOP_TYPE → unsigned char``
     - 2022-07-04

   * - 1.26
     - Fixed ``enum.CONTROL_SPACE`` |br| |br|
       Fixed ``set_on_monitoring_safety_state`` |br| |br|
       Fixed ``enum.MOVE_REFERENCE`` |br| |br|
       Fixed ``change_operation_speed`` |br| |br|
       Fixed ``TOnRobotSystemCB`` |br| |br|

       **Update Functions**

       - Add new property functions

         - ``get_current_posj``
         - ``get_control_space``
         - ``get_current_velj``
         - ``get_desired_posj``
         - ``get_current_tool_flange_posx``
         - ``get_current_velx``
         - ``get_desired_velx``
         - ``get_joint_torque``
         - ``get_external_torque``
         - ``get_tool_force``

       - Add Enums/Structs

         - Add ``enum.ROBOT_SPACE``
         - Add ``struct.ROBOT_VEL`` / ``struct.ROBOT_FORCE``
     - 2022-06-02

   * - 1.25
     - Delete ``port`` parameter in ``flange_serial_open / close`` |br| |br|
       Add cause sentence for ``set_tool`` / ``set_workpiece_weight`` function
     - 2022-05-04

   * - 1.24
     - Edited content related to ``enum.SAFETY_MODE_EVENT`` |br| |br|
       Fixed parameter in ``set_safety_mode`` example |br| |br|
       Add ``port`` parameter to ``flange_serial`` related command (specify available for new flange) |br| |br|
       Change version → GL010115 |br| |br|

       **Update Functions**

       - Add new functions

         - ``set_workpiece_weight``
         - ``set_mode_tool_analog_input``
         - ``set_tool_digital_output_type``
         - ``set_tool_digital_output_level``
         - ``get_tool_analog_input``

       - Add enums

         - ``COG_REFERNCE``
         - ``ADD_UP``
         - ``OUTPUT_TYPE``
     - 2022-04-29

   * - 1.23
     - 3.3.21: Change the argument part ``TOnMonitoringSafetyState`` → ``TOnMonitoringSafetyStateCB`` |br| |br|
       3.7.14: Argument part ``TYPE_TYPE`` → change to ``DATA_TYPE`` |br| |br|
       3.8.11 Modify the argument to enum → ``enum.MODBUS_REGISTER_TYPE`` |br| |br|
       
       **Update Definition**

       - Add enums: ``SAFETY_MODE / SAFETY_EVENT``, ``COORDINATE_SYSTEM``
       - Add structs: ``struct.MESSAGE_PROGRESS``
       - Resolve enum constant ``ROBOT_STATE`` notation error
       
       **Update Functions**

       - Delete ``get_override_speed``

       **Update Features**

       - Add realtime control
     - 2022-03-10

   * - 1.2
     - Modify version information: GL010112 |br| |br|

       **Add new functions**

       - ``set_safety_mode``
       - ``set_on_monitoring_state``
       - Add new function for real-time control (refer to the other manual).

     - 2021-12-16

   * - 1.19
     - Modify version information: GL010112 |br| |br|

       **Add new functions**

       - ``ikin (extension)``
       - ``set_monitoring_robot_system``
       - ``change_collision_detection``
       - ``add_sw_module``
       - ``del_sw_module``
       - ``update_sw_module``
       - ``release_protective_stop``
       - ``set_on_monitoring_update_module``
     - 2021-11-22

   * - 1.18
     - Modify version information: GL010111 |br| |br|

       **Add new function** : ``get_override_speed``
     - 2021-09-15

   * - 1.17
     - Modify version information: GL010110
     - 2021-06-09

   * - 1.16
     - **Add missing function** : ``servo_off``
     - 2021-03-24

   * - 1.15
     - **Add missing functions** : ``set_user_home`` / ``Flange_serial_read`` parameter added (timeout)
     - 2021-03-19

   * - 1.14
     - **Correction of typos / Correction of some functions** : ``movesj``, ``set_safe_stop_reset_type``, ``close_connection`` etc.
     - 2020-10-19

   * - 1.13
     - **Add functions** : ``flange_serial`` etc.
     - 2020-10-19

   * - 1.12
     - Split the header (add ``DRFLEx`` class)
     - 2020-06-08

   * - 1.11
     - Update function name (DRL style)
     - 2020-05-28

   * - 1.1
     - Update new commands
     - 2020-05-20

   * - 1.0
     - Initial Creation and Distribution
     - 2018-06-29
