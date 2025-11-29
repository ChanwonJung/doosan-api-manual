.. _manual_get_analog_input:

get_analog_input (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_analog_input <get_analog_input>` during **Manual (Teach)** operations  
to **read analog voltage or current values** from the robot’s **control box analog input ports**  
when using API version **DRCF_VERSION == 2**.

**Typical usage**

- Monitor **external sensors or potentiometers** connected to control box analog inputs.  
- Verify **signal levels (0–10 V or 4–20 mA)** during wiring inspection or manual calibration.  
- Check feedback from an analog device (e.g., pressure, torque, distance) before automation setup.

.. Note::

    - Range and scaling are defined by **control box settings** (check teach pendant → I/O → Analog).  

**Example: Read analog input voltage from control box**

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
       // - Control box analog input connected to voltage or sensor signal

       // 1) Read CH1 analog value
       float value_ch1 = drfl.get_analog_input(ANALOG_IN_CH1);
       std::printf("[Analog CH1] = %.3f V\n", value_ch1);

       // 2) Read CH2 analog value
       float value_ch2 = drfl.get_analog_input(ANALOG_IN_CH2);
       std::printf("[Analog CH2] = %.3f V\n", value_ch2);

       return 0;
   }

**Tips**

- Ensure correct **input mode (Voltage/Current)** is configured on the controller.  
- If readings are unstable, add a short delay between reads (e.g., 100 ms).  
