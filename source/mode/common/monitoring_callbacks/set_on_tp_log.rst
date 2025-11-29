.. _set_on_tp_log:

set_on_tp_log
------------------------------------------
This function is used to register a callback function to check log messages  
when the ``tp_log`` command is used in DRL.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 641) 

.. code-block:: cpp

    void set_on_tp_log(TOnTpLogCB pCallbackFunc) { 
        _set_on_tp_log(_rbtCtrl, pCallbackFunc); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnTpLogCB <cb_tontplogcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include <iostream>
   #include <fstream>
   #include <ctime>
   #include <string>
   using namespace std;

   // Simple utility to add timestamp
   string GetTimestamp()
   {
       time_t now = time(0);
       tm* ltm = localtime(&now);
       char buffer[64];
       sprintf(buffer, "%04d-%02d-%02d %02d:%02d:%02d",
               1900 + ltm->tm_year, 1 + ltm->tm_mon, ltm->tm_mday,
               ltm->tm_hour, ltm->tm_min, ltm->tm_sec);
       return string(buffer);
   }

   // Callback for TP log messages
   void OnTpLog(const char* strLog)
   {
       cout << "[" << GetTimestamp() << "] [TP LOG] " << strLog << endl;

       // Example: also save to local log file
       ofstream logFile("tp_log_history.txt", ios::app);
       if (logFile.is_open())
       {
           logFile << "[" << GetTimestamp() << "] " << strLog << endl;
           logFile.close();
       }

       // Example: detect specific event keyword
       if (strstr(strLog, "Warning"))
           cout << "[Host] Warning detected from TP log." << endl;
   }

   int main()
   {
       // Register TP log callback
       drfl.set_on_tp_log(OnTpLog);

       cout << "Waiting for TP log events..." << endl;
       while (true)
       {
           this_thread::sleep_for(chrono::seconds(1));
       }
       return 0;
   }

When registered, this callback function executes automatically  
when a **log message is triggered on the Teach Pendant (TP)** through DRL.  
It enables **real-time monitoring and logging of TP events**,  
allowing users to record, filter, or react to messages as needed.
