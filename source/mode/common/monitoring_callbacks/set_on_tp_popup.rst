.. _set_on_tp_popup:

set_on_tp_popup
------------------------------------------
This function is used to register a callback function to check the popup message  
when the ``tp_popup`` command is used in DRL.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 639)

.. code-block:: cpp

    void set_on_tp_popup(TOnTpPopupCB pCallbackFunc) { 
        _set_on_tp_popup(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnTpPopupCB <cb_tontppopupcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include <iostream>
   #include <string>
   using namespace std;

   // Callback function to handle popup events from TP
   void OnTpPopup(LPMESSAGE_POPUP tPopup)
   {
       cout << "-------------------------------------------" << endl;
       cout << "[TP POPUP DETECTED]" << endl;
       cout << "Popup Message : " << tPopup->_szText << endl;
       cout << "Message Level : " << tPopup->_iLevel << endl;
       cout << "Button Type   : " << tPopup->_iBtnType << endl;
       cout << "-------------------------------------------" << endl;

       // Example: handle based on popup message or level
       if (strcmp(tPopup->_szText, "Confirm Start?") == 0)
       {
           cout << "[Host] Sending OK response to controller..." << endl;
           drfl.tp_popup_response(POPUP_RESPONSE_OK);
       }
       else if (tPopup->_iLevel == 2)   // Warning level popup
       {
           cout << "[Host] Warning received from TP. Logging event..." << endl;
           // Log or take action (e.g., slow down motion)
       }
       else
       {
           cout << "[Host] Display only popup - no action required." << endl;
       }
   }

   int main()
   {
       // Register the popup callback
       drfl.set_on_tp_popup(OnTpPopup);

       // Main program logic
       cout << "Waiting for popup events from Teach Pendant..." << endl;
       while (true)
       {
           // Maintain connection and check callbacks
           this_thread::sleep_for(chrono::seconds(1));
       }
       return 0;
   }

When registered, this callback function executes automatically  
when a **popup message is triggered on the Teach Pendant (TP)** through DRL.  
It allows the user to **check popup content, message level, and button type**,  
and optionally **send a response back to the controller** (e.g., OK / Cancel).  
This enables dynamic handling of TP-side prompts such as confirmations,  
warnings, or notifications during robot operation.

