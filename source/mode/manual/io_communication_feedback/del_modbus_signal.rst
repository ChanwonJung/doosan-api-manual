.. _manual_del_modbus_signal:

del_modbus_signal (Manual Mode)
----------------------------------------------------
This section explains how to use :ref:`del_modbus_signal <del_modbus_signal>` during **Manual (Teach)** operations  
to **unregister** previously created Modbus symbols after testing PLC or inverter communication in **3.2.3 Communication**.

**Typical usage**

- Clean up symbolic Modbus tags created via :ref:`add_modbus_signal <add_modbus_signal>`.  
- Prevent duplicate symbol registration or memory leaks during repeated manual tests.  
- Maintain a consistent Modbus tag list for teaching and debugging.

.. Note::

    - Always call this function **after finishing tests** to release the Modbus entry.  
    - Use :ref:`query_modbus_data_list <query_modbus_data_list>` to verify that symbols were properly removed.

**Example: Register, test, and remove Modbus symbols**

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
       // - External PLC/inverter reachable

       // 1) Register test symbols
       drfl.add_modbus_signal("PLC_READY",     "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_DISCRETE_INPUT, 0, 0);
       drfl.add_modbus_signal("PLC_START",     "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_COIL, 1, 0);
       drfl.add_modbus_signal("INV_SPEED_CMD", "192.168.0.10", 502,
                              MODBUS_REGISTER_TYPE_HOLDING_REGISTER, 100, 0, 1);

       // 2) Perform a brief test
       bool ready = drfl.get_modbus_input("PLC_READY");
       std::printf("[READY] = %s\n", ready ? "ON" : "OFF");

       drfl.set_modbus_output("INV_SPEED_CMD", 1500);
       drfl.set_modbus_output("PLC_START", 1);
       std::this_thread::sleep_for(std::chrono::milliseconds(50));
       drfl.set_modbus_output("PLC_START", 0);

       // 3) Remove symbols after testing
       bool ok = true;
       ok &= drfl.del_modbus_signal("PLC_READY");
       ok &= drfl.del_modbus_signal("PLC_START");
       ok &= drfl.del_modbus_signal("INV_SPEED_CMD");

       if (ok) std::printf("[Modbus] Symbols successfully deleted.\n");
       else    std::printf("[Modbus] One or more deletions failed.\n");

       return 0;
   }

**Tips**

- Always remove all temporary symbols to avoid **namespace clutter**.  
- If deletion fails, check for **typos** or ensure the symbol is not actively in use.  
- Re-run :ref:`query_modbus_data_list <query_modbus_data_list>` to confirm successful cleanup.
