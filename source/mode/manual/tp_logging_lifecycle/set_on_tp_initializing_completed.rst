.. _manual_set_on_tp_initializing_completed:

set_on_tp_initializing_completed (Manual Mode)
-------------------------------------------------
This section explains how to use :ref:`set_on_tp_initializing_completed <set_on_tp_initializing_completed>`  
during **Manual (Teach)** operations. |br|
This function registers a **callback function** that is invoked once the Teach Pendant (TP)  
has finished its initialization process and is ready for user interaction.  
It is typically used to enable UI elements or start monitoring threads  
after the TP has fully booted and established communication with the controller.

**Typical usage**

- Detect when the TP has completed boot-up and is ready for teaching operations.  
- Automatically enable custom UI panels or log systems after initialization.  
- Display messages or LED signals indicating readiness for manual control.  
- Synchronize startup procedures between the TP and host PC.

.. Note::

    - The callback is called **only once** after TP initialization completes.  
    - Execution is asynchronous and should be kept lightweight.  
    - The callback remains registered until replaced or the session is closed.

**Example: Initialize teaching environment after TP startup**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   CDRFLEx drfl;

   // Callback executed after TP finishes initialization
   void OnTpInitCompleted()
   {
       cout << "-------------------------------------------\n";
       cout << "[TP INITIALIZATION COMPLETED]\n";
       cout << "Teach Pendant is now ready for user interaction.\n";
       cout << "-------------------------------------------\n";

       // Set LED to indicate readiness
       drfl.set_state_led_color(0, 255, 0); // Green: Ready
   }

   int main()
   {
       drfl.open_connection("192.168.137.100");
       drfl.set_on_tp_initializing_completed(OnTpInitCompleted);
       cout << "[Teach] Waiting for TP initialization...\n";

       // Keep running to detect initialization completion
       while (true)
           this_thread::sleep_for(chrono::seconds(1));

       return 0;
   }

When registered, this callback executes automatically  
once the **Teach Pendant (TP) completes its initialization sequence**.  
It allows the host to **start teaching-related processes or indicate readiness visually**  
(e.g., turning the LED green when TP is ready).

**Tips**

- Use to trigger system checks or UI activation right after TP startup.  
- Combine with :ref:`set_state_led_color <set_state_led_color>` to indicate initialization status.  
- Ideal for preparing monitoring threads or reconnecting services automatically.