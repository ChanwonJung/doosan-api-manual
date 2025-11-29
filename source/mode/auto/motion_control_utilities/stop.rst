.. _auto_stop:

stop (Auto Mode)
------------------------------------------
This section explains how to use :ref:`stop <stop>`  
during **Auto (Run)** operations to halt the **currently active robot motion**.  

The stopping behavior depends on the selected :ref:`STOP_TYPE <enum_STOP_TYPE>`  
(e.g., **quick**, **slow**, **hold**).  
Unlike an emergency stop, this function affects **only the current motion segment**,  
not the entire robot system.

**Typical usage**

- Interrupt an ongoing motion when a sensor condition is triggered.  
- Perform a smooth (slow) stop for safe task transitions.  
- Execute a quick stop for urgent motion cancellation.  
- Use in adaptive automation where motion may need to be cancelled mid-trajectory.  

.. Note::

   - ``STOP_TYPE_QUICK`` → Fast deceleration, immediate halt  
   - ``STOP_TYPE_SLOW``  → Smooth deceleration, minimal jerk  
   - ``STOP_TYPE_HOLD``  → Stop and maintain current position  
   - Only affects the current motion; does **not** cancel or stop the DRL program itself  

**Example: Interrupting Motion With a Slow Stop**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Start an asynchronous linear motion
       float target[6] = {784, 543, 970, 0, 180, 0};
       drfl.amovel(target, 100, 200);
       printf("Motion started.\n");

       // 2) Wait 2 seconds before stopping the motion
       Sleep(2000);

       // 3) Perform a slow stop for smooth deceleration
       if (!drfl.stop(STOP_TYPE_SLOW)) {
           printf("Failed to stop motion.\n");
           return -1;
       }

       printf("Motion stopped with slow deceleration.\n");
       return 0;
   }

In this example, the robot begins moving asynchronously to a target pose.  
After a delay, the program issues a **slow stop** command to smoothly halt the motion  
without abruptly cancelling the DV trajectory.

**Tips**

- Use **Quick Stop** for fast interruption when timing is critical.  
- Use **Slow Stop** during normal automation flows to keep movement smooth.  
- Use **Hold Stop** when precise endpoint stability is required.  
- Combine with :ref:`check_motion <auto_check_motion>` for intelligent stop timing.  
- Helpful for safety-aware automation where real-time conditions require mid-motion intervention.  
