.. _set_on_tp_get_user_input:

set_on_tp_get_user_input
------------------------------------------
This function is used to register a callback function to check user input  
when the ``tp_get_user_input`` command is used in DRL.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 645)

.. code-block:: cpp

    void set_on_tp_get_user_input(TOnTpGetUserInputCB pCallbackFunc) { 
        _set_on_tp_get_user_input(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnTpGetUserInputCB <cb_tontpgetuserinputcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include <iostream>
   #include <thread>
   #include <cstring>
   using namespace std;

   // Callback function for TP user input events
   void OnTpGetUserInput(LPMESSAGE_INPUT tInput)
   {
       cout << "-------------------------------------------" << endl;
       cout << "[TP USER INPUT RECEIVED]" << endl;
       cout << "Prompt Message : " << tInput->_szTitle << endl;
       cout << "User Input     : " << tInput->_szText << endl;
       cout << "Data Type      : " << tInput->_iType << endl;
       cout << "-------------------------------------------" << endl;

       // Example: handle input based on content
       if (strcmp(tInput->_szText, "start") == 0)
       {
           cout << "[Host] Received start command from TP user." << endl;
           // Execute robot routine or set flag here
       }
       else if (strcmp(tInput->_szText, "stop") == 0)
       {
           cout << "[Host] Received stop request. Halting operation." << endl;
           // Stop current motion or procedure
       }
       else
       {
           cout << "[Host] Generic input received, storing for later use." << endl;
       }
   }

   int main()
   {
       // Register the TP user input callback
       drfl.set_on_tp_get_user_input(OnTpGetUserInput);

       cout << "Waiting for user input events from Teach Pendant..." << endl;
       while (true)
       {
           this_thread::sleep_for(chrono::seconds(1));
       }
       return 0;
   }

When registered, this callback function executes automatically  
when a **user input message** is triggered on the Teach Pendant (TP).  
It allows the user to **handle typed responses or commands dynamically**,  
enabling interactive robot control or parameter entry through the TP.
