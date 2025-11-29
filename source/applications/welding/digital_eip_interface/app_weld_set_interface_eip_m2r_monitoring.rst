.. _app_weld_set_interface_eip_m2r_monitoring:

app_weld_set_interface_eip_m2r_monitoring
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1029)

.. code-block:: cpp

    bool app_weld_set_interface_eip_m2r_monitoring(CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING pConfigdigitalweldinginterfacemonitoring)
    {
        return _app_weld_set_interface_eip_m2r_monitoring(_rbtCtrl, pConfigdigitalweldinginterfacemonitoring);
    };

**Features**

This function configures the communication interface for a welder that supports **EtherNet/IP communication**.  
It sets up the interface related to **welding status monitoring** among the communication data sent **from the welder to the robot controller**.  
This function is essential for receiving feedback signals like current, voltage, and fault states from the welder in real time.

Refer to the communication signal datasheet of the corresponding welder for specific byte and bit mapping details.

**Note**

To properly use the EtherNet/IP welding interface, all **8 configuration commands** must be defined:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`  
- :ref:`app_weld_set_interface_eip_r2m_option <app_weld_set_interface_eip_r2m_option>`  
- :ref:`app_weld_set_interface_eip_m2r_process2 <app_weld_set_interface_eip_m2r_process2>`  
- :ref:`app_weld_set_interface_eip_m2r_monitoring <app_weld_set_interface_eip_m2r_monitoring>`  ← (this page)  
- :ref:`app_weld_set_interface_eip_m2r_other <app_weld_set_interface_eip_m2r_other>`

**Arguments**

.. list-table::
   :widths: 28 28 12 32
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldinginterfacemonitoring
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING <struct_CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING>`
     - -
     - Digital welding interface **monitoring** structure (M2R: Welder → Robot)

The data type, default value, and description of each field within the structure are as follows:

.. list-table::
   :widths: 26 18 18 38
   :header-rows: 1

   * - **Field Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - _bEnable
     - unsigned char
     - -
     - Enable flag |br|
       (0: Disabled, 1: Enabled)
   * - _nDataType
     - unsigned char
     - -
     - Data type |br|
       (0: off/on, 1: selection, 2: value)
   * - _nPositionNumber
     - unsigned char
     - -
     - Data digit precision |br|
       (1: 0, 0.1: 1, 0.01: 2)
   * - _fMinData
     - float
     - -
     - Minimum signal data range
   * - _fMaxData
     - float
     - -
     - Maximum signal data range
   * - _nByteOffset
     - unsigned char
     - -
     - Byte offset in the EtherNet/IP monitoring map (1-255)
   * - _nBitOffset
     - unsigned char
     - -
     - Bit offset (1-255)
   * - _nCommDataType
     - unsigned char
     - -
     - **Communication data size** |br|
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
     - -
     - Effective data bit length

**Return**

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

    // Creating a structure for EIP M2R monitoring configuration
    CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING monitoringData;

    // Assign monitoring parameters from welder to robot
    monitoringData._bEnable        = 1;      // Enable feedback data mapping
    monitoringData._nDataType      = 2;      // Continuous data (value type)
    monitoringData._nPositionNumber= 1;      // Decimal precision
    monitoringData._fMinData       = 0.0f;
    monitoringData._fMaxData       = 100.0f;
    monitoringData._nByteOffset    = 10;     // Byte position in monitoring data block
    monitoringData._nBitOffset     = 0;      // Start bit
    monitoringData._nCommDataType  = 5;      // 16-bit (for analog current/voltage)
    monitoringData._nMaxDigitSize  = 16;

    // Example feedback items
    monitoringData._bWeldingCurrent   = 1;   // Current feedback signal
    monitoringData._bWeldingVoltage   = 1;   // Voltage feedback signal
    monitoringData._bWireFeedSpeed    = 1;   // Wire feed speed
    monitoringData._bErrorFlag        = 1;   // Welding error detection
    monitoringData._bErrorNumber      = 1;   // Error code output

    // Apply configuration to robot controller
    bool result = Drfl.app_weld_set_interface_eip_m2r_monitoring(monitoringData);

This example demonstrates how to configure the **M2R (Monitoring)** interface  
for real-time EtherNet/IP feedback from a welding machine, including current, voltage,  
wire feed speed, and error information signals transmitted to the robot controller.
