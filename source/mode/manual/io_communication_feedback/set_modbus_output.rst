.. _manual_set_modbus_output:

set_modbus_output (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_modbus_output <set_modbus_output>` during **Manual (Teach)** operations  
to manually **write values to PLC/inverter Modbus registers** for on-site verification or parameter tuning.

**Typical usage**

- Send **coil ON/OFF commands** (e.g., START/STOP, ENABLE).  
- Write **setpoints or control words** to Holding Registers (e.g., target speed, torque limit).  
- Validate device write behavior during communication setup before running Auto programs.

.. Note::

    - Supported for register types **COIL** and **HOLDING_REGISTER** only.  
    - For read-back verification, use :ref:`get_modbus_input <get_modbus_input>`.  

**Example: Write coil and holding register outputs**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Modbus symbols registered via add_modbus_signal()

       // 1) Register test symbols (simplified)
       drfl.add_modbus_signal("PLC_START",     "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_COIL, 1, 0);
       drfl.add_modbus_signal("INV_SPEED_CMD", "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_HOLDING_REGISTER, 100, 0, 1);

       // 2) Write target speed (example: 1500 = 15.00 Hz)
       bool ok_speed = drfl.set_modbus_output("INV_SPEED_CMD", 1500);

       // 3) Trigger start coil pulse
       bool ok_start = drfl.set_modbus_output("PLC_START", 1);
       std::this_thread::sleep_for(std::chrono::milliseconds(50));
       drfl.set_modbus_output("PLC_START", 0);

       // 4) Verify write success
       if (ok_speed && ok_start)
           std::printf("[Modbus] Output write successful.\n");
       else
           std::printf("[Modbus] Write failed. Check connection or tag name.\n");

       // 5) Cleanup
       drfl.del_modbus_signal("PLC_START");
       drfl.del_modbus_signal("INV_SPEED_CMD");
       return 0;
   }

**Tips**

- Avoid rapid consecutive writes; allow short **delays (≥ 50 ms)** between commands.  
- Always confirm device response using **read-back or indicator bits**.  
- Keep teaching environment clean by deleting all test symbols after use.
