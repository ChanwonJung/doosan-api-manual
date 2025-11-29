.. _manual_state_led_reset:

state_led_reset (Manual Mode)
------------------------------------------
This section explains how to use :ref:`state_led_reset <state_led_reset>` during **Manual (Teach)** operations.  
This function resets the **State LED** to its default controller-defined rule.  
It is typically used when the LED color has been customized (via :ref:`set_state_led_color <set_state_led_color>`)  
and needs to return to standard behavior reflecting system state.

**Typical usage**

- Revert LED behavior after custom manual-mode feedback (e.g., after color change).  
- Restore LED control to the robot controller’s internal rule logic.  
- Use at the end of teaching or before switching to automatic mode.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;
       drfl.open_connection("192.168.137.100");

       if (drfl.state_led_reset())
           cout << "[LED] LED state reset to default controller rule.\n";
       else
           cout << "[ERROR] Failed to reset LED state.\n";

       return 0;
   }

When called, this function **restores the LED to its controller-managed mode**,  
removing any manual color overrides applied during teaching.

**Tips**

- Call after using :ref:`set_state_led_color <set_state_led_color>` to restore default LED behavior.  
- Useful at the end of manual teaching to indicate system standby.  
- Combine with :ref:`set_state_led_off <set_state_led_off>` for clear on/off transitions.