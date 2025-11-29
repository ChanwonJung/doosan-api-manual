.. _auto_get_digital_input:

get_digital_input (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_digital_input <get_digital_input>`  
during **Auto (Run)** operations to read the state of a **digital input (DI)**  
channel connected to sensors or external equipment.

Digital inputs are used to receive binary signals such as  
part-detection sensors, button inputs, machine-ready signals,  
or safety interlocks.

**Typical usage**

- Wait for a sensor to detect a part before grasping.  
- Synchronize robot actions with external machine signals.  
- Implement interlock-based sequence logic.  
- Monitor jig/fixture status during automated runs.

.. Note::
 
    - DI signals often require debounce logic depending on the sensor type.  
    - For tool-mounted DI, use ``get_tool_digital_input``.

**Example: Waiting for a Part-Detected Sensor**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Wait for DI[0] to become TRUE (part present)
       while (!drfl.get_digital_input(0)) {
           printf("Waiting for part...\n");
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }

       printf("Part detected! Executing pick motion.\n");

       float pick[6] = {250.f, 200.f, 180.f, 180.f, 0.f, 0.f};
       drfl.movel(pick, (float[2]){80.f, 40.f}, (float[2]){300.f, 120.f});

       return 0;
   }

In this example, the robot continuously monitors a DI channel  
until a part-detection sensor is triggered, then performs a pick motion.

**Tips**

- Use DI for sensors, machine-ready signals, and interlocks.  
- Always validate sensor wiring and signal polarity.  
- Use polling intervals of 20–100 ms for stable Auto Mode loops.  
- Combine with DO signals for synchronized machine–robot control.
