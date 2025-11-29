.. _manual_set_on_tp_popup:

set_on_tp_popup (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_on_tp_popup <set_on_tp_popup>` during **Manual (Teach)** operations.  
This function registers a **callback function** that is invoked whenever a DRL program or TP action triggers a **popup message** on the Teach Pendant.  
It is useful for acknowledging prompts (OK/Cancel), routing operator decisions to the host app, and logging human–robot interactions during teaching.

**Typical usage**

- Show **operator confirmations** (e.g., “Clamp closed?”, “Ready to jog to next point?”) and capture the response on the host PC.  
- **Gate risky actions** in teach mode (e.g., approach near obstacles) with an explicit human confirmation.  
- **Log popup content/level/button type** to audit teaching sessions or guide SOPs.

.. Note::

    - The callback is triggered **every time a TP popup occurs** while connected.  
    - Keep the callback **non-blocking**; do heavy work in a worker thread to avoid UI stalls.  
    - To answer a popup from the host, use :ref:`tp_popup_response <tp_popup_response>`.

**Example: Register a popup callback and respond to operator choice**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <cstring>
   using namespace std;
   using namespace DRAFramework;

   CDRFLEx drfl;

   // 1) Define TP popup callback
   void OnTpPopup(LPMESSAGE_POPUP tPopup)
   {
       cout << "-------------------------------------------\n";
       cout << "[TP POPUP]\n";
       cout << "Message : " << tPopup->_szText   << "\n";
       cout << "Level   : " << (int)tPopup->_iLevel   << "\n";   // info/warn/error
       cout << "Buttons : " << (int)tPopup->_iBtnType << "\n";   // OK / OK-Cancel / Yes-No
       cout << "-------------------------------------------\n";

       // 2) Simple policy examples in Teach mode
       //    - Auto-acknowledge harmless info
       //    - Require operator decision for risk-related prompts (leave unanswered)
       if (tPopup->_iLevel == 0 /* info */ &&
           strstr(tPopup->_szText, "Start jogging") != nullptr)
       {
           // Acknowledge informational prompt
           drfl.tp_popup_response(POPUP_RESPONSE_OK);
           cout << "[Host] Auto-acknowledged jogging start.\n";
       }
       else if (strstr(tPopup->_szText, "Near obstacle") != nullptr)
       {
           // Let the human press the TP button; do not auto-respond
           cout << "[Host] Waiting for operator decision on TP.\n";
       }
       else
       {
           // Default: no automatic response
           cout << "[Host] Logged popup. No automatic response.\n";
       }
   }

   int main()
   {
       // Preconditions:
       //  - drfl.open_connection("192.168.137.100");
       //  - Controller in Manual (Teach) mode
       drfl.set_on_tp_popup(OnTpPopup);
       cout << "[Teach] TP popup callback registered.\n";

       // Keep the process alive to receive callbacks during teaching
       while (true) std::this_thread::sleep_for(std::chrono::seconds(1));
       return 0;
   }

In this example, the host application listens for **popup events** generated on the Teach Pendant (TP).  
When an informational popup appears (e.g., “Start jogging”), it automatically sends an OK response.  
However, for higher-risk messages such as “Near obstacle,” the system pauses and waits for the operator’s manual input.  
This approach enables **safe semi-automatic decision handling** while maintaining manual override control.

**Tips**

- Combine with :ref:`set_on_tp_log <set_on_tp_log>` to correlate **popup** and **log** streams for SOP auditing.  
- For input forms on TP, pair with :ref:`set_on_tp_get_user_input <set_on_tp_get_user_input>` and :ref:`tp_get_user_input_response <tp_get_user_input_response>`.  
- Use **LED feedback** (:ref:`set_state_led_color <set_state_led_color>`) to mirror popup severity (e.g., warning→amber, error→red) in teach mode.  
- If your callback policy auto-responds, document the cases clearly and avoid auto-OK on **dangerous actions**.
