.. _manual_tp_popup_response:

tp_popup_response (Manual Mode)
------------------------------------------
This section explains how to use :ref:`tp_popup_response <tp_popup_response>` during **Manual (Teach)** operations.  
This function sends a **response** (e.g., OK, CANCEL, YES, NO) back to the Teach Pendant (TP)  
when a popup is triggered by a DRL program or a system event during manual teaching.  

It allows the host application to remotely acknowledge or reject operator prompts.

**Typical usage**

- Automatically confirm or cancel popup prompts in specific teaching workflows.  
- Integrate TP prompts with external UIs or safety validation systems.  
- Use in combination with :ref:`set_on_tp_popup <set_on_tp_popup>` to manage two-way popup interaction.  
- Implement custom popup policies (e.g., auto-approve safe operations, require manual confirmation for high-risk ones).

.. Note::

    - Can only be called **after** the TP popup callback (:ref:`set_on_tp_popup <set_on_tp_popup>`) has been triggered.

**Example: Send popup response based on custom logic**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <cstring>
   using namespace std;
   using namespace DRAFramework;

   CDRFLEx drfl;

   // Popup callback: triggered when popup appears on TP
   void OnTpPopup(LPMESSAGE_POPUP tPopup)
   {
       cout << "-------------------------------------------\n";
       cout << "[TP POPUP RECEIVED]\n";
       cout << "Message : " << tPopup->_szText << "\n";
       cout << "Level   : " << (int)tPopup->_iLevel << "\n";
       cout << "Button Type : " << (int)tPopup->_iBtnType << "\n";
       cout << "-------------------------------------------\n";

       // Example 1: Auto-approve if it's an information popup
       if (tPopup->_iLevel == 0 && strstr(tPopup->_szText, "Continue") != nullptr)
       {
           drfl.tp_popup_response(POPUP_RESPONSE_OK);
           cout << "[Host] Auto-OK sent to controller.\n";
       }
       // Example 2: Auto-cancel if a warning or safety message appears
       else if (tPopup->_iLevel >= 2)
       {
           drfl.tp_popup_response(POPUP_RESPONSE_CANCEL);
           cout << "[Host] Warning detected. Sent CANCEL response.\n";
       }
       else
       {
           cout << "[Host] Waiting for manual confirmation on TP.\n";
       }
   }

   int main()
   {
       // Preconditions:
       // - drfl.open_connection("192.168.137.100");
       // - Controller in Manual (Teach) mode
       drfl.set_on_tp_popup(OnTpPopup);
       cout << "[Teach] Popup callback active. Ready to respond automatically.\n";

       // Keep program running to receive TP popup events
       while (true)
           this_thread::sleep_for(chrono::seconds(1));

       return 0;
   }

In this example, the host PC listens for **popup events** from the Teach Pendant (TP)  
and sends an automatic response based on popup level or content.  
For instance, informational popups are acknowledged with OK, while warnings trigger CANCEL.  
This enables the host to **automate response handling** while still respecting safety-critical interactions.

**Tips**

- Always verify the popup **message level** before sending an automatic response.  
- For **critical operations** (e.g., tool change, safety override), require manual confirmation on the TP.  
- When testing DRL programs remotely, this function can help simulate **operator confirmation flows**.  
- Combine with :ref:`set_on_tp_get_user_input <set_on_tp_get_user_input>` for integrated dialog-driven manual mode automation.
