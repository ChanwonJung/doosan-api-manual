.. _app_weld_set_interface_eip_r2m_mode:

app_weld_set_interface_eip_r2m_mode
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1018)

.. code-block:: cpp

    bool app_weld_set_interface_eip_r2m_mode(CONFIG_DIGITAL_WELDING_INTERFACE_MODE pConfigdigitalweldinginterfacemode)
    {
        return _app_weld_set_interface_eip_r2m_mode(_rbtCtrl, pConfigdigitalweldinginterfacemode);
    };

**Features**

This function configures the **EtherNet/IP communication interface** for a welder that supports EtherNet/IP connectivity.  
It defines the communication signals related to **welding mode selection**, transmitted from the **robot controller → welder**.  

Through this interface, the robot can command welding mode changes such as process type or welding program number, ensuring that the robot and welder remain synchronized.

You may add additional welding mode selection signals through the optional parameter field ``wm_opt1`` within the structure.  
Refer to the welder manufacturer's EtherNet/IP signal documentation for detailed mode mapping.

**Note**

To fully configure an EtherNet/IP-based welding system, the following 8 interface setup commands must all be configured:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>` ← (this page)
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
   * - pConfigdigitalweldinginterfacemode
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_MODE <struct_CONFIG_DIGITAL_WELDING_INTERFACE_MODE>`
     - -
     - Structure for EtherNet/IP digital mode configuration from robot to welder

**Structure Fields**

The configuration structure defines the data mapping parameters for each EtherNet/IP output item:

.. list-table::
   :widths: 22 18 15 45
   :header-rows: 1

   * - **Field Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - _bEnable
     - unsigned char
     - None
     - Enable flag |br|
       (0: Disabled, 1: Enabled)
   * - _bDataType
     - unsigned char
     - None
     - Data type |br| 
       (0: On/Off, 1: Selection, 2: Numeric value)
   * - _bPositionalNumber
     - unsigned char
     - None
     - Position number digit (e.g., 1.0, 0.1, 0.01)
   * - _fMinData
     - float
     - None
     - Minimum value for the communication parameter
   * - _fMaxData
     - float
     - None
     - Maximum value for the communication parameter
   * - _bByteOffset
     - unsigned char
     - None
     - Byte offset in the communication frame (1-255)
   * - _bBitOffset
     - unsigned char
     - None
     - Bit offset in the communication frame (1-255)
   * - _bCommDataType
     - unsigned char
     - None
     - **Communication data size** |br|
       0: 1-bit (Low/High) |br|
       1: 2-bit |br|
       2: 4-bit |br|
       3: 8-bit |br|
       4: 16-bit |br|
       5: 32-bit (int/float)
   * - _bMaxDigitSize
     - unsigned char
     - None
     - Effective data size in bits

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

    // Create a structure for EtherNet/IP mode configuration
    CONFIG_DIGITAL_WELDING_INTERFACE_MODE modeData;

    // Enable mode communication
    modeData._bEnable = 1;

    // Define byte/bit mapping for the mode selection signal
    modeData._bByteOffset   = 8;   // Byte position in EIP frame
    modeData._bBitOffset    = 1;   // Bit offset
    modeData._bCommDataType = 3;   // 8-bit communication
    modeData._bDataType     = 2;   // Mode type: numeric value
    modeData._fMinData      = 0.0;
    modeData._fMaxData      = 10.0; // Mode value range 0–10

    // Apply the EtherNet/IP welding mode configuration
    bool result = Drfl.app_weld_set_interface_eip_r2m_mode(modeData);

This example defines a welding **mode selection signal** over EtherNet/IP,  
where an 8-bit data field (byte 8, bit 1) is used to transmit a numeric process ID from the robot controller to the welder.  
Such mapping allows flexible control of welding programs, such as switching between **TIG/MIG/MAG** modes directly from the robot program.
