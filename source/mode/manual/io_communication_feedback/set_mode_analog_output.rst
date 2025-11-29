.. _manual_set_mode_analog_output:

set_mode_analog_output (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_mode_analog_output <set_mode_analog_output>` during **Manual (Teach)** operations  
to **configure the signal type** (Voltage or Current) of the **control box analog output channels**.

**Typical usage**

- Select whether each analog output channel outputs **voltage (0–10 V)** or **current (4–20 mA)** signals.  
- Match the robot’s analog output mode with the connected device (e.g., inverter, proportional valve).  
- Adjust analog signal mode before sending values via :ref:`set_analog_output <manual_set_analog_output>`.

.. Note::

    - Apply before outputting values using :ref:`set_analog_output <manual_set_analog_output>`.

**Example: Configure analog output modes**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 1) Set CH1 output mode to voltage (0–10 V)
       drfl.set_mode_analog_output(ANALOG_OUT_CH1, GPIO_ANALOG_TYPE_VOLTAGE);
       std::printf("[Analog OUT CH1] Mode set to VOLTAGE\n");

       // 2) Set CH2 output mode to current (4–20 mA)
       drfl.set_mode_analog_output(ANALOG_OUT_CH2, GPIO_ANALOG_TYPE_CURRENT);
       std::printf("[Analog OUT CH2] Mode set to CURRENT\n");

       return 0;
   }

**Tips**

- Match the target device’s expected input type before enabling analog output.  
- For voltage mode, ensure total load impedance is **≥ 10 kΩ**; for current mode, ensure **≤ 500 Ω**.  
- Incorrect mode selection can cause distorted or unstable output signals.  
- Reconfigure mode after reboot if settings are not stored persistently.
