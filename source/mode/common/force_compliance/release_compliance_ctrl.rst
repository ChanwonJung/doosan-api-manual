.. _release_compliance_ctrl:

release_compliance_ctrl
------------------------------------------
This function terminates the active **compliance control** mode and restores the robot to **standard position control**  
while maintaining its current position.  

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 950)

.. code-block:: cpp

   bool release_compliance_ctrl() {
       return _release_compliance_ctrl(_rbtCtrl);
   };

**Parameter** |br|
None

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

**Example A — Manual Mode (End of Hand-Guiding or Alignment)**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connected and servo ON
       // - Manual (Teach) mode active

       // 1) Move to initial pose
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Enable compliance for hand-guiding
       float stiff[6] = {2500.f, 2500.f, 2500.f, 150.f, 150.f, 150.f};
       drfl.task_compliance_ctrl(stiff, COORDINATE_SYSTEM_TOOL, 0.0f);
       printf("Compliance active. Hand-guide the robot.\n");

       // 3) Adjust stiffness during guidance if necessary
       float adjStiff[6] = {1500.f, 1500.f, 1000.f, 100.f, 100.f, 100.f};
       drfl.set_stiffnessx(adjStiff, COORDINATE_SYSTEM_TOOL, 0.4f);

       // 4) Release compliance and return to position control
       if (drfl.release_compliance_ctrl())
           printf("Compliance released. Robot now under position control.\n");
       else
           printf("Failed to release compliance control.\n");

       return 0;
   }

**Example B — Auto Mode (After Force-Controlled Task)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Compliance and force control previously enabled

   // 1) Perform a compliant insertion motion
   float fTarget[6] = {0.f, 0.f, 25.f, 0.f, 0.f, 0.f};
   unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
   drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);

   float p_insert[NUM_TASK] = {550.f, 200.f, 95.f, 180.f, 0.f, 0.f};
   drfl.movel(p_insert, (float[2]){50.f, 20.f}, (float[2]){200.f, 80.f});
   drfl.mwait();

   // 2) Release the applied force gradually
   drfl.release_force(0.4f);

   // 3) Restore position control for the next operation
   if (drfl.release_compliance_ctrl())
       printf("Compliance control successfully released.\n");
   else
       printf("Compliance release failed.\n");

**Notes & Best Practices**

- Always call ``release_compliance_ctrl()`` after completing any force or compliance-based operation.  
- Recommended sequence: ``release_force() → release_compliance_ctrl()`` for smooth and stable recovery.  
- After release, the robot **maintains its current pose** and resumes standard servo position control.  
- To re-enable compliance, call :ref:`task_compliance_ctrl <task_compliance_ctrl>` again with new stiffness parameters.  
- Use :ref:`set_stiffnessx <set_stiffnessx>` before releasing compliance to gradually return stiffness to default levels in Auto mode.
