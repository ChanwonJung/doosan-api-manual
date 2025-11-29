.. _manual_servo_off:

servo_off (Manual Mode)
------------------------------------------
This section explains how to use :ref:`servo_off <servo_off>` during **Manual (Teach)** operations.  
This function turns **OFF the robot’s servo power**, safely removing torque from all joints.  

It is primarily used when stopping motion for inspection, teaching, or before manually moving the robot arm by hand.

**Typical usage**

- Disable all motor torques before **hand-guided teaching** or manual alignment.  
- Safely stop motion during **setup, calibration, or recovery**.  
- Use as part of a safety or maintenance procedure to ensure the robot cannot move unexpectedly.

.. Note::

    - After calling ``servo_off()``, all robot joints become freely movable by hand.  
    - Motion commands are **disabled** until servo power is re-enabled (e.g., by using the Teach Pendant or safety reset).

**Example: Turn off servo power safely after motion**

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

       // 1) Move robot to a reference position
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 50, 50);
       drfl.mwait();

       // 2) Turn servo power OFF smoothly
       if (drfl.servo_off(STOP_TYPE_SLOW))
           std::printf("[Servo] Power OFF (SLOW stop)\n");
       else
           std::printf("[Servo] Failed to turn OFF\n");

       // 3) Wait briefly before manual intervention
       std::this_thread::sleep_for(std::chrono::seconds(2));

       // 4) At this point, the robot can be moved by hand for manual positioning or teaching
       return 0;
   }

**Tips**

- Use ``STOP_TYPE_SLOW`` whenever possible to prevent abrupt motion stops.  
- Always ensure the robot has **fully stopped** before performing manual alignment.  
- If servo power does not turn off, verify that no motion or protective stop is active using :ref:`check_motion <manual_check_motion>`.  
- To restore normal operation, re-enable servo power from the **Teach Pendant** or controller interface after manual adjustments.  
- Combine with :ref:`release_protective_stop <manual_release_protective_stop>` and :ref:`set_auto_servo_off <manual_set_auto_servo_off>` for complete safety control workflows.
