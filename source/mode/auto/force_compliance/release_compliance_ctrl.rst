.. _auto_release_compliance_ctrl:

release_compliance_ctrl (Auto Mode)
------------------------------------------
This section explains how to use :ref:`release_compliance_ctrl <release_compliance_ctrl>`  
during **Auto (Run)** operations to terminate **compliance control**  
and return the robot to standard **position control mode**.  

It is typically used after performing tasks requiring compliance, such as **force-controlled assembly** or **surface fitting**,  
to transition back to standard motion commands in automated processes.

**Typical usage**

- Exit compliance or force-control mode after completing an automated task, such as assembly or insertion.  
- Restore position control for subsequent automated motion commands.  
- Maintain the robot’s **current pose** after compliance release during automated sequences.  
- Safely finalize automated tasks, ensuring the robot is in position control mode.

.. Note::

    - No input parameters are required.  
    - Use after any compliance or force-control task to revert to position control in automated operations.  
    - Once released, the robot will hold its **current position** under standard motion mode.

**Example: Restoring Position Control After Compliance in Automated Process**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Auto mode active, servo ON

       // 1) Move to initial pose in AUTO mode
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Activate compliance control for automated task (e.g., assembly)
       float stiffBase[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(stiffBase, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 3) Perform an automated process (e.g., insertion or fitting)
       // (Assume process logic here)

       // 4) Release compliance control and return to position control mode
       if (drfl.release_compliance_ctrl())
           printf("Compliance control released — robot now under position control.\n");
       else
           printf("Failed to release compliance control.\n");

       return 0;
   }

In this example, compliance control is activated for an automated task (e.g., assembly or insertion),  
and then released to resume position-controlled operation.  
This allows the robot to maintain its current pose once compliance mode is terminated during automated processes.

**Tips**

- Always call this function **after completing compliance or force-based tasks** in automated systems.  
- Use it before transitioning to new automated motion tasks or starting a new automated cycle.  
- To re-enable compliance control, call :ref:`task_compliance_ctrl <auto_task_compliance_ctrl>` again.  
- Combine with :ref:`set_stiffnessx <auto_set_stiffnessx>` for smooth stiffness transitions in automated operations.  
- Ensure the robot is stationary or in a controlled position before releasing compliance to avoid sudden movements during automation.
