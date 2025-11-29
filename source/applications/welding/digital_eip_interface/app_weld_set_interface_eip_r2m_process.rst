.. _app_weld_set_interface_eip_r2m_process:

app_weld_set_interface_eip_r2m_process
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1016)

.. code-block:: cpp

    bool app_weld_set_interface_eip_r2m_process(CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS pConfigdigitalweldinginterfaceprocess)
    {
        return _app_weld_set_interface_eip_r2m_process(_rbtCtrl, pConfigdigitalweldinginterfaceprocess);
    };

**Features**

This function configures the **EtherNet/IP communication interface** for welders that support EtherNet/IP connectivity.  
It sets up interlocking signals between the robot controller and the welder, defining how communication data is transmitted from the **robot controller → welder** (R2M: *Robot to Machine*).

This command must be used when setting up EtherNet/IP-based welding systems, allowing synchronized control signals such as welding start, robot ready, and error reset to be sent to the welder.  
Refer to the communication datasheet of the specific welder model for valid signal ranges and mapping rules.

**Note**

To properly enable EtherNet/IP communication with a welding system,  
**all eight** related interface setup functions must be configured:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>` ← (this page)
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`  
- :ref:`app_weld_set_interface_eip_r2m_option <app_weld_set_interface_eip_r2m_option>`  
- :ref:`app_weld_set_interface_eip_m2r_process2 <app_weld_set_interface_eip_m2r_process2>`  
- :ref:`app_weld_set_interface_eip_m2r_monitoring <app_weld_set_interface_eip_m2r_monitoring>`  
- :ref:`app_weld_set_interface_eip_m2r_other <app_weld_set_interface_eip_m2r_other>`

**Arguments**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldinginterfaceprocess
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS <struct_CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS>`
     - -
     - Refer to the structure definition and see below

**Structure Fields**

.. list-table::
   :widths: 25 15 15 45
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - welding_start
     - See below
     - See below
     - Welding start command signal (welder-specific mapping)
   * - robot_ready
     - 
     - 
     - Robot ready signal (welder-specific mapping)
   * - error_reset
     - 
     - 
     - Welder error reset (welder specific)

**Data Field Details**

The data fields within each signal structure (e.g., ``welding_start``, ``robot_ready``, ``error_reset``)  
have the following sub-parameters:

.. list-table::
   :widths: 22 18 15 45
   :header-rows: 1

   * - **Sub-field**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - _bEnable
     - unsigned char
     - None
     - Enable flag (0 = Disabled, 1 = Enabled)
   * - _nDataType
     - unsigned char
     - None
     - Data type (0 = off/on, 1 = selection, 2 = value)
   * - _nPositionalNumber
     - unsigned char
     - None
     - Data position index (1=0, 0.1 = 1, 0.01 = 2)
   * - _fMinData
     - float
     - None
     - Minimum data value
   * - _fMaxData
     - float
     - None
     - Maximum data value
   * - _nByteOffset
     - unsigned char
     - None
     - Communication byte location (1-255)
   * - _nBitOffset
     - unsigned char
     - None
     - Communication bit location (1-255)
   * - _nCommDataType
     - unsigned char
     - None
     - Communication data size |br|
       0: 1-bit(Disable Low) |br|
       1: 1-bit(Disable High) |br|
       2: 2-bit |br|
       3: 4-bit |br|
       4: 8-bit |br|
       5: 15-bit |br|
       6: 16-bit(short) |br|
       7: 32-bit(int)
   * - _nMaxDigitSize
     - unsigned char
     - None
     - Effective bit length for communication data

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

    CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS processSetting;

    // Welding Start Signal Mapping
    processSetting._WeldingStart._bEnable      = 1;
    processSetting._WeldingStart._bByteOffset  = 5;
    processSetting._WeldingStart._bBitOffset   = 3;
    processSetting._WeldingStart._bCommDataType = 4;  // 8-bit data

    // Robot Ready Signal Mapping
    processSetting._RobotReady._bEnable      = 1;
    processSetting._RobotReady._bByteOffset  = 8;
    processSetting._RobotReady._bBitOffset   = 0;
    processSetting._RobotReady._bCommDataType = 4;

    // Error Reset Signal Mapping
    processSetting._ErrorReset._bEnable      = 1;
    processSetting._ErrorReset._bByteOffset  = 10;
    processSetting._ErrorReset._bBitOffset   = 2;
    processSetting._ErrorReset._bCommDataType = 4;

    // Apply configuration
    bool result = Drfl.app_weld_set_interface_eip_r2m_process(processSetting);

This example maps the EtherNet/IP output channels for **welding start**, **robot ready**,  
and **error reset** signals. Each signal is assigned to a unique byte/bit position  
within the robot’s EtherNet/IP communication frame, allowing synchronized welding operations  
between the robot and the connected digital welder controller.
