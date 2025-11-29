.. _manual_set_analog_output:

set_analog_output (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_analog_output <set_analog_output>` during **Manual (Teach)** operations  
to **output analog voltage or current signals** from the robot’s **control box analog output ports**  
for testing or calibration of connected devices.

**Typical usage**

- Send analog control signals (e.g., 0–10 V or 4–20 mA) to external devices such as **inverters**, **valves**, or **amplifiers**.  
- Test analog wiring and output scaling during system setup.  
- Manually tune device parameters (e.g., motor speed, torque reference) without running Auto programs.

.. Note::

    - The output range (e.g., **0–10 V** or **4–20 mA**) depends on the robot’s control box settings.

**Example: Set analog output to control an inverter or analog actuator**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Analog output configured and connected to an external device

       // 1) Set analog output channel 1 to 5.0 V
       bool ok1 = drfl.set_analog_output(ANALOG_OUT_CH1, 5.0f);
       std::printf("[Analog OUT CH1] Set to %.2f V : %s\n", 5.0f, ok1 ? "OK" : "FAILED");

       // 2) Set analog output channel 2 to 7.5 V
       bool ok2 = drfl.set_analog_output(ANALOG_OUT_CH2, 7.5f);
       std::printf("[Analog OUT CH2] Set to %.2f V : %s\n", 7.5f, ok2 ? "OK" : "FAILED");

       return 0;
   }

**Tips**

- Ensure the **output mode** (Voltage/Current) matches the external device specification.  
- Gradually increase the output to avoid sudden surges in external actuators.  
- If the output does not change, check control box analog configuration and wiring.  
- Use :ref:`get_analog_input <manual_get_analog_input>` to verify the signal via loopback testing.
