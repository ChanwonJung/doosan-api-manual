.. _manual_mwait:

mwait (Manual Mode)
------------------------------------------
This section explains how to use :ref:`mwait <mwait>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, it is frequently used in teaching to **synchronize** motion steps  
and ensure the robot has fully stopped before proceeding to the next action.

**Typical usage**

- Wait until all current motions (e.g., jog, move, or blend) are completed.  
- Prevent overlapping commands during step-by-step teaching.  
- Used after :ref:`stop <stop>`, :ref:`move_pause <move_pause>`, or any manual jogging action.

.. Note::

    ``mwait()`` blocks program execution until the controller reports the robot is stationary.  
    This is useful in manual teaching sequences where the operator wants to **guarantee motion stability**  
    before performing a visual check or starting the next movement.

**Example: Step-by-step Manual Teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are active.

       // 1) Move to an initial position
       float pose1[6] = {500.0f, 200.0f, 400.0f, 180.0f, 0.0f, 90.0f};
       drfl.movel(pose1, 50, 50);
       drfl.mwait();  // wait until motion completes

       // 2) Perform a short jog for fine adjustment
       drfl.jog(JOG_AXIS_TASK_Z, MOVE_REFERENCE_TOOL, -5.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(500));
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();  // ensure stable stop before the next move

       // 3) Proceed to next taught position
       float pose2[6] = {550.0f, 250.0f, 420.0f, 180.0f, 0.0f, 90.0f};
       drfl.movel(pose2, 40, 40);
       drfl.mwait();

       return 0;
   }

**Tips**

- Always call ``mwait()`` before issuing the next motion to avoid command overlap.  
- Especially useful when combining manual jogs and automatic moves in a mixed teaching sequence.  
- When integrating with external control (e.g., GUI or voice command), ``mwait()`` ensures safe sequencing.
