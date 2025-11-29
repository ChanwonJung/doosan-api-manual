.. _release_force:

release_force
------------------------------------------
This function gradually reduces the **target force and torque values** to zero over the specified transition time  
and returns the robot’s control mode to **adaptive position control**.  

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 953)

.. code-block:: cpp

   bool release_force(float fTargetTime = 0.f) {
       return _release_force(_rbtCtrl, fTargetTime);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetTime
     - float
     - 0
     - Duration [sec] for reducing the target force to zero. |br|
       Range: **0–1.0** (linear interpolation over time).

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

**Example A — Manual Mode (Force Release After Hand-Guiding)**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established and servo ON
       // - Manual (Teach) mode active

       // 1) Set reference coordinate
       drfl.set_ref_coord(COORDINATE_SYSTEM_TOOL);

       // 2) Move to start pose
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 3) Enable compliance mode
       float stiff[6] = {1500.f, 1500.f, 1000.f, 150.f, 150.f, 150.f};
       drfl.task_compliance_ctrl(stiff);

       // 4) Apply downward force (+Z)
       float fTarget[6] = {0.f, 0.f, 20.f, 0.f, 0.f, 0.f};
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);

       // 5) Gradually release the applied force
       drfl.release_force(0.4f);

       // 6) End compliance control
       drfl.release_compliance_ctrl();

       printf("Force released and compliance ended.\n");
       return 0;
   }

**Example B — Auto Mode (Force-Controlled Task Completion)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Force control previously enabled during a process

   // 1) Apply a downward insertion force
   float fTarget[6] = {0.f, 0.f, 30.f, 0.f, 0.f, 0.f};
   unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
   drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);

   // 2) Execute insertion motion
   float p_insert[NUM_TASK] = {550.f, 200.f, 90.f, 180.f, 0.f, 0.f};
   drfl.movel(p_insert, (float[2]){50.f, 20.f}, (float[2]){200.f, 80.f});
   drfl.mwait();

   // 3) Smoothly release the applied force after completion
   drfl.release_force(0.4f);

   // 4) Restore normal control and continue next motion
   drfl.release_compliance_ctrl();

   printf("Force smoothly released and returned to position mode.\n");

**Notes & Best Practices**

- Always call ``release_force()`` before ``release_compliance_ctrl()`` to ensure a stable transition.  
- Use **short transition times (0.3–0.5 s)** for smooth and safe force decay.  
- Avoid releasing force suddenly when under external load — ensure stable contact conditions first.  
- Combine with :ref:`set_desired_force <set_desired_force>` and :ref:`task_compliance_ctrl <task_compliance_ctrl>`  
  for full compliance-force control workflows.  
- In Auto mode, it’s recommended to wait for motion completion (e.g., using ``mwait()``) before releasing the force.
