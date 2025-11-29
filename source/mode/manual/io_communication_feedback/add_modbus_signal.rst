.. _manual_add_modbus_signal:

add_modbus_signal (Manual Mode)
----------------------------------------------------
This section explains how to use :ref:`add_modbus_signal <add_modbus_signal>` during **Manual (Teach)** operations  
to register external PLC / inverter Modbus points as **symbolic tags** for quick read/write tests in **3.2.3 Communication**.

**Typical usage**

- Map a PLC/inverter register (Coil / Discrete Input / Holding / Input Register) to a **symbol name**.
- Verify **READY/FAULT** bits or write **START/SPEED** commands from a small test app during teaching.
- Prepare a clean symbol set, then use :ref:`get_modbus_input <get_modbus_input>`, :ref:`set_modbus_output <manual_set_modbus_output>`, and finally :ref:`del_modbus_signal <manual_del_modbus_signal>` to clean up.

.. Note::

    - Data width/sign/endian follow the **device manual**. Multi-word values may require device-specific handling.  
    - Inspect the registered tags via :ref:`query_modbus_data_list <query_modbus_data_list>` for debugging.

**Example: Register and test READY (DI) + START (Coil) + SPEED (Holding Reg.)**

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
       // - Manual (Teach) mode, servo/safety OK
       // - External PLC/inverter reachable over the network

       // 1) Register symbols (IP, port, type, address, default value, slave ID)
       bool ok = true;
       ok &= drfl.add_modbus_signal("PLC_READY",     "192.168.0.10", 502,
                                    MODBUS_REGISTER_TYPE_DISCRETE_INPUT, 0, 0);
       ok &= drfl.add_modbus_signal("PLC_START",     "192.168.0.10", 502,
                                    MODBUS_REGISTER_TYPE_COIL, 1, 0);
       ok &= drfl.add_modbus_signal("INV_SPEED_CMD", "192.168.0.10", 502,
                                    MODBUS_REGISTER_TYPE_HOLDING_REGISTER, 100, 0, 1);

       if (!ok) {
           std::printf("[Modbus] Failed to register one or more symbols\n");
           return -1;
       }

       // 2) Wait until external device is READY (max ~3s)
       bool ready = false;
       for (int i = 0; i < 30; ++i) {
           // For DISCRETE_INPUT/INPUT_REGISTER types, read with get_modbus_input()
           if (drfl.get_modbus_input("PLC_READY")) {
               ready = true;
               break;
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }
       std::printf("READY = %s\n", ready ? "ON" : "OFF");
       if (!ready) goto CLEANUP;

       // 3) Write a speed command (example: 1500 means 15.00 Hz if device uses 0.01 scaling)
       drfl.set_modbus_output("INV_SPEED_CMD", 1500);

       // 4) Issue START coil pulse
       drfl.set_modbus_output("PLC_START", 1);
       std::this_thread::sleep_for(std::chrono::milliseconds(50));
       drfl.set_modbus_output("PLC_START", 0);

       // Optional: Read back additional status via get_modbus_input("...") here

   CLEANUP:
       // 5) Always clean up test symbols
       drfl.del_modbus_signal("PLC_READY");
       drfl.del_modbus_signal("PLC_START");
       drfl.del_modbus_signal("INV_SPEED_CMD");
       return 0;
   }

**Tips**

- Double-check **addressing (0/1-based)**, **byte/word order**, and **scaling** in the device manual.  
- Keep test tags **namespaced** (e.g., ``"TEST/PLC_READY"``) and **always delete** them after tests.  
- If you see intermittent timeouts, add **simple retry/timeout** logic and inspect with :ref:`query_modbus_data_list <manual_query_modbus_data_list>`.
