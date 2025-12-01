.. _set_desired_force:

set_desired_force
------------------------------------------
This function defines the **target force and torque** for each task-space axis, along with the **direction mask**,  
**transition time**, and **control mode**. It linearly transitions from the current force to the target values over ``fTargetTime``.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 952)

.. code-block:: cpp

   bool set_desired_force(float fTargetForce[NUM_TASK],
                          unsigned char iTargetDirection[NUM_TASK],
                          COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL,
                          float fTargetTime = 0.f,
                          FORCE_MODE eForceMode = FORCE_MODE_ABSOLUTE) {
       return _set_desired_force(_rbtCtrl, fTargetForce, iTargetDirection, eForceReference, fTargetTime, eForceMode);
   };

**Parameter**

.. list-table::
   :widths: 24 22 18 36
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetForce
     - float[6]
     - -
     - Target forces and torques applied along the task-space axes: **[Fx, Fy, Fz, Mx, My, Mz]**. |br|
       Units: N (translational) and N·m (rotational).
   * - iTargetDirection
     - unsigned char[6]
     - -
     - Axis mask for control |br|
       (**0**: ignore, **1**: active control). |br|
       Controls which axes respond to the commanded force.
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Coordinate system where the force is defined (e.g., TOOL, BASE, WORLD).
   * - fTargetTime
     - float
     - 0
     - Transition time [sec] for the force ramp (**0–1.0**). |br|
       Linear interpolation over this time.
   * - eForceMode
     - :ref:`FORCE_MODE <enum_force_mode>`
     - ``FORCE_MODE_ABSOLUTE``
     - Force mode (**absolute** for direct control, **relative** for incremental application).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed
   * - 1
     - Success

**Example A — Manual Mode (Pressing During Teaching)**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, Teach mode active, Servo ON.

       // 1) Enable compliance with moderate stiffness
       float stiff[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(stiff, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 2) Apply +20 N along TOOL Z axis
       float fTarget[6] = {0.f, 0.f, 20.f, 0.f, 0.f, 0.f};
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};  // control only Z
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f, FORCE_MODE_ABSOLUTE);

       printf("Force control active: +20N along TOOL Z.\n");

       // 3) Gradually release the applied force
       drfl.release_force(0.4f);
       drfl.release_compliance_ctrl();

       return 0;
   }

**Example B — Auto Mode (Force-Controlled Insertion Task)**

.. code-block:: cpp

   // Preconditions: Robot connected, Auto mode active, motion sequence running.

   // 1) Move to approach position
   float p_app[NUM_TASK] = {550.f, 200.f, 130.f, 180.f, 0.f, 0.f};
   drfl.movel(p_app, (float[2]){100.f, 30.f}, (float[2]){400.f, 150.f});
   drfl.mwait();

   // 2) Enable compliance
   float stiff[6] = {2500.f, 2500.f, 1500.f, 150.f, 150.f, 150.f};
   drfl.task_compliance_ctrl(stiff, COORDINATE_SYSTEM_TOOL, 0.1f);

   // 3) Apply downward insertion force (+Z)
   float fTarget[6] = {0.f, 0.f, 30.f, 0.f, 0.f, 0.f};
   unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
   drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.2f, FORCE_MODE_ABSOLUTE);

   // 4) Perform insertion motion
   float p_down[NUM_TASK] = {550.f, 200.f, 90.f, 180.f, 0.f, 0.f};
   drfl.movel(p_down, (float[2]){50.f, 20.f}, (float[2]){200.f, 80.f});
   drfl.mwait();

   // 5) Release force and compliance
   drfl.release_force(0.3f);
   drfl.release_compliance_ctrl();

   printf("Force-controlled insertion completed.\n");

**Notes & Best Practices**

- Apply :ref:`task_compliance_ctrl <task_compliance_ctrl>` before setting a target force to ensure stable behavior.  
- Use **direction mask** to apply force only along required axes (e.g., pressing in Z while maintaining free X/Y).  
- Set small ``fTargetTime`` (0.2–0.5s) for smooth transitions and avoid sudden motion.  
- ``FORCE_MODE_RELATIVE`` can be used to incrementally adjust existing force values during process adaptation.  
- Always call :ref:`release_force <release_force>` and :ref:`release_compliance_ctrl <release_compliance_ctrl>` after force-based tasks to restore normal control.
