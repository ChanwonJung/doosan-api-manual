.. _manual_set_on_program_stopped:

set_on_program_stopped (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_on_program_stopped <set_on_program_stopped>`  
during **Manual (Teach)** operations. |br|
This function registers a **callback function** that is triggered whenever a program  
running on the controller is **stopped**, either manually from the Teach Pendant (TP),  
through an API command, or due to an error condition.  

It is particularly useful for restoring the teaching environment,  
resetting motion states, or logging the reason for program interruption.

**Typical usage**

- Detect and handle program termination events during manual teaching.  
- Automatically log the stop cause for debugging or traceability.  
- Reset system indicators (e.g., LED or popup) when the program halts.  
- Prepare the controller for a safe restart or next teaching sequence.

.. Note::

    - Keep callback logic simple to avoid blocking subsequent recovery actions.

**Example: Log and respond to program stop events**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   CDRFLEx drfl;

   // Callback triggered when DRL or manual program stops
   void OnProgramStopped(int cause)
   {
       cout << "-------------------------------------------\n";
       cout << "[PROGRAM STOPPED]\n";
       cout << "Stop cause: " << cause << endl;

       // LED feedback depending on cause
       if (cause == 0)
           drfl.set_state_led_color(0, 255, 0);   // Green: Normal stop
       else if (cause == 1)
           drfl.set_state_led_color(255, 0, 0);   // Red: Emergency stop
       else
           drfl.set_state_led_color(255, 200, 0); // Yellow: User interruption

       cout << "LED color updated according to stop cause.\n";
       cout << "-------------------------------------------\n";
   }

   int main()
   {
       drfl.open_connection("192.168.137.100");
       drfl.set_on_program_stopped(OnProgramStopped);
       cout << "[Teach] Program stop monitoring active.\n";

       // Keep running to receive program stop events
       while (true)
           this_thread::sleep_for(chrono::seconds(1));

       return 0;
   }

When registered, this callback executes automatically  
when a **DRL program or manual operation stops** on the controller.  
It helps implement **automatic post-stop handling**, such as LED color changes,  
system recovery preparation, or custom safety notifications.

**Tips**

- Use to detect and classify **stop causes** in real time.  
- Combine with :ref:`set_state_led_color <set_state_led_color>` for visual stop indication.  
- Ideal for automatic recovery, logging, or post-teaching cleanup routines.