.. _auto_get_program_state:

get_program_state (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_program_state <get_program_state>`  
during **Auto (Run)** operations to monitor the **execution state**  
of the currently running DRL (Doosan Robotics Language) program.

This function is essential for building robust automation logic,  
allowing external applications to determine whether the robot is  
**running**, **paused**, or **stopped** and respond accordingly.

**Typical usage**

- Check whether the robot is **actively executing** a DRL task.  
- Detect when a program has **paused** and trigger inspection or operator workflows.  
- Determine when a program has **stopped** due to completion or interruption.  
- Build branching logic using :ref:`drl_pause <auto_drl_pause>`,  
  :ref:`drl_resume <auto_drl_resume>`, and :ref:`drl_stop <auto_drl_stop>`.  

.. Note::

   - Typical states include:  
     - **DRL_PROGRAM_STATE_STOP**  
     - **DRL_PROGRAM_STATE_PLAY**  
     - **DRL_PROGRAM_STATE_HOLD**  
   - When no DRL program is active, the state is usually **STOP**.  

**Example: Responding to Current Program Execution State**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       DRL_PROGRAM_STATE state = drfl.get_program_state();

       switch (state) {
           case DRL_PROGRAM_STATE_PLAY:
               // If a program is running, slow stop for safe halt
               drfl.drl_stop(0);
               printf("Program was running. Requested Slow Stop.\n");
               break;

           case DRL_PROGRAM_STATE_HOLD:
               // If paused, resume execution
               drfl.drl_resume();
               printf("Program was paused. Resumed execution.\n");
               break;

           case DRL_PROGRAM_STATE_STOP:
           default:
               printf("No active DRL program.\n");
               break;
       }

       return 0;
   }

In this example, the external application checks the current  
DRL program state and performs an appropriate action—stopping, resuming,  
or simply acknowledging that no program is running.

**Tips**

- Useful for implementing “smart” automation flows that adapt to robot state.  
- Helps synchronize external systems (vision, conveyors, sensors) with robot execution.  
- Call periodically during Auto Mode for real-time program tracking.  
- Combine with :ref:`get_last_alarm <auto_get_last_alarm>`  
  to understand why a program transitioned to STOP.  
