.. _manual_query_modbus_data_list:

query_modbus_data_list (Manual Mode)
------------------------------------------
This section explains how to use :ref:`query_modbus_data_list <query_modbus_data_list>` during **Manual (Teach)** operations.  
This function retrieves the **current list of Modbus signals** (both inputs and outputs) registered in the controller.  
It allows operators to verify communication mappings, monitor connected devices, and debug Modbus I/O configurations during manual setup or testing.

**Typical usage**

- Display all registered **Modbus input/output channels** during system commissioning.  
- Check whether a device (e.g., PLC, sensor, actuator) is properly linked to the Modbus network.  
- Validate signal names, data addresses, and values before running automatic sequences.  
- Use as a diagnostic tool when Modbus devices fail to respond or behave unexpectedly.

.. Note::

    - The function provides **read-only data**; it does not modify or refresh Modbus connections.  
    - Use :ref:`add_modbus_signal <manual_add_modbus_signal>` and :ref:`del_modbus_signal <manual_del_modbus_signal>` to manage Modbus entries.  
    - Typically used after network setup or signal registration to confirm configuration integrity.

**Example: Display all registered Modbus signals**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <chrono>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Modbus device configured via add_modbus_signal()

       LPMODBUS_DATA_LIST pList = drfl.query_modbus_data_list();
       if (pList) {
           cout << "-------------------------------------------\n";
           cout << "[MODBUS SIGNAL LIST]\n";
           cout << "Total Signals: " << pList->_iCount << endl;

           for (int i = 0; i < pList->_iCount; ++i) {
               auto& data = pList->_tModbusData[i];
               cout << "-------------------------------------------\n";
               cout << "Index       : " << i << endl;
               cout << "Name        : " << data._szName << endl;
               cout << "Address     : " << data._iAddress << endl;
               cout << "Type        : " << (data._iType == 0 ? "Input" : "Output") << endl;
               cout << "Value       : " << data._iValue << endl;
           }
           cout << "-------------------------------------------\n";
       } else {
           cout << "[Modbus] No registered Modbus signals found.\n";
       }

       return 0;
   }

**Tips**

- Use this function frequently during **field device mapping** or **I/O verification**.  
- When signal values are not updating, check Modbus master/slave configuration and wiring.  
- Combine with :ref:`get_modbus_input <manual_get_modbus_input>` and :ref:`set_modbus_output <manual_set_modbus_output>` for real-time testing.  
- Ideal for debugging Modbus network communication directly from the Teach mode without running full automation sequences.
