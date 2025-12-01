.. _app_weld_set_interface_eip_m2r_process2:

app_weld_set_interface_eip_m2r_process2
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1027)

.. code-block:: cpp

    bool app_weld_set_interface_eip_m2r_process2(CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2 pConfigdigitalweldinginterfaceprocess2)
    {
        return _app_weld_set_interface_eip_m2r_process2(_rbtCtrl, pConfigdigitalweldinginterfaceprocess2);
    };

**Features**

This function configures the communication interface for using a welder that supports **EtherNet/IP communication**.  
It defines the interlocking signals transmitted **from the welder to the robot controller**, specifically for **“Process 2” signals**.  
This setup enables synchronization between the welding device's execution states and the robot motion sequence.

Refer to the communication signal datasheet of the corresponding welder for precise signal mapping details.

**Note**

To properly use the EtherNet/IP-based welding function, all **8 interface setup functions** must be configured:

- :ref:`app_weld_set_interface_eip_r2m_process <app_weld_set_interface_eip_r2m_process>`  
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`  
- :ref:`app_weld_set_interface_eip_r2m_test <app_weld_set_interface_eip_r2m_test>`  
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`  
- :ref:`app_weld_set_interface_eip_r2m_option <app_weld_set_interface_eip_r2m_option>`  
- :ref:`app_weld_set_interface_eip_m2r_process2 <app_weld_set_interface_eip_m2r_process2>`  ← (this page)  
- :ref:`app_weld_set_interface_eip_m2r_monitoring <app_weld_set_interface_eip_m2r_monitoring>`  
- :ref:`app_weld_set_interface_eip_m2r_other <app_weld_set_interface_eip_m2r_other>`

- **Robot motion start** is interlocked with the *current_flow* signal from the welder.  
  When the *main_current* item is active, it synchronizes instead with that signal.  
- **Robot motion end** is also interlocked with *current_flow*, unless the *process_active* signal is used,  
  in which case the motion completion is synchronized with *process_active* instead.

**Arguments**

.. list-table::
   :widths: 28 28 12 32
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldinginterfaceprocess2
     - :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2 <struct_CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2>`
     - -
     - Digital welding interface "Process 2" settings structure

**Structure Fields**

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
     - Data type: |br|
       (0: off/on, 1: selection, 2: value)
   * - _nPositionalNumber
     - unsigned char
     - -
     - Data digit representation |br|
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
     - Byte index in EtherNet/IP M2R communication map (1-255)
   * - _nBitOffset
     - unsigned char
     - -
     - Bit index (1-255)
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
     - Effective bit width of signal data

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

    // Create and assign EIP M2R Process2 configuration
    CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2 processData;

    processData._bEnable         = 1;    // Enable signal mapping
    processData._bDataType       = 0;    // On/Off type
    processData._bPositionalNumber = 1;  // Data digit position
    processData._fMinData        = 0.0;  // Minimum data (OFF)
    processData._fMaxData        = 1.0;  // Maximum data (ON)
    processData._bByteOffset     = 5;    // Located at byte index 5
    processData._bBitOffset      = 2;    // Bit offset 2
    processData._bCommDataType   = 3;    // 8-bit
    processData._bMaxDigitSize   = 8;    // Bit width = 8

    // Example signal interlocks
    processData._bCurrentFlow    = 1;    // Welding current flowing signal
    processData._bProcessActive  = 1;    // Active process flag
    processData._bArcReady       = 1;    // Welder ready signal
    processData._bTorchReady     = 1;    // Torch safety interlock

    bool result = Drfl.app_weld_set_interface_eip_m2r_process2(processData);

This example defines EtherNet/IP M2R Process 2 communication mapping,  
assigning welder-to-robot feedback signals (e.g., current flow, process active, and torch ready).  
These signals are used to synchronize the robot's motion sequence with the welder’s operating state during real-time execution.
