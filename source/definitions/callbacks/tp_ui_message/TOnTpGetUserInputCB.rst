.. _cb_tontpgetuserinputcb:

TOnTpGetUserInputCB
------------------------------------------
This is a callback function that is triggered when **user input features** are executed  
in the robot controller through the teach pendant (T/P).
It allows the application to capture and process user-entered values or selections from pop-up input windows.

As the callback function is executed automatically upon a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnTpGetUserInputCB)(LPMESSAGE_INPUT);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_tp_get_user_input(LPROBOTCONTROL pCtrl, TOnTpGetUserInputCB pCallbackFunc);

   // user input message handler
   void set_on_tp_get_user_input(TOnTpGetUserInputCB pCallbackFunc)
   {
       _set_on_tp_get_user_input(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - tInput
     - :ref:`MESSAGE_INPUT <struct_MESSAGE_INPUT>`
     - -
     - Pointer to structure containing user input data (text, number, or selection entered via T/P).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when a user input is entered on the teach pendant
   void OnTpGetUserInputCB(LPMESSAGE_INPUT tInput)
   {
       if (!tInput) return;

       cout << "[TP USER INPUT]" << endl;
       cout << "Prompt Title : " << tInput->_szTitle << endl;
       cout << "User Input   : " << tInput->_szUserInput << endl;

       // Example: respond to specific keyword
       if (strcmp(tInput->_szUserInput, "START") == 0)
           cout << "Starting operation..." << endl;
       else if (strcmp(tInput->_szUserInput, "STOP") == 0)
           cout << "Stopping operation..." << endl;
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register TP user input callback
       drfl.set_on_tp_get_user_input(OnTpGetUserInputCB);

       // Keep alive to monitor TP user inputs
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- Triggered when a **T/P input dialog** (text box, numeric field, or selection) receives user input.  
- The :ref:`MESSAGE_INPUT <struct_MESSAGE_INPUT>` structure contains fields such as prompt title, input type, and entered value.  
- Common use cases: **operator prompts**, **manual confirmations**, or **parameter entry** during DRL program execution.  
- Avoid long-running operations within the callback (execution time < 50 ms).
