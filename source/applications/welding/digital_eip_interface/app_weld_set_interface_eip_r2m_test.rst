.. _app_weld_set_interface_eip_r2m_test:

app_weld_set_interface_eip_r2m_test
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1021)

.. code-block:: cpp

    bool app_weld_set_interface_eip_r2m_test(CONFIG_DIGITAL_WELDING_INTERFACE_TEST pConfigdigitalweldinginterfacetest)
    {
        return _app_weld_set_interface_eip_r2m_test(_rbtCtrl, pConfigdigitalweldinginterfacetest);
    };

**Features**

This function configures the **EtherNet/IP test signal interface** for welders supporting EtherNet/IP communication.  
It defines the data mapping for **test or diagnostic signals** transmitted from the **robot controller → welder (R2M)**.  
This allows the robot to send diagnostic flags or calibration signals used for verifying communication and test cycles.

You may include additional test signal configurations using optional structure fields such as ``ts_opt1`` and ``ts_opt2``.  
Refer to the welder’s communication datasheet for detailed signal mapping and valid byte/bit assignments.

**Note**

For proper EtherNet/IP welding operation, all 8 communication interfaces should be configured:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>` ← (this page)  
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
   * - pConfigdigitalweldinginterfacetest
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_TEST <struct_CONFIG_DIGITAL_WELDING_INTERFACE_TEST>`
     - -
     - Digital welding interface test settings structure

**Structure Fields**

The following fields define the bit-level mapping for each EtherNet/IP test signal element:

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
     - Enable flag for the test signal |br|
       (0: Disabled, 1: Enabled)
   * - _nDataType
     - unsigned char
     - None
     - Data type |br| 
       (0: On/Off, 1: Selection, 2: Numeric value)
   * - _nPositionalNumber
     - unsigned char
     - None
     - Data digit position |br|
       (1:0, 0.1: 1, 0.01: 2)
   * - _fMinData
     - float
     - None
     - Minimum threshold value for signal validation
   * - _fMaxData
     - float
     - None
     - Maximum threshold value for signal validation
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
     - **Communication data size** |br|
       0: 1-bit(Disable Low) |br|
       1: 1-bit(Disable High) |br|
       2: 2-bit |br|
       3: 4-bit |br|
       4: 8-bit |br|
       5: 15-bit |br|
       6: 16-bit(short) |br|
       7: 32-bit(int)
   * - _bMaxDigitSize
     - unsigned char
     - None
     - Effective bit-length of the data

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

    // Example for setting EtherNet/IP test interface signals
    CONFIG_DIGITAL_WELDING_INTERFACE_TEST testData;

    testData._bEnable        = 1;    // Enable signal mapping
    testData._bDataType      = 0;    // Boolean signal type
    testData._bPositionalNumber = 1; // Single-bit signal
    testData._fMinData       = 0.0;
    testData._fMaxData       = 1.0;
    testData._bByteOffset    = 5;    // Located at byte 5
    testData._bBitOffset     = 3;    // Bit 3 in byte 5
    testData._bCommDataType  = 3;    // 8-bit field
    testData._bMaxDigitSize  = 1;    // Single-bit signal

    bool result = Drfl.app_weld_set_interface_eip_r2m_test(testData);

This example maps a **test signal** (e.g., “Arc Detection Test”) in the EtherNet/IP frame.  
It assigns the signal to byte position 5, bit 3, using a single-bit Boolean flag.  
Such test mappings are commonly used to verify digital communication between the robot controller and the connected welder before production welding begins.
