.. _manual_release_compliance_ctrl:

release_compliance_ctrl (Manual Mode)
------------------------------------------
This section explains how to use :ref:`release_compliance_ctrl <release_compliance_ctrl>`  
during **Manual (Teach)** operations to terminate **compliance control**  
and return the robot to standard **position control mode**.  
It is typically used after completing hand-guiding, force-tuned alignment,  
or compliant interaction tasks during teaching.

**Typical usage**

- Exit compliance or force-control mode after teaching or calibration.  
- Restore position control for subsequent jogging or motion commands.  
- Maintain the robot’s **current pose** after compliance release.  
- Safely finalize manual contact tasks such as surface alignment or assembly fitting.

.. Note::

    - Use after any compliance or force-control task to revert to position control.  
    - Once released, the robot will hold its **current position** under standard motion mode.

**Example: Restore Position Control After Compliance Adjustment**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established, servo ON
       // - Manual (Teach) mode active

       // 1) Move to initial pose
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Activate compliance control
       float stiffBase[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(stiffBase, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 3) Adjust stiffness values
       float stiffAdj[6] = {1000.f, 1500.f, 2000.f, 150.f, 150.f, 150.f};
       drfl.set_stiffnessx(stiffAdj, COORDINATE_SYSTEM_TOOL, 0.5f);

       // 4) End compliance control and return to position control
       if (drfl.release_compliance_ctrl())
           printf("Compliance control released — robot now under position control.\n");
       else
           printf("Failed to release compliance control.\n");

       return 0;
   }

In this example, compliance control is first activated for stiffness adjustment,  
then released to resume position-controlled operation.  
The robot maintains its current pose once compliance mode is terminated.

**Tips**

- Always call this function **after completing compliance or force tasks**.  
- Use it before starting new motion or teaching sequences.  
- To re-enable compliance control, call :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>` again.  
- Combine with :ref:`set_stiffnessx <manual_set_stiffnessx>` for smooth stiffness transitions.  
- Ensure the robot is stationary before releasing to prevent sudden movements.
