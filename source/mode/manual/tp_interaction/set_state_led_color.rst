.. _manual_set_state_led_color:

set_state_led_color (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_state_led_color <set_state_led_color>` during **Manual (Teach)** operations.  
This function sets the **State LED color** using RGB values, allowing users to define custom color codes  
to indicate specific teaching or safety states.

**Typical usage**

- Provide visual feedback for teaching states (e.g., blue = teaching, yellow = waiting, red = stop).  
- Display custom LED colors to represent operator messages or warnings.  
- Synchronize LED with popup or log severity in manual teaching mode.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;
       drfl.open_connection("192.168.137.100");

       // Blue - Teaching Ready
       drfl.set_state_led_color(0, 0, 255);
       cout << "[LED] Teaching Ready (Blue)\n";
       this_thread::sleep_for(chrono::seconds(2));

       // Yellow - Waiting for Input
       drfl.set_state_led_color(255, 200, 0);
       cout << "[LED] Waiting for user input (Yellow)\n";
       this_thread::sleep_for(chrono::seconds(2));

       // Red - Error or Stop
       drfl.set_state_led_color(255, 0, 0);
       cout << "[LED] Error Condition (Red)\n";
       this_thread::sleep_for(chrono::seconds(2));

       drfl.state_led_reset();
       return 0;
   }

By setting RGB values manually, this function lets you display **context-aware colors**  
to improve operator awareness during manual teaching.

**Tips**

- Common color usage: Blue = Teaching, Yellow = Waiting, Red = Error.  
- Use with :ref:`set_on_tp_popup <set_on_tp_popup>` for visual popup feedback.  
- Reset with :ref:`state_led_reset <state_led_reset>` after teaching.