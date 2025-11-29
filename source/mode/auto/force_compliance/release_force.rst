.. _auto_release_force:

release_force (Auto Mode)
------------------------------------------
This section explains how to use :ref:`release_force <release_force>`  
during **Auto (Run)** operations to safely **reduce or remove applied force control**.  
It gradually decreases the current target force to zero over a defined transition time,  
then restores the robot to standard **adaptive position control** mode.

This function is typically used after executing a constant or directional force command  
via :ref:`set_desired_force <auto_set_desired_force>` to ensure smooth and stable recovery in automated processes.

**Typical usage**

- Smoothly release the currently applied **force or torque** after automated pressing, insertion, or contact tasks.  
- Prevent sudden motion or vibration when switching from force control to position control in automated workflows.  
- Integrate into automated processes where **force-controlled actions** are followed by **position-controlled tasks**.  
- Combine with :ref:`release_compliance_ctrl <auto_release_compliance_ctrl>` to fully disengage both force and compliance control in automation.

.. Note::

    - Recommended range: **0.3–0.5 seconds** for smooth transitions in automated cycles.  
    - Should be called **before** releasing compliance control or starting new motion commands in automated operations.

**Example: Gradual Force Release After Automated Insertion Task**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Auto mode active
       // - Servo ON and force control available

       // 1) Set reference coordinate to TOOL
       drfl.set_ref_coord(COORDINATE_SYSTEM_TOOL);

       // 2) Move to initial pose
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 3) Apply compliance control
       float stiff[6] = {1000.f, 500.f, 500.f, 100.f, 100.f, 100.f};
       drfl.task_compliance_ctrl(stiff);

       // 4) Apply downward force (+Z) of 15 N
       float fTarget[6] = {0.f, 0.f, 15.f, 0.f, 0.f, 0.f};
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);

       // 5) Gradually release the applied force over 0.4 seconds
       drfl.release_force(0.4f);

       // 6) Disable compliance control and return to position control
       drfl.release_compliance_ctrl();

       return 0;
   }

In this example, the robot applies a **15 N force** along the TOOL’s +Z axis,  
then reduces it gradually over **0.4 seconds** using ``release_force()``.  
This ensures stable detachment from the contact surface and safe transition back to position control in automated operations.

**Tips**

- Always use ``release_force()`` before calling :ref:`release_compliance_ctrl <auto_release_compliance_ctrl>`.  
- Apply short transition times (0.3–0.5 s) for smooth force decay in automated tasks.  
- Check for unexpected external loads before releasing the force.  
- Combine with :ref:`set_desired_force <auto_set_desired_force>` for full force-control cycles in automated workflows.  
- Useful for **automated press-fit**, **surface contact**, or **insertion** operations with controlled disengagement.
