.. _auto_task_compliance_ctrl:

task_compliance_ctrl (Auto Mode)
------------------------------------------
This section explains how to use :ref:`task_compliance_ctrl <task_compliance_ctrl>`  
during **Auto (Run)** operations to activate **Cartesian compliance control**  
for force-assisted or compliance-based tasks.  
This function allows the robot to adjust its stiffness dynamically for specific tasks,  
enabling safe interaction with objects, materials, or the environment.

In **Auto Mode**, this function is useful for tasks that require force control or compliant motion,  
such as automated assembly, insertion, or material handling.

**Typical usage**

- Enable compliance mode to allow **force-assisted movement** during automated tasks.  
- Perform **surface following**, **insertion**, or **contact-based alignment** in automated operations.  
- Adjust stiffness dynamically for **safe interaction** with parts or tools.  
- Combine with :ref:`set_desired_force <auto_set_desired_force>` to control both force and compliance for automated tasks.  
- Use :ref:`release_compliance_ctrl <auto_release_compliance_ctrl>` to revert to standard position control after the task is complete.

.. Note::

  - Typical stiffness range: |br|
    - Translational: 0–20000 N/m |br| 
    - Rotational: 0–400 N·m/rad  
  - Use ``COORDINATE_SYSTEM_TOOL`` for tool-aligned compliance or ``BASE`` for global compliance control.  

**Example: Enable Cartesian Compliance for Automated Insertion**

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

       // 2) Enable compliance control with base stiffness
       float baseStiff[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(baseStiff, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 3) Adjust stiffness dynamically for insertion task
       float newStiff[6] = {1000.f, 1500.f, 2000.f, 150.f, 150.f, 150.f};
       drfl.set_stiffnessx(newStiff, COORDINATE_SYSTEM_TOOL, 0.5f);

       // 4) Finalize insertion task and return to position control
       drfl.release_compliance_ctrl();

       printf("Compliance mode enabled for automated insertion.\n");
       return 0;
   }

In this example, the robot transitions to a compliant state, adjusts stiffness for optimal insertion,  
and then releases compliance to return to standard position control after the task.

**Tips**

- Use **moderate stiffness** (e.g., 1000–3000 N/m) for safe and controlled insertion or assembly tasks.  
- Apply **short transition times (0.3–0.5 s)** for smooth and responsive stiffness changes.  
- **COORDINATE_SYSTEM_TOOL** is recommended for force applications related to tool movement or part insertion.  
- Ensure compliance control is activated before performing tasks that involve **force or contact-based control**.  
- Combine with :ref:`set_desired_force <auto_set_desired_force>` to manage force control in conjunction with compliance.
