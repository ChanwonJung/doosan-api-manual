.. _tutorials_application_welding:

6.4.1 Welding Tutorials
===================================

The **Welding Tutorials** section provides examples for controlling welding applications  
using the Doosan Robotics API.  
It covers both **analog** and **digital** interfaces, along with **weaving** (oscillation) motion,  
parameter adjustment, and TCP calibration.

These examples demonstrate how to integrate the welding interface with a real robot motion sequence  
to achieve synchronized weld control.

**Tutorial Flow**

1. **Analog Welding Control** – Configure and adjust analog welding conditions.  
2. **Digital Welding Control (EtherNet/IP)** – Set up digital interface and process mapping.  
3. **Weaving Patterns** – Apply trapezoidal, zigzag, circular, or sinusoidal weaving motion.  
4. **Real-time Parameter Adjustment** – Modify welding conditions dynamically during operation.  
5. **Welding TCP Calibration** – Calibrate the welding tool center point (TCP).  
6. **Monitoring & Signal Output** – Monitor welding data and control digital welding signals.

---------------------------------------
Analog Welding Control
---------------------------------------

**Purpose**  |br|
Enable analog welding control interface and set base welding conditions  
such as voltage, current, and wire feed speed.

.. code-block:: cpp

   CONFIG_ANALOG_WELDING_INTERFACE analog_if{};
   CONFIG_ANALOG_WELDING_SETTING analog_set{};

   // Enable analog interface
   Drfl.app_weld_enable_analog(&analog_if);

   // Set analog welding condition
   analog_set._fVoltage = 22.5f;
   analog_set._fCurrent = 160.0f;
   analog_set._fWireFeedSpeed = 6.5f;
   Drfl.app_weld_set_weld_cond_analog(&analog_set);

**Check**  |br|
Analog interface is activated successfully,  
and the configured parameters (voltage/current/feed) are applied to the external welder.

---------------------------------------
Digital Welding Control (EtherNet/IP)
---------------------------------------

**Purpose**  |br|
Establish communication with the welder through EtherNet/IP  
and configure both R2M (Robot-to-Machine) and M2R (Machine-to-Robot) signals.

.. code-block:: cpp

   CONFIG_DIGITAL_WELDING_INTERFACE eip_if{};
   CONFIG_DIGITAL_WELDING_SETTING eip_set{};

   // Set up EtherNet/IP process interface
   Drfl.app_weld_set_interface_eip_r2m_process(&eip_if);
   Drfl.app_weld_set_interface_eip_m2r_monitoring(&eip_if);

   // Enable digital interface
   Drfl.app_weld_enable_digital(&eip_set);

**Check** |br| 
Digital interface activates successfully and EtherNet/IP connection status is valid.

---------------------------------------
Weaving Patterns
---------------------------------------

**Purpose** |br|
Configure and apply a weaving pattern (trapezoidal, zigzag, circular, or sinusoidal)  
to simulate weld bead oscillation.

.. code-block:: cpp

   CONFIG_TRAPEZOID_WEAVING_SETTING weave{};
   weave._fOffsetY = 2.0f;
   weave._fOffsetZ = 1.0f;
   weave._fWeavingWidth = 5.0f;
   weave._fWeavingCycle = 3.0f;

   Drfl.app_weld_weave_cond_trapezoidal(
       weave._fOffsetY, weave._fOffsetZ, 0.0f,
       weave._fWeavingWidth, weave._fWeavingCycle
   );

**Check**  |br|
The robot follows the configured oscillation pattern  
and maintains consistent bead width across the welding path.

---------------------------------------
Real-time Parameter Adjustment
---------------------------------------

**Purpose**  |br|
Adjust welding parameters dynamically during operation for adaptive control.

.. code-block:: cpp

   bool enable = true;
   float new_voltage = 23.0f;
   float new_current = 165.0f;
   float new_feed_speed = 7.0f;

   Drfl.app_weld_adj_welding_cond_analog(
       enable, false, new_voltage, new_current, new_feed_speed, 0.0f, 0.0f, 1.0f
   );

**Check**  |br|
Voltage/current/feed parameters update smoothly in real time  
without interrupting the welding process.

---------------------------------------
Welding TCP Calibration
---------------------------------------

**Purpose** |br| 
Calibrate the TCP (Tool Center Point) for accurate weld torch alignment.

.. code-block:: cpp

   CONFIG_WELDING_TCP tcp{};
   Drfl.measure_welding_tcp(&tcp);

**Check**  |br|
TCP measurement completes successfully,  
and the calibrated position matches the torch tip location.

---------------------------------------
Monitoring & Signal Output
---------------------------------------

**Purpose**  
Monitor welding data and control digital outputs for arc start/stop signals.

.. code-block:: cpp

   // Start monitoring
   Drfl.set_on_monitoring_welding_data(OnMonitoringWeldingData);

   // Control output signal
   Drfl.set_digital_welding_signal_output(GPIO_TOOL_DIGITAL_INDEX_2, TRUE);  // Arc start
   std::this_thread::sleep_for(std::chrono::seconds(2));
   Drfl.set_digital_welding_signal_output(GPIO_TOOL_DIGITAL_INDEX_2, FALSE); // Arc stop

**Check** |br| 
Monitoring callback provides real-time welding feedback,  
and the digital output toggles the external welder correctly.

.. note::
   - Welding tutorials require an external welding machine  
     (analog or digital EtherNet/IP) configured with the correct parameters.  
   - All welding operations must run under **Auto Mode** with **Servo ON**.  