.. _auto_set_desired_force:

set_desired_force (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_desired_force <set_desired_force>`  
during **Auto (Run)** operations to apply a **target force or torque** along specific axes.  
It linearly transitions from the current force value to the desired one over the specified time,  
enabling controlled force application in automated tasks.

This function is commonly used in **automated assembly**, **press-fitting**, **force-based insertion**,  
and **force feedback tasks** to ensure precision and safety during automated processes.

**Typical usage**

- Apply a defined **force or torque** in one or more axes during automated operations.  
- Perform **press-fit**, **insertion**, or **force validation** tasks during automatic operation.  
- Combine with :ref:`task_compliance_ctrl <auto_task_compliance_ctrl>` to ensure stable force control during motion.  
- Use direction masking to control only selected axes (e.g., apply force only along Z-axis during assembly).

.. Note::

    - Force direction and reference frame depend on ``eForceReference`` (TOOL or BASE).

**Example: Apply 20 N Downward Force Along Z-Axis in Auto Mode**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Auto mode active
       // - Servo ON and force control calibrated

       // 1) Move to initial pose
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Apply downward force (+Z) of 20 N in TOOL frame
       float fTarget[6] = {0.f, 0.f, 20.f, 0.f, 0.f, 0.f};  // 20 N push along +Z
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};           // control Z-axis only

       // 3) Apply force smoothly over 0.3 seconds
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f, FORCE_MODE_ABSOLUTE);

       // ... perform automated insertion or calibration under force control ...

       // 4) Release force and return to position control
       drfl.release_force(0.2f);
       drfl.release_compliance_ctrl();

       return 0;
   }

In this example, the robot applies a **+20 N** downward force along the TOOL Z-axis over **0.3 seconds**.  
It then releases both force and compliance control for a smooth transition to position control.  
This ensures precision during **automated insertion** or **force-based assembly** tasks.

**Tips**

- Start with **moderate stiffness values** (1000–3000 N/m) to ensure stable force application.  
- Use **direction masks** to control force along the relevant axes only (e.g., Z-axis for insertion).  
- Prefer ``COORDINATE_SYSTEM_TOOL`` for tool-aligned forces, and ``COORDINATE_SYSTEM_BASE`` for global forces.  
- Always call :ref:`release_force <auto_release_force>` before ending force control with :ref:`release_compliance_ctrl <auto_release_compliance_ctrl>`.  
- Gradual force activation (0.2–0.5 s) prevents abrupt or unsafe force application in automated workflows.
