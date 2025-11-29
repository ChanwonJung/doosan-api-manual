.. _app_weld_set_interface_eip_m2r_other:

app_weld_set_interface_eip_m2r_other
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1031)

.. code-block:: cpp

    bool app_weld_set_interface_eip_m2r_other(CONFIG_DIGITAL_WELDING_INTERFACE_OTHER pConfigdigitalweldinginterfacemonitoring)
    {
        return _app_weld_set_interface_eip_m2r_other(_rbtCtrl, pConfigdigitalweldinginterfacemonitoring);
    };

**Features**

This function configures the **communication interface** for using a welder that supports **EtherNet/IP communication**.  
It sets up the interface for **additional or custom data signals** that go **from the welder to the robot controller (M2R)**,  
beyond the standard monitoring or process data.  

You can define supplementary functions or signal mappings required for specialized welding control or feedback.

This configuration handles communication data sent **from the welder to the robot**,  
and the specific mapping should follow the signal datasheet provided by the welding equipment manufacturer.

**Note**

To properly use the EtherNet/IP-based welding interface, all **8 interface setting commands** must be configured:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`  
- :ref:`app_weld_set_interface_eip_r2m_option <app_weld_set_interface_eip_r2m_option>`  
- :ref:`app_weld_set_interface_eip_m2r_process2 <app_weld_set_interface_eip_m2r_process2>`  
- :ref:`app_weld_set_interface_eip_m2r_monitoring <app_weld_set_interface_eip_m2r_monitoring>`  
- :ref:`app_weld_set_interface_eip_m2r_other <app_weld_set_interface_eip_m2r_other>`  ← (this page)

**Arguments**

.. list-table::
   :widths: 28 28 12 32
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldinginterfacemonitoring
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_OTHER <struct_CONFIG_DIGITAL_WELDING_INTERFACE_OTHER>`
     - -
     - Digital welding interface **other** data configuration structure (M2R: Welder → Robot)

Each field within the structure defines a communication mapping parameter as shown below:

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
     - Data precision |br|
       (1: 0, 0.1: 1, 0.01: 2)
   * - _fMinData
     - float
     - -
     - Minimum data value
   * - _fMaxData
     - float
     - -
     - Maximum data value
   * - _nByteOffset
     - unsigned char
     - -
     - Communication data byte offset (1-255)
   * - _nBitOffset
     - unsigned char
     - -
     - Communication data bit offset (1-255)
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
     - Effective data size (bit)
   * - _nOption01~_nOption08
     - float
     - -
     - Vendor-specific extension fields (quality metrics, diagnostics, etc.)


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

    // Create a structure for defining EtherNet/IP M2R "Other" signals and assign values
    CONFIG_DIGITAL_WELDING_INTERFACE_OTHER otherData;

    otherData._bEnable        = 1;    // Enable other data interface
    otherData._nDataType      = 2;    // Continuous data (value type)
    otherData._nPositionNumber= 1;    // Decimal precision
    otherData._fMinData       = 0.0f;
    otherData._fMaxData       = 100.0f;
    otherData._nByteOffset    = 15;   // Byte position
    otherData._nBitOffset     = 0;    // Bit start position
    otherData._nCommDataType  = 4;    // 8-bit
    otherData._nMaxDigitSize  = 8;    // Effective data size (bit)

    // Example user-defined signals (for special welder functions)
    otherData._nOption01 = 0.3f;
    otherData._nOption02 = 0.3f;
    otherData._nOption03 = 0.3f;
    otherData._nOption04 = 0.3f;
    otherData._nOption05 = 0.3f;
    otherData._nOption06 = 0.3f;
    otherData._nOption07 = 0.3f;
    otherData._nOption08 = 0.3f;

    // Apply configuration
    bool result = Drfl.app_weld_set_interface_eip_m2r_other(otherData);

This example demonstrates how to configure **custom EtherNet/IP feedback channels** from the welder to the robot controller,  
allowing additional analog or status signals beyond the standard monitoring set.  
These fields are typically used for vendor-specific extensions such as custom welding quality metrics or torch diagnostics.
