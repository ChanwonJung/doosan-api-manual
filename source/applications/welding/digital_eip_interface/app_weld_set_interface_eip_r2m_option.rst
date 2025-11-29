.. _app_weld_set_interface_eip_r2m_option:

app_weld_set_interface_eip_r2m_option
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1025)

.. code-block:: cpp

    bool app_weld_set_interface_eip_r2m_option(CONFIG_DIGITAL_WELDING_INTERFACE_OPTION pConfigdigitalweldinginterfaceoption)
    {
        return _app_weld_set_interface_eip_r2m_option(_rbtCtrl, pConfigdigitalweldinginterfaceoption);
    };

**Features**

This function configures the communication interface for using a welder that supports EtherNet/IP communication.  
It allows you to set up **additional option functions** required beyond the default settings provided by the following commands:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`

This configuration involves communication data that is sent from the **robot controller to the welder**.  
Refer to the communication signal datasheet of the corresponding welder for details related to the settings below.

**Note**

To properly use the welding function with an EtherNet/IP communication-capable welder, **all 8 types** of interface setting commands must be configured:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`  
- :ref:`app_weld_set_interface_eip_r2m_option <app_weld_set_interface_eip_r2m_option>`  ← (this page)  
- :ref:`app_weld_set_interface_eip_m2r_process2 <app_weld_set_interface_eip_m2r_process2>`  
- :ref:`app_weld_set_interface_eip_m2r_monitoring <app_weld_set_interface_eip_m2r_monitoring>`  
- :ref:`app_weld_set_interface_eip_m2r_other <app_weld_set_interface_eip_m2r_other>`

**Arguments**

.. list-table::
   :widths: 28 28 12 32
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldinginterfaceoption
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_OPTION <struct_CONFIG_DIGITAL_WELDING_INTERFACE_OPTION>`
     - -
     - Digital welding interface **option** structure (R2M: Robot → Welder)

The data type, default value, and description of the arguments **within the structure** are the same as below:

.. list-table::
   :widths: 26 18 18 38
   :header-rows: 1

   * - **Argument Name**
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
     - Signal data type |br|
       (0: off/on, 1: selection, 2: value)
   * - _nPositionNumber
     - unsigned char
     - -
     - Data digit representation |br|
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
     - Communication data location (byte): 1-255
   * - _nBitOffset
     - unsigned char
     - -
     - Communication data location (bit): 1-255
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

    // Create a structure for setting EIP R2M option data and set values.
    CONFIG_DIGITAL_WELDING_INTERFACE_OPTION optionData;

    optionData._bEnable        = 1;     // use option
    optionData._nDataType      = 2;     // value type
    optionData._nPositionNumber= 1;     // 0.0 format
    optionData._fMinData       = 0.0f;
    optionData._fMaxData       = 100.0f;
    optionData._nByteOffset    = 1;     // byte position in R2M area
    optionData._nBitOffset     = 0;     // bit offset (if bit type)
    optionData._nCommDataType  = 3;     // 8-bit
    optionData._nMaxDigitSize  = 8;

    // Vendor-specific option fields (example: _nOption01 ~ _nOption16)
    optionData._nOption01 = 0.3f;
    optionData._nOption02 = 0.3f;
    optionData._nOption03 = 0.3f;
    optionData._nOption04 = 0.3f;
    optionData._nOption05 = 0.3f;
    optionData._nOption06 = 0.3f;
    optionData._nOption07 = 0.3f;
    optionData._nOption08 = 0.3f;
    optionData._nOption09 = 0.3f;
    optionData._nOption10 = 0.3f;
    optionData._nOption11 = 0.3f;
    optionData._nOption12 = 0.3f;
    optionData._nOption13 = 0.3f;
    optionData._nOption14 = 0.3f;
    optionData._nOption15 = 0.3f;
    optionData._nOption16 = 0.3f;

    // Call
    bool result = Drfl.app_weld_set_interface_eip_r2m_option(optionData);

This example enables an option block for an EtherNet/IP welder, maps it into the R2M area,  
and fills vendor-defined option slots (``_nOption01 ~ _nOption16``).  
Consult your welder's signal map to set the correct byte/bit offsets and data size.
