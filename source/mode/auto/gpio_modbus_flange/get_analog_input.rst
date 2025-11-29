.. _auto_get_analog_input:

get_analog_input (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_analog_input <get_analog_input>`  
during **Auto (Run)** operations to read the value of an  
**analog input (AI)** channel connected to sensors or external devices.

Analog inputs are commonly used to monitor pressure sensors,  
distance sensors, potentiometers, load cells, or any device  
that outputs variable voltage/current levels.

**Typical usage**

- Monitor pressure or vacuum levels before gripping.  
- Read analog distance/height sensors during alignment tasks.  
- Receive feedback from proportional actuators or external controllers.  
- Implement threshold-based decision logic in Auto Mode.

.. Note::

    - ``nIndex`` identifies the analog input channel.  
    - Ensure proper analog mode configuration using ``set_mode_analog_input``.  
    - Scaling or conversion to engineering units may be required.

**Example: Checking Vacuum Level Before Picking**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Wait until pressure reaches target threshold
       while (drfl.get_analog_input(0) < 4.0f) {   // e.g., threshold voltage
           printf("Building vacuum...\n");
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }

       printf("Vacuum level sufficient. Executing pick motion.\n");

       float pick[6] = {250.f, 200.f, 180.f, 180.f, 0.f, 0.f};
       drfl.movel(pick, (float[2]){80.f, 40.f}, (float[2]){300.f, 120.f});

       return 0;
   }

In this example, the robot continuously monitors an analog sensor  
until a threshold is met, ensuring safe and valid Auto Mode pick operation.

**Tips**

- Use AI channels for continuous monitoring of sensors and process parameters.  
- Apply filtering or averaging in software if the signal is noisy.  
- Combine with AO for closed-loop process control.  
- Use engineering unit conversions for pressure, force, or distance sensors.
