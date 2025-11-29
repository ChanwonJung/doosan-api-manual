.. _app_weld_enable_analog:

app_weld_enable_analog
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1010)

.. code-block:: cpp

    bool app_weld_enable_analog(CONFIG_ANALOG_WELDING_INTERFACE pConfiganalogweldinginterface)
    {
        return _app_weld_enable_analog(_rbtCtrl, pConfiganalogweldinginterface);
    };

**Features**

This function activates the **analog welding function**.  
It takes the connection and environmental configuration of the welding device, which can be connected via analog input/output and digital signal output, as input parameters.

The target welder must support the analog interface method and be able to receive target current and target voltage commands from the analog output channels of the connected controller.

**Analog Output Configuration**

- Set the channel number (1 or 2) and output mode (current/voltage) of the physically connected analog channel to ``ch_v_out`` and ``ch_f_out``, respectively.  
- The analog input/output range of the controller is **0–10 V** for voltage mode and **4–20 mA** for current mode.  
- Ensure that the setting mode and output range for each channel are compatible with the input specifications and range of the welder.

  - For example, if the welder’s target voltage input range is 0–10 V, set the controller output channel to voltage mode (0–10 V output).  
  - If the welder requires 2–15 V input, set the controller to current mode (4–20 mA output) and connect a 75 Ω resistor to achieve ~3–15 V output range.  
    (Note that voltage below 2 V cannot be commanded.)

- Configure as much of the input range as possible to match the welder’s specification.  
- Set the maximum/minimum analog output range of both controller and welder in ``spec_v_out`` and ``spec_f_out``.  

  *spec_v_out / spec_f_out* values: |br|

  - [0] = WO_min  
  - [1] = CO_min  
  - [2] = WO_max  
  - [3] = CO_max  

  where **WO_min**, **WO_max** = welder’s min/max output specs,  
  and **CO_min**, **CO_max** = controller’s analog output values for those specs.

**Welding Current and Monitoring**

- The welding current output varies depending on wire feed speed, base material, and welding type.  
- Check the output using either the welder’s own monitoring or an external current sensor.  
- For voltage/current measurement, connect an analog input channel (``ch_v_in``, ``ch_c_in``).  
- Define the analog input range of both controller and sensor in ``spec_v_in`` and ``spec_c_in``.

  *spec_v_in / spec_c_in* values: |br|

  - [0] = SI_min  
  - [1] = CI_min  
  - [2] = SI_max  
  - [3] = CI_max  

  where **SI_min**, **SI_max** = sensor measurement range (min/max),  
  and **CI_min**, **CI_max** = controller input values for those ranges.

**Digital Signal Configuration**

- Set channel numbers for the following digital I/O signals:  

  - **ARC-ON/OFF** (start/end of welding output)  
  - **GAS-ON/OFF** (gas output start/end)  
  - **INCHING-Forward-ON/OFF** (forward wire feed start/end)  
  - **INCHING-Backward-ON/OFF** (reverse wire feed start/end)  
  - **BlowOut-ON/OFF** (torch cleaning gas start/end)  

- Other signals can be selectively configured depending on the welder’s supported functions.

**Arguments**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfiganalogweldinginterface
     - :ref:`CONFIG_ANALOG_WELDING_INTERFACE <struct_CONFIG_ANALOG_WELDING_INTERFACE>`
     - -
     - Analog welding interface structure

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

    // Define CONFIG_ANALOG_WELDING_INTERFACE
    CONFIG_ANALOG_WELDING_INTERFACE config;
    config._bMode = 1;   // Start mode

    // Target Voltage Configuration
    config._fTargetVoltage._iChannel = 1;
    config._fTargetVoltage._iChannelType = 1;   // Voltage
    config._fTargetVoltage._fSetRatio = 0.06;
    config._fTargetVoltage._fMinOutput = 0.0;
    config._fTargetVoltage._fMaxOutput = 200.0;

    // Feeding Speed Configuration
    config._fFeedingSpeed._iChannel = 1;
    config._fFeedingSpeed._iChannelType = 0;    // Current
    config._fFeedingSpeed._fSetRatio = 0.06;
    config._fFeedingSpeed._fMinOutput = 0.0;
    config._fFeedingSpeed._fMaxOutput = 100.0;

    // Welding Voltage Configuration
    config._fWeldingVoltage._iChannel = 1;
    config._fWeldingVoltage._iChannelType = 1;  // Voltage
    config._fWeldingVoltage._fSetRatio = 0.06;
    config._fWeldingVoltage._fMinOutput = 0.0;
    config._fWeldingVoltage._fMaxOutput = 200.0;

    // Welding Current Configuration
    config._fWeldingCurrent._iChannel = 1;
    config._fWeldingCurrent._iChannelType = 0;  // Current
    config._fWeldingCurrent._fSetRatio = 0.06;
    config._fWeldingCurrent._fMinOutput = 0.0;
    config._fWeldingCurrent._fMaxOutput = 100.0;

    // Other Configuration
    config._iGASOnCh = 1;
    config._iInchingFCh = 1;
    config._iInchingBCh = 1;
    config._iBlowOutCh = 1;

    // Enable Analog Welding Function
    Drfl.app_weld_enable_analog(config);

This example activates the analog welding mode by defining all analog channel and signal configurations.  
It enables the controller to send real-time voltage/current commands and receive sensor feedback  
for precise analog welding control and dynamic process monitoring.
