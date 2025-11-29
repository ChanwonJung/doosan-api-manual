.. _cb_tontplogcb:

TOnTpLogCB
------------------------------------------
This is a callback function that is triggered when a **user log feature** is executed  
on the robot controller (e.g., T/P message logs or user-defined log prints).  

As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnTpLogCB)(const char[256]);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_tp_log(LPROBOTCONTROL pCtrl, TOnTpLogCB pCallbackFunc);
   void set_on_tp_log(TOnTpLogCB pCallbackFunc)
   {
       _set_on_tp_log(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - strLog
     - string
     - -
     - 256-byte character string containing the T/P log message.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when a log message is generated on the teach pendant
   void OnTpLogCB(const char strLog[256])
   {
       cout << "[TP LOG MESSAGE] " << strLog << endl;

       // Optional: write logs to file or external system
       ofstream logFile("tp_log_history.txt", ios::app);
       if (logFile.is_open()) {
           logFile << strLog << endl;
           logFile.close();
       }
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register TP log callback
       drfl.set_on_tp_log(OnTpLogCB);

       // Keep program alive to receive TP log messages
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- Triggered automatically when the **teach pendant** logs a system or user message.  
- Useful for creating **log monitors**, **debug tools**, or **real-time system diagnostics**.  
- Ensure callback execution remains short (< 50 ms); defer long operations to a background thread if necessary.
