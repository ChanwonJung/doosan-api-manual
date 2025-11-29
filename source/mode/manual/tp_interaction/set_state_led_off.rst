.. _manual_set_state_led_off:

set_state_led_off (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_state_led_off <set_state_led_off>` during **Manual (Teach)** operations.  
This function turns **off** the robot’s State LED completely.  
It is often used when you want to disable LED indication temporarily during maintenance or quiet operation.

**Typical usage**

- Turn off LED illumination during manual operation or diagnostics.  
- Use when LED light may interfere with visual calibration or camera sensing.  
- Disable LED to indicate a “paused” or “standby” condition.

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

       drfl.set_state_led_off();
       cout << "[LED] State LED has been turned off.\n";

       this_thread::sleep_for(chrono::seconds(3));
       drfl.state_led_reset();  // Restore LED afterward
       cout << "[LED] LED reset to default state.\n";

       return 0;
   }

This function **disables all LED output**, allowing manual tasks to be performed  
without LED distraction or ambient light interference.

**Tips**

- Use to indicate a **standby** or **inactive** state during teaching pauses.  
- Combine with :ref:`state_led_reset <state_led_reset>` to restore LED behavior after maintenance.  
- Helpful when performing **camera calibration** or light-sensitive operations.