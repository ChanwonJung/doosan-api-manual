.. _manual_set_mode_analog_input:

set_mode_analog_input (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_mode_analog_input <set_mode_analog_input>` during **Manual (Teach)** operations  
to **configure the signal type** (Voltage or Current) of the **control box analog input channels**.

**Typical usage**

- Define whether each analog input channel operates in **voltage mode (0–10 V)** or **current mode (4–20 mA)**.  
- Match the robot’s analog input configuration with external sensors’ signal types.  
- Prevent incorrect readings due to mismatched input mode.

.. Note::

    - Setting takes effect immediately; ensure no analog read operation is in progress.

**Example: Configure analog input types on control box**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 1) Set CH1 as current input (4–20 mA)
       drfl.set_mode_analog_input(ANALOG_IN_CH1, GPIO_ANALOG_TYPE_CURRENT);
       std::printf("[Analog IN CH1] Mode set to CURRENT\n");

       // 2) Set CH2 as voltage input (0–10 V)
       drfl.set_mode_analog_input(ANALOG_IN_CH2, GPIO_ANALOG_TYPE_VOLTAGE);
       std::printf("[Analog IN CH2] Mode set to VOLTAGE\n");

       return 0;
   }

**Tips**

- Ensure sensor output and control box mode match exactly (both voltage or both current).  
- For current mode, verify proper **current loop wiring** and resistance compliance.  
- Mode setting is persistent only until power cycle unless saved by higher-level configuration.
