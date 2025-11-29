.. _manual_check_motion:

check_motion (Manual Mode)
------------------------------------------
This section explains how to use :ref:`check_motion <check_motion>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, it is especially useful when monitoring whether a robot motion command  
is **currently active, being planned, or completed** during manual or step-based movement.

**Typical usage**

- Confirm that the robot has **completed a move command** before issuing the next.  
- Use in polling loops or step-wise teaching sequences to synchronize motions.  
- Verify the robot is **idle** before applying safety actions (e.g., :ref:`servo_off <manual_servo_off>`).

.. Note::

    - The function is non-blocking and can be safely used in tight polling loops.  
    - Recommended to combine with :ref:`mwait() <mwait>` or :ref:`get_robot_state() <get_robot_state>` for robust synchronization.

**Example: Wait until motion is complete before next move**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Servo power ON

       // 1) Execute first joint motion
       float q0[6]  = {0, 0, 90, 0, 90, 0};
       float q99[6] = {0, 0, 0, 0, 0, 0};
       drfl.movej(q0, 60, 30);

       // 2) Wait until the previous motion completes
       while (true) {
           int state = drfl.check_motion();
           if (state == 0) { // motion completed
               std::printf("[check_motion] Motion finished. Proceeding...\n");
               break;
           } else if (state == 1) {
               std::printf("[check_motion] Motion being calculated...\n");
           } else if (state == 2) {
               std::printf("[check_motion] Motion in progress...\n");
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       // 3) Start next motion after confirming completion
       drfl.movej(q99, 60, 30);

       return 0;
   }

**Tips**

- ``check_motion()`` is ideal for synchronization in **step-by-step motion tests**.  
- Always ensure the function returns **0 (idle)** before sending new move commands.  
- Useful before safety procedures like :ref:`servo_off <manual_servo_off>` or :ref:`release_protective_stop <manual_release_protective_stop>`.  
- When building teaching GUIs, use it to display motion state indicators (Idle / Calculating / Moving) in real time.
