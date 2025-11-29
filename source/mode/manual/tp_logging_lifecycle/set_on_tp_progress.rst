.. _manual_set_on_tp_progress:

set_on_tp_progress (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_on_tp_progress <set_on_tp_progress>` during **Manual (Teach)** operations.  
This function registers a **callback function** that receives progress updates from the Teach Pendant (TP).  
It is primarily used for monitoring **execution progress**, such as the percentage of a running program,  
or displaying visual progress feedback during manual teaching sequences.

**Typical usage**

- Display real-time progress or completion percentage during a teaching task.  
- Monitor multi-step DRL procedures executed in manual mode.  
- Log and visualize progress data on a host PC or teaching UI.  
- Synchronize TP progress updates with LED or sound feedback to improve user awareness.

.. Note::

    - The callback is triggered whenever the TP sends progress update data.  
    - The callback runs asynchronously — avoid blocking operations within it.  
    - The received structure contains fields such as ``_iPercent``, ``_iCurrentCount``, and ``_szDesc``.

**Example: Monitor progress feedback during manual teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   CDRFLEx drfl;

   // Callback for TP progress messages
   void OnTpProgress(LPMESSAGE_PROGRESS tProgress)
   {
       cout << "-------------------------------------------\n";
       cout << "[TP PROGRESS UPDATE]\n";
       cout << "Step : " << tProgress->_iCurrentCount << " / "
            << tProgress->_iTotalCount << endl;
       cout << "Progress (%) : " << tProgress->_iPercent << "%" << endl;
       cout << "Description  : " << tProgress->_szDesc << endl;
       cout << "-------------------------------------------\n";

       // Example: LED color changes according to progress
       if (tProgress->_iPercent < 50)
           drfl.set_state_led_color(0, 0, 255);     // Blue
       else if (tProgress->_iPercent < 100)
           drfl.set_state_led_color(255, 200, 0);   // Yellow
       else
           drfl.set_state_led_color(0, 255, 0);     // Green (done)
   }

   int main()
   {
       drfl.open_connection("192.168.137.100");
       drfl.set_on_tp_progress(OnTpProgress);

       cout << "[Teach] Waiting for progress updates from TP...\n";
       while (true)
           this_thread::sleep_for(chrono::seconds(1));

       return 0;
   }

When registered, this callback is executed automatically  
when a **progress message** is reported from the Teach Pendant (TP).  
It provides **real-time information about operation steps, progress percentage, and task description**  
to enhance manual teaching visibility and synchronization with host-side feedback systems.

**Tips**

- Use to monitor long or multi-step teaching procedures in real time.  
- Combine with :ref:`set_state_led_color <set_state_led_color>` for visual progress feedback.  
- Avoid heavy processing inside the callback to maintain real-time responsiveness.