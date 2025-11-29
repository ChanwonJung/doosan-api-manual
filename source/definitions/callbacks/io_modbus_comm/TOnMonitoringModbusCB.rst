.. _cb_tonmonitoringmodbuscb:

TOnMonitoringModbusCB
------------------------------------------
This is a callback function for checking **Modbus I/O state data** registered in the robot controller.  
As the callback function is executed automatically upon Modbus monitoring updates,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnMonitoringModbusCB)(const LPMONITORING_MODBUS);

   // registration API (internal + wrapper)
   DRFL_API void _SetOnMonitoringModbus(LPROBOTCONTROL pCtrl, TOnMonitoringModbusCB pCallbackFunc);
   void SetOnMonitoringModbus(TOnMonitoringModbusCB pCallbackFunc)
   {
       _SetOnMonitoringModbus(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pModbus
     - :ref:`MONITORING_MODBUS <struct_MONITORING_MODBUS>`
     - -
     - Pointer to structure containing Modbus register symbols and values.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback: invoked when Modbus monitoring data updates
   void OnMonitoringModbusCB(const LPMONITORING_MODBUS pModbus)
   {
       if (!pModbus) return;

       cout << "[MODBUS] register count = " << pModbus->_iRegCount << endl;

       // Each entry contains a symbol (name) and its current value
       for (int i = 0; i < pModbus->_iRegCount; ++i)
       {
           // Example fields based on structure naming
           //   _tRegister[i]._szSymbol  → register name
           //   _tRegister[i]._iValue    → register value
           cout << "  " << pModbus->_tRegister[i]._szSymbol
                << " : " << pModbus->_tRegister[i]._iValue << endl;
       }
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register Modbus monitoring callback
       drfl.set_on_monitoring_modbus(OnMonitoringModbusCB);

       // Keep process alive to receive Modbus updates
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- Use this callback to build **Modbus dashboards**, **alarm rules**, or **data logging** pipelines.  
- For I/O state (GPIO) monitoring, see :ref:`TOnMonitoringCtrlIOCB <cb_tonmonitoringctrliocb>` and its EX variants.  
- Keep the callback lightweight (execution time < 50 ms) and avoid blocking operations.
