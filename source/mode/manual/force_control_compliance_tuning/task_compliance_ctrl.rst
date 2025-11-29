.. _manual_task_compliance_ctrl:

task_compliance_ctrl (Manual Mode)
------------------------------------------
This section explains how to use :ref:`task_compliance_ctrl <task_compliance_ctrl>`  
during **Manual (Teach)** operations to activate **Cartesian compliance control**.  
This function allows the robot arm to be guided safely by adjusting stiffness along translational and rotational axes,  
enabling smooth hand-guiding, insertion, or surface-following behavior.

It is one of the most fundamental APIs for compliant control — providing safe human–robot interaction  
by modulating how the robot reacts to external forces.

**Typical usage**

- Enable compliance mode to allow **hand-guiding** or **force-assisted alignment**.  
- Perform **surface following**, **assembly fitting**, or **teaching by demonstration** (PbD).  
- Reduce stiffness for **softer contact** and **safe physical guidance**.  
- Combine with :ref:`set_desired_force <manual_set_desired_force>` for **hybrid force–compliance control**.  
- End compliance using :ref:`release_compliance_ctrl <manual_release_compliance_ctrl>` when manual alignment is complete.

.. Note::

  - Use ``COORDINATE_SYSTEM_TOOL`` for tool-aligned compliance or ``BASE`` for global stiffness control.  
  - Returns **1** on success, **0** on failure.

**Example: Enable Cartesian Compliance for Hand-Guiding**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Robot connected and servo ON
       // - Manual (Teach) mode active
       // - Operator ready to guide robot by hand

       // 1) Move to a safe position before enabling compliance
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Define target stiffness (lower values → softer behavior)
       float stiffness[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};

       // 3) Activate Cartesian compliance in TOOL coordinate system
       if (drfl.task_compliance_ctrl(stiffness, COORDINATE_SYSTEM_TOOL, 0.3f))
           printf("Compliance mode enabled. Robot is now compliant.\n");
       else {
           printf("Failed to activate compliance control.\n");
           return -1;
       }

       // (The robot can now be hand-guided safely.)
       printf("You can manually guide the robot arm.\n");

       // 4) End compliance control and return to position mode
       drfl.release_compliance_ctrl();
       printf("Compliance control released.\n");

       return 0;
   }

In this example, the robot moves to a safe pose and then activates Cartesian compliance  
with moderate stiffness values. While compliance is active, the arm becomes compliant  
and can be manually guided or adjusted by the operator.  
After completion, ``release_compliance_ctrl()`` restores standard position control.

**Tips**

- Recommended stiffness for hand-guiding: **1000–3000 N/m**.  
- Use TOOL frame for most alignment and insertion operations.  
- Gradually apply stiffness transitions (0.2–0.5 s) to prevent jerky motion.  
- Always release compliance before executing new motion commands.  
- Combine with :ref:`set_stiffnessx <manual_set_stiffnessx>`  
  to fine-tune compliance during manual teaching or calibration.
