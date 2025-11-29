.. _auto_get_modbus_input:

get_modbus_input (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_modbus_input <get_modbus_input>`  
during **Auto (Run)** operations to read data from a Modbus slave device.  
This allows the robot to receive real-time status from PLCs, sensors,  
industrial controllers, and automation equipment connected via Modbus.

**Typical usage**

- Read sensor status from Modbus-based digital/analog modules.  
- Wait for a PLC “machine-ready” or “cycle-complete” signal.  
- Monitor process values such as pressure, load, or temperature.  
- Use Modbus feedback for conditional logic in Auto Mode sequences.

.. Note::

    - ``strSymbol`` must correspond to a Modbus signal added through ``add_modbus_signal``.  
    - Polling rate should be managed carefully to avoid communication overhead.  
    - Combine with robot motion checks for safe synchronized operations.

**Example: Waiting for a PLC Signal Over Modbus**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Wait for PLC to signal "READY" via Modbus input
       while (drfl.get_modbus_input("PLC_READY") == 0) {
           printf("Waiting for PLC READY...\n");
           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       printf("PLC READY received. Starting robot operation.\n");

       float startPose[6] = {300.f, 200.f, 250.f, 180.f, 0.f, 0.f};
       drfl.movel(startPose, (float[2]){100.f, 50.f}, (float[2]){300.f, 100.f});

       return 0;
   }

In this example, the robot monitors a Modbus input until  
an external PLC reports readiness, then continues its Auto Mode tasks.

**Tips**

- Use Modbus inputs for machine–robot synchronization.  
- Validate register mappings in the Modbus configuration table.  
- Avoid excessive polling; 100–300 ms intervals work well for most devices.  
- Combine with DO/AI/DI logic for hybrid communication solutions.
