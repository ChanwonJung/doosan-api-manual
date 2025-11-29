.. _cb_tontppopupcb:

TOnTpPopupCB
------------------------------------------
This is a callback function that is executed when a **user pop-up feature** is triggered  
in the robot controller. It allows developers to handle or log pop-up events displayed on the teach pendant (T/P) UI.  

As the callback function is executed automatically upon the pop-up event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnTpPopupCB)(LPMESSAGE_POPUP);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_tp_popup(LPROBOTCONTROL pCtrl, TOnTpPopupCB pCallbackFunc);
   void set_on_tp_popup(TOnTpPopupCB pCallbackFunc)
   {
       _set_on_tp_popup(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - tPopup
     - :ref:`MESSAGE_POPUP <struct_MESSAGE_POPUP>`
     - -
     - Pointer to the structure containing pop-up message information (e.g., title, message text, icon type).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when a user pop-up message appears on the TP
   void OnTpPopupCB(LPMESSAGE_POPUP tPopup)
   {
       if (!tPopup) return;

       cout << "[TP POPUP]" << endl;
       cout << "Title   : " << tPopup->_szTitle << endl;
       cout << "Message : " << tPopup->_szMessage << endl;
       cout << "Icon    : " << static_cast<int>(tPopup->_nIconType) << endl;

       // You may log or trigger additional actions here (keep under 50ms)
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to the robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register TP popup callback
       drfl.set_on_tp_popup(OnTpPopupCB);

       // Keep alive to monitor TP popup events
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback is invoked when the robot controller triggers a **teach pendant pop-up**  
  (e.g., alert messages, user confirmation dialogs, or DRL-generated pop-ups).  
- Common use cases include **logging**, **custom alert handling**, or **debug message tracing**.  
- Avoid blocking calls or long computations (execution time < 50 ms).
