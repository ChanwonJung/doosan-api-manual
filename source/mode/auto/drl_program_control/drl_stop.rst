.. _auto_drl_stop:

drl_stop (Auto Mode)
------------------------------------------
This section explains how to use :ref:`drl_stop <drl_stop>`  
during **Auto (Run)** operations to stop a currently running  
**DRL (Doosan Robotics Language)** program.

It is typically used to interrupt a task sequence triggered by  
:drl_start:, allowing external systems (PC, PLC, MES, vision logic, safety logic)  
to control when the robot should safely or immediately halt DRL execution.

**Typical usage**

- Stop an active DRL program when a cycle must be interrupted.  
- Apply a **Slow Stop** for smooth deceleration during normal task transitions.  
- Apply a **Quick Stop** when urgent interruption is required (e.g., product misalignment, sensor triggers).  
- Integrate with external UI/PLC buttons (STOP / EMERGENCY STOP substitutes).  

.. Note::

   - ``0`` → Slow Stop (gradual deceleration)  
   - ``1`` → Quick Stop (immediate halt)  
   - The function only succeeds if a DRL program is currently running or paused.  

**Example: Performing a Quick Stop During a Running DRL Task**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Check DRL program execution state
       DRL_PROGRAM_STATE state = drfl.get_program_state();

       // 2) Stop only if the program is running or paused
       if (state == DRL_PROGRAM_STATE_PLAY ||
           state == DRL_PROGRAM_STATE_HOLD) {

           // Quick Stop (1): immediate halt
           if (!drfl.drl_stop(1)) {
               printf("Failed to stop DRL program.\n");
               return -1;
           }

           printf("DRL program stopped (Quick Stop).\n");
       } else {
           printf("No active DRL program.\n");
       }

       return 0;
   }

In this example, the program checks the current DRL execution state  
and issues a **Quick Stop** only when a DRL program is running or paused.  
This allows external logic to safely interrupt automatic task sequences.

**Tips**

- Use **Slow Stop (0)** during routine process changes to avoid abrupt motion.  
- Use **Quick Stop (1)** when immediate intervention is needed.  
- Combine with :ref:`drl_pause <auto_drl_pause>` for smoother step-wise control.  
- Log stop reasons (sensor trigger, operator request, safety event) for debugging and traceability.  
