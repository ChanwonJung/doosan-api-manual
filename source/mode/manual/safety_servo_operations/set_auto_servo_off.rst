.. _manual_set_auto_servo_off:

set_auto_servo_off (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_auto_servo_off <set_auto_servo_off>` during **Manual (Teach)** operations.  
This function enables or disables the **automatic servo-off feature**, which turns off servo power automatically  
after a specified period of robot inactivity. It helps reduce energy consumption and prevent unwanted torque holding when idle.

**Typical usage**

- Enable **auto servo-off** during teaching sessions to automatically disable servo torque after a period of inactivity.  
- Prevent unnecessary heat or wear on servo motors when the robot is stationary.  
- Disable the feature temporarily when performing long-duration manual setups.

.. Note::

    - Servo power will automatically turn off if **no motion commands** or **manual jogging** occur during the timeout period.

**Example: Enable automatic servo-off after 60 seconds of inactivity**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Servo power currently ON

       // 1) Enable auto servo-off (60 seconds timeout)
       if (drfl.set_auto_servo_off(true, 60.0f))
           std::printf("[Auto Servo-Off] Enabled (timeout: 60s)\n");
       else
           std::printf("[Auto Servo-Off] Failed to enable.\n");

       // 2) Wait for demonstration (simulate idle state)
       std::printf("Waiting... Servo will turn OFF automatically after 60 seconds of inactivity.\n");
       std::this_thread::sleep_for(std::chrono::seconds(65));

       // 3) Disable auto servo-off again
       drfl.set_auto_servo_off(false, 0);
       std::printf("[Auto Servo-Off] Disabled.\n");

       return 0;
   }

**Tips**

- Always verify that servo power is **restored manually** before issuing new motion commands after an auto servo-off event.  
- When using this feature during long teaching sessions, set a **moderate timeout (30–90s)** to balance safety and convenience.  
- The feature only activates during **idle states**—active motions or held torques reset the timer.  
- Combine with :ref:`servo_off <manual_servo_off>` for manual shutdown and :ref:`release_protective_stop <manual_release_protective_stop>` for complete recovery sequences.  
- For Auto mode operation, ensure the timeout is sufficiently long to avoid unwanted servo-off during program pauses.
