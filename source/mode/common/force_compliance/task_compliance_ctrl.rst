.. _task_compliance_ctrl:

task_compliance_ctrl
------------------------------------------
This function starts **task-space compliance control (Cartesian stiffness control)** in the specified reference coordinate system.  

To end compliance control, use :ref:`release_compliance_ctrl <release_compliance_ctrl>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 947)

.. code-block:: cpp

   bool task_compliance_ctrl(float fTargetStiffness[NUM_TASK],
                             COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL,
                             float fTargetTime = 0.f) {
       return _task_compliance_ctrl(_rbtCtrl, fTargetStiffness, eForceReference, fTargetTime);
   };

**Parameter**

.. list-table::
   :widths: 22 22 18 38
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetStiffness
     - float[6]
     - ``[3000, 3000, 3000, 200, 200, 200]``
     - Stiffness for XYZ (translation) and Rx/Ry/Rz (rotation). |br|
       Larger: stiffer (less compliant) |br|
       Smaller values: softer (more compliant) |br|
       Units: **N/m** (translation) and **N·m/rad** (rotation).
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Reference coordinate frame for stiffness control (e.g., TOOL, BASE, WORLD).
   * - fTargetTime
     - float
     - 0
     - Transition duration [sec] for stiffness change (range 0–1). |br|
       Linear interpolation is used during the specified time.

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

**Example A — Manual (Teach) Hand-Guiding**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Manual (Teach) mode active
       // - Servo power ON

       // 1) Move to a safe position before enabling compliance
       float q0[6] = { 0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f };
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Define stiffness for each axis (lower = more compliant)
       float stiffness[6] = { 2500.f, 2500.f, 2500.f, 150.f, 150.f, 150.f };

       // 3) Enable compliance control in TOOL frame
       if (!drfl.task_compliance_ctrl(stiffness, COORDINATE_SYSTEM_TOOL, 0.1f)) {
           printf("Failed to start compliance control.\n");
           return -1;
       }

       printf("Compliance active. The arm can now be hand-guided safely.\n");

       // 4) Release compliance after teaching
       drfl.release_compliance_ctrl();
       printf("Compliance control released.\n");
       return 0;
   }

**Example B — Auto Mode (Insertion or Surface Contact Task)**

.. code-block:: cpp

   // 1) Move to approach position
   float p_app[NUM_TASK] = {550.f, 200.f, 150.f, 180.f, 0.f, 0.f};
   drfl.movel(p_app, (float[2]){150.f, 30.f}, (float[2]){400.f, 150.f});
   drfl.mwait();

   // 2) Enable compliance (soft in Z and rotation)
   float k_soft[NUM_TASK] = {2500.f, 2500.f, 1200.f, 100.f, 100.f, 100.f};
   if (!drfl.task_compliance_ctrl(k_soft, COORDINATE_SYSTEM_TOOL, 0.2f)) {
       printf("Failed to enable compliance.\n");
   }

   // 3) Execute insertion motion under compliance
   float p_down[NUM_TASK] = {550.f, 200.f, 90.f, 180.f, 0.f, 0.f};
   drfl.movel(p_down, (float[2]){40.f, 15.f}, (float[2]){150.f, 60.f});
   drfl.mwait();

   // 4) Disable compliance after insertion
   drfl.release_compliance_ctrl();
   drfl.mwait();

   // 5) Continue with precision motion
   float p_final[NUM_TASK] = {550.f, 200.f, 85.f, 180.f, 0.f, 0.f};
   drfl.movel(p_final, (float[2]){60.f, 20.f}, (float[2]){300.f, 120.f});
   drfl.mwait();

**Notes & Best Practices**

- Activate compliance **only during necessary operations**. Disable it before executing fast or high-precision movements using :ref:`release_compliance_ctrl <release_compliance_ctrl>`.  
- Use ``mwait()`` to ensure motion completion before switching between position and compliance control.  
- Recommended stiffness values: XYZ **1500–2500**, rotations **100–200**.  
- Use **TOOL** coordinate system for hand-guiding or alignment tasks.  
- Use **BASE** coordinate system when compliance direction should follow the workspace axes.
