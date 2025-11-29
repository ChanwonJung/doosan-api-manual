.. _manual_set_stiffnessx:

set_stiffnessx (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_stiffnessx <set_stiffnessx>`  
during **Manual (Teach)** operations to modify the robot’s **Cartesian stiffness**  
for compliant or force-assisted motion.  
It linearly transitions from the current stiffness to the new target stiffness  
within the specified time duration, enabling smooth adjustment of robot rigidity.

This function is commonly used during **hand-guiding**, **surface contact tuning**,  
and **assembly teaching** to make the robot either softer or stiffer in selected axes.

**Typical usage**

- Adjust stiffness dynamically during manual guidance or contact testing.  
- Fine-tune compliance behavior for **safe interaction** with humans or the environment.  
- Apply **lower stiffness** for compliant movement or **higher stiffness** for stable precision positioning.  
- Combine with :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>` to adapt robot flexibility in real-time.

.. Note::
  
  - Always ensure compliance control is active before adjusting stiffness.

**Example: Adjust Cartesian Stiffness in TOOL Coordinates**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established, servo ON
       // - Manual (Teach) mode active

       // 1) Move to a safe position
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Enable base compliance control
       float baseStiff[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(baseStiff, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 3) Adjust stiffness over 0.5 seconds
       float newStiff[6] = {1000.f, 1500.f, 2000.f, 150.f, 150.f, 150.f};
       drfl.set_stiffnessx(newStiff, COORDINATE_SYSTEM_TOOL, 0.5f);

       // 4) Finish compliance and return to position control
       drfl.release_compliance_ctrl();

       printf("Stiffness adjusted successfully.\n");
       return 0;
   }

In this example, the robot transitions smoothly from a stiff configuration  
to a softer one by lowering stiffness values along each axis.  
This adjustment allows the user to safely hand-guide or fine-tune the robot’s compliance  
while maintaining stable and responsive control.

**Tips**

- Lower stiffness → **more compliant**, safer for hand guidance.  
- Higher stiffness → **more rigid**, suitable for precise motion.  
- Apply stiffness adjustments gradually for realistic compliance tuning.  
- Use ``COORDINATE_SYSTEM_TOOL`` for tool-aligned operations (e.g., polishing).  
- Combine with :ref:`release_compliance_ctrl <manual_release_compliance_ctrl>`  
  to return to position control after manual stiffness tuning.
