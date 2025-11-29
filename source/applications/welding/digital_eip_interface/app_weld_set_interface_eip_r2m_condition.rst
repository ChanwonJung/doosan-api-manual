.. _app_weld_set_interface_eip_r2m_condition:

app_weld_set_interface_eip_r2m_condition
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1023)

.. code-block:: cpp

    bool app_weld_set_interface_eip_r2m_condition(CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION pConfigdigitalweldinginterfacecondition)
    {
        return _app_weld_set_interface_eip_r2m_condition(_rbtCtrl, pConfigdigitalweldinginterfacecondition);
    };

**Features**

This function configures the **EtherNet/IP communication interface** for welding systems that support EtherNet/IP connectivity.  
It defines the mapping of welding **condition control signals**—such as parameter adjustment, correction enablement, and condition synchronization—sent from the **robot controller → welder**.

This setup allows the welder to receive welding condition settings in real time (e.g., voltage correction, current correction, or synergic adjustments).  
Refer to the communication datasheet of the connected welding device for compatible condition parameters.

**Note**

To fully utilize EtherNet/IP-based welding functionality, all 8 related interface configuration commands must be set:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>` ← (this page)
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
   * - pConfigdigitalweldinginterfacecondition
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION <struct_CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION>`
     - -
     - EtherNet/IP condition mapping structure from robot to welder

**Structure Fields**

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
     - Enable flag for condition signal |br|
       (0: Disabled, 1: Enabled)
   * - _nDataType
     - unsigned char
     - None
     - Signal data type |br| 
       (0: On/Off, 1: Selection, 2: Value)
   * - _nPositionalNumber
     - unsigned char
     - None
     - Data digit |br|
       (1:0, 0.1:1, 0.01:2)
   * - _fMinData
     - float
     - None
     - Minimum reference value for parameter
   * - _fMaxData
     - float
     - None
     - Maximum reference value for parameter
   * - _nByteOffset
     - unsigned char
     - None
     - Communication byte offset (1-255)
   * - _nBitOffset
     - unsigned char
     - None
     - Communication bit offset (1-255)
   * - _nCommDataType
     - unsigned char
     - None
     - **Data size of the communication frame** |br|
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
     - Effective bit length used for condition data

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

    // Example: Configure EtherNet/IP welding condition mapping
    CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION conditionData;

    conditionData._bEnable        = 1;
    conditionData._bDataType      = 2;    // Value type signal
    conditionData._bPositionalNumber = 1; // Numeric position
    conditionData._fMinData       = -5.0; // Min correction (e.g., voltage)
    conditionData._fMaxData       = 5.0;  // Max correction (e.g., voltage)
    conditionData._bByteOffset    = 6;    // Located at byte 6
    conditionData._bBitOffset     = 0;    // Bit offset 0
    conditionData._bCommDataType  = 3;    // 8-bit field
    conditionData._bMaxDigitSize  = 8;    // 8-bit effective size

    bool result = Drfl.app_weld_set_interface_eip_r2m_condition(conditionData);

This example maps a welding condition signal to byte position 6 of the EtherNet/IP output frame.  
It allows the robot to transmit real-time **welding voltage or current correction values** to the welder,  
enabling adaptive condition control synchronized with the robot’s motion path.
