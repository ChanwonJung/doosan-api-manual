.. _manual_get_modbus_input:

get_modbus_input (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_modbus_input <get_modbus_input>` during **Manual (Teach)** operations  
to **read real-time values** from external PLC or inverter Modbus registers for diagnostic or verification purposes.

**Typical usage**

- Monitor **status bits** (e.g., READY, RUN, FAULT) from coils or discrete inputs.  
- Read **analog feedback** (e.g., current speed, torque, or position) from Input or Holding Registers.  
- Check whether external Modbus communication is functioning correctly during manual setup.

.. Note::
  
    - Applicable for **DISCRETE_INPUT** and **INPUT_REGISTER** types.  
    - For writable points, use :ref:`set_modbus_output <set_modbus_output>`.  
    - Ensure the device uses the correct **address base (0/1-based)** and **byte/word order**.

**Example: Read PLC READY and inverter speed feedback**

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
       // - Modbus symbols registered beforehand

       // 1) Register input tags
       drfl.add_modbus_signal("PLC_READY", "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_DISCRETE_INPUT, 0, 0);
       drfl.add_modbus_signal("INV_SPEED_FB", "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_INPUT_REGISTER, 120, 0, 1);

       // 2) Poll device until READY or timeout
       bool ready = false;
       for (int i = 0; i < 30; ++i) {
           unsigned short val = drfl.get_modbus_input("PLC_READY");
           if (val == 1) { ready = true; break; }
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }
       std::printf("[PLC_READY] = %s\n", ready ? "ON" : "OFF");

       // 3) Read inverter feedback (e.g., speed in 0.01 Hz units)
       unsigned short fb = drfl.get_modbus_input("INV_SPEED_FB");
       std::printf("[INV_SPEED_FB] = %u (%.2f Hz)\n", fb, fb / 100.0);

       // 4) Cleanup
       drfl.del_modbus_signal("PLC_READY");
       drfl.del_modbus_signal("INV_SPEED_FB");
       return 0;
   }

**Tips**

- If read value stays 0, confirm device mapping and IP/port configuration.  
- Periodically polling too fast may cause **timeout or CRC errors**; use 50–200 ms intervals.  
- For multi-word data (e.g., 32-bit), combine successive registers per device documentation.
