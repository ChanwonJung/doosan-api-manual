.. _auto_drl_resume:

drl_resume (Auto Mode)
------------------------------------------
This section explains how to use :ref:`drl_resume <drl_resume>`  
during **Auto (Run)** operations to **resume** a paused  
**DRL (Doosan Robotics Language)** program.

It continues execution from the exact point where  
:ref:`drl_pause <auto_drl_pause>` stopped the task, making it useful for  
operator-driven pause/resume flows, vision-based inspections,  
or external system synchronization.

**Typical usage**

- Resume task execution after a temporary pause for inspection or alignment.  
- Continue a DRL routine after checking sensor conditions mid-cycle.  
- Integrate with HMI/PLC “PAUSE / RESUME” buttons for operator workflows.  
- Recover the robot after momentary workflow adjustments without restarting the task.  

.. Note::

   - Can only be used when the program is in the **HOLD (paused)** state.  
   - The function fails if no DRL program is paused.  

**Example: Resuming a Paused DRL Task**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Confirm that the DRL program is paused
       if (drfl.get_program_state() == DRL_PROGRAM_STATE_HOLD) {

           // 2) Resume the DRL program
           if (!drfl.drl_resume()) {
               printf("Failed to resume DRL program.\n");
               return -1;
           }

           printf("DRL program resumed.\n");
       } else {
           printf("DRL program is not paused.\n");
       }

       return 0;
   }

In this example, the DRL program resumes only when the controller reports  
that the program is currently in the **HOLD** state, enabling clean task continuation.

**Tips**

- Pair with :ref:`drl_pause <auto_drl_pause>` to build robust pause/resume controls.  
- Useful during quality checks, vision detection steps, or manual adjustments.  
- Works on both **real** and **virtual** robot systems without differences.  
- Log resume events to track operator interventions during production.  
