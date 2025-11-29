.. _manual_set_desired_force:

set_desired_force (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_desired_force <set_desired_force>`  
during **Manual (Teach)** operations to apply a **target force or torque** along specific axes.  
It linearly transitions from the current force value to the desired one over the specified time,  
allowing controlled and stable activation of **force control**.

This function is typically used during **pressing**, **contact testing**, **surface alignment**,  
or **assembly calibration** to apply precise forces while maintaining compliance safety.

**Typical usage**

- Apply a defined **force or torque** in one or more axes while the robot is in compliance mode.  
- Perform **press-fit**, **pushing**, or **holding** operations during manual teaching.  
- Combine with :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>`  
  to ensure stable behavior under external force.  
- Use direction masking to control only selected axes (e.g., apply force only along Z).

.. Note::

  - Force direction and reference frame depend on ``eForceReference`` (TOOL or BASE).

**Example: Apply 20 N Downward Force Along Z-Axis**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Servo ON
       // - Manual (Teach) mode active

       // 1) Enable compliance mode with base stiffness
       float stiff[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(stiff, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 2) Define target force (push along Z only)
       float fTarget[6] = {0.f, 0.f, 20.f, 0.f, 0.f, 0.f};   // 20 N push along +Z
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};            // control Z-axis only

       // 3) Apply target force smoothly over 0.3 s
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f, FORCE_MODE_ABSOLUTE);

       // ... perform manual pressing or calibration under force control ...

       // 4) Release force and return to normal control
       drfl.release_force(0.2f);
       drfl.release_compliance_ctrl();

       return 0;
   }

In this example, the robot activates compliance mode,  
applies a **+20 N** downward force along the TOOL Z-axis over **0.3 s**,  
then releases both force and compliance control for a smooth recovery.  
This approach ensures stable contact and safe disengagement during manual force teaching.

**Tips**

- Start with **moderate stiffness values** (1000–3000 N/m) for stable contact.  
- Use **direction masks** to restrict control to relevant axes.  
- Prefer ``COORDINATE_SYSTEM_TOOL`` for end-effector-aligned forces.  
- Always call :ref:`release_force <manual_release_force>`  
  before ending compliance control with :ref:`release_compliance_ctrl <manual_release_compliance_ctrl>`.  
- Gradual activation (0.2–0.5 s) prevents jerky or unsafe force application during teaching.
