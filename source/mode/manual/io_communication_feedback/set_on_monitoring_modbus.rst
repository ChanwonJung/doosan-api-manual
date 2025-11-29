.. _manual_set_on_monitoring_modbus:

set_on_monitoring_modbus (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_on_monitoring_modbus <set_on_monitoring_modbus>` during **Manual (Teach)** operations  
to **register a callback function** that monitors **Modbus I/O data** exchanged between the robot controller  
and external devices such as PLCs or inverters in real time.

**Typical usage**

- Observe Modbus coil/register states for debugging communication.  
- Monitor real-time signals (e.g., READY, RUN, FAULT, SPEED) from an external PLC or inverter.  
- Log Modbus traffic and diagnose incorrect addresses or value updates.

.. Note::

    - The callback is triggered whenever Modbus data (coil, discrete input, holding, or input register) changes.  
    - Must be registered **after establishing a connection** and after Modbus symbols are defined using :ref:`add_modbus_signal(Manual Mode) <manual_add_modbus_signal>`.  

**Example: Register and handle Modbus monitoring callback**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   // 1) Define callback function
   void OnMonitoringModbus(const LPROBOT_MONITORING_MODBUS pModbusData) {
       std::printf("[Modbus Monitor] Symbol: %s | Type: %d | Value: %d\n",
                   pModbusData->_szSymbolName,
                   pModbusData->_iRegType,
                   pModbusData->_nValue);
   }

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Modbus signals registered via add_modbus_signal()

       // 2) Register callback for Modbus monitoring
       drfl.set_on_monitoring_modbus(OnMonitoringModbus);
       std::printf("[Modbus] Monitoring callback registered.\n");

       // 3) Keep program running to receive updates
       while (true) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       return 0;
   }

**Tips**

- Avoid long or blocking operations inside the callback function.  
- Use callbacks to trigger UI updates or lightweight logging rather than heavy computation.  
- Ensure all Modbus tags are registered and reachable to receive consistent monitoring events.  
- Unregister or stop monitoring before disconnecting from the robot controller to avoid dangling callbacks.
