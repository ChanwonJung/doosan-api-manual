.. _auto_drl_pause:

drl_pause (Auto Mode)
------------------------------------------
This section explains how to use :ref:`drl_pause <drl_pause>`  
during **Auto (Run)** operations to temporarily **pause** a running  
**DRL (Doosan Robotics Language)** program.

Pausing halts robot motion and task execution at the current instruction,  
allowing operators or external systems to perform checks, adjustments,  
or synchronizations without stopping the entire program.

**Typical usage**

- Pause the robot during inspection, positioning correction, or vision checks.  
- Temporarily stop movement when a sensor condition requires validation.  
- Integrate with HMI/PLC “PAUSE” buttons for operator workflows.  
- Halt robot motion safely without terminating the DRL program.  

.. Note::

   - Can only be called when the program is currently **running**.  
   - The program remains paused until :ref:`drl_resume <auto_drl_resume>` is invoked.  

**Example: Pausing a Running DRL Program**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Check whether a DRL program is running
       if (drfl.get_program_state() == DRL_PROGRAM_STATE_PLAY) {

           // 2) Pause program execution
           if (!drfl.drl_pause()) {
               printf("Failed to pause DRL program.\n");
               return -1;
           }

           printf("DRL program paused.\n");
       } else {
           printf("No running DRL program.\n");
       }

       return 0;
   }

In this example, the robot pauses only if a DRL task is currently in  
the **PLAY (running)** state, ensuring safe and predictable interruption  
during Auto Mode operation.

**Tips**

- Combine with :ref:`drl_resume <auto_drl_resume>` for pause/resume workflows.  
- Helps during manual checks, recalibration steps, or workstation alignment.  
- DRL program execution fully stops but is not terminated.  
- Effective in collaborative setups requiring temporary human intervention.  
