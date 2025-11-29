.. _auto_set_stiffnessx:

set_stiffnessx (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_stiffnessx <set_stiffnessx>`  
during **Auto (Run)** operations to adjust the robot’s **Cartesian stiffness**  
for compliance control or force-assisted tasks in automated environments.  
It linearly transitions from the current stiffness to the desired one over the specified time,  
enabling smooth adjustment of robot rigidity for optimized performance.

This function is commonly used in **automated assembly**, **force-based insertion**,  
**surface interaction**, or **material handling** tasks to adjust the robot’s rigidity  
based on task requirements, ensuring stable and safe performance.

**Typical usage**

- Adjust stiffness during automated tasks requiring **force control** or **compliance**.  
- Fine-tune the robot's stiffness for **safe interaction** with materials or the environment.  
- Apply **lower stiffness** for compliant movement or **higher stiffness** for precise, rigid motion.  
- Combine with :ref:`task_compliance_ctrl <auto_task_compliance_ctrl>` to adapt robot flexibility in real-time for automated processes.

.. Note::

  - Translational stiffness range: **0–20000 N/m**, rotational stiffness range: **0–400 N·m/rad**.  

**Example: Adjust Cartesian Stiffness in TOOL Coordinates for Automated Insertion**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established, servo ON
       // - Auto mode active

       // 1) Move to a safe position for insertion
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Enable base compliance control for insertion
       float baseStiff[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(baseStiff, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 3) Adjust stiffness for fine positioning in insertion task
       float newStiff[6] = {1000.f, 1500.f, 2000.f, 150.f, 150.f, 150.f};
       drfl.set_stiffnessx(newStiff, COORDINATE_SYSTEM_TOOL, 0.5f);

       // 4) Finalize task and return to standard position control
       drfl.release_compliance_ctrl();

       printf("Stiffness adjusted successfully for insertion task.\n");
       return 0;
   }

In this example, the robot transitions smoothly from a stiffer configuration  
to a softer one to optimize for **force-based insertion**.  
This adjustment ensures stable and compliant behavior while maintaining precise control during automated tasks.

**Tips**

- Lower stiffness → **more compliant**, suitable for delicate operations like insertion or contact tasks.  
- Higher stiffness → **more rigid**, ideal for precise, rigid motion in automated assembly.  
- Apply stiffness adjustments gradually for smoother transitions in automated workflows.  
- Use **COORDINATE_SYSTEM_TOOL** for tool-aligned force applications (e.g., insertion, pressing).  
- Combine with :ref:`release_compliance_ctrl <auto_release_compliance_ctrl>`  
  to return to standard position control after automated stiffness tuning.
