.. _set_stiffnessx:

set_stiffnessx
------------------------------------------
This function sets **task-space stiffness** (Cartesian stiffness) values for each translational and rotational axis  
within the specified reference coordinate system.  

The stiffness transitions linearly from the current value over the specified time ``fTargetTime``.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 949)

.. code-block:: cpp

   bool set_stiffnessx(float fTargetStiffness[NUM_TASK],
                       COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL,
                       float fTargetTime = 0.f) {
       return _set_stiffnessx(_rbtCtrl, fTargetStiffness, eForceReference, fTargetTime);
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
     - -
     - Stiffness values for XYZ and Rx/Ry/Rz. |br|
       Range: 0-20000 N/m (translation), 0-400 N·m/rad (rotation). |br|
       Larger: stiffer motion |br|
       Smaller → more compliant
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Coordinate frame in which stiffness is applied (e.g., TOOL, BASE, WORLD).
   * - fTargetTime
     - float
     - 0
     - Transition time [sec] for stiffness interpolation (0-1.0) |br|
       Gradual change over the given duration.

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

**Example A — Manual Mode (Hand-Guiding Adjustment)**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established, Teach mode active, Servo ON

       // 1) Move to a safe position
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 60, 30);
       drfl.mwait();

       // 2) Start compliance mode
       float baseStiff[6] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(baseStiff, COORDINATE_SYSTEM_TOOL, 0.0f);

       // 3) Adjust stiffness for more compliance along Z and rotations
       float softStiff[6] = {2000.f, 2000.f, 1000.f, 120.f, 120.f, 120.f};
       drfl.set_stiffnessx(softStiff, COORDINATE_SYSTEM_TOOL, 0.5f);

       printf("Stiffness adjusted for smoother hand guidance.\n");

       // 4) Stop compliance
       drfl.release_compliance_ctrl();
       printf("Compliance released.\n");

       return 0;
   }

**Example B — Auto Mode (Dynamic Stiffness Tuning During Insertion)**

.. code-block:: cpp

   // 1) Approach target area
   float p_app[NUM_TASK] = {550.f, 200.f, 150.f, 180.f, 0.f, 0.f};
   drfl.movel(p_app, (float[2]){100.f, 30.f}, (float[2]){400.f, 150.f});
   drfl.mwait();

   // 2) Enable compliance
   float initStiff[NUM_TASK] = {3000.f, 3000.f, 2000.f, 200.f, 200.f, 200.f};
   drfl.task_compliance_ctrl(initStiff, COORDINATE_SYSTEM_TOOL, 0.1f);

   // 3) Reduce Z stiffness gradually for insertion
   float tunedStiff[NUM_TASK] = {3000.f, 3000.f, 800.f, 150.f, 150.f, 150.f};
   drfl.set_stiffnessx(tunedStiff, COORDINATE_SYSTEM_TOOL, 0.3f);

   // 4) Perform motion while compliant
   float p_insert[NUM_TASK] = {550.f, 200.f, 90.f, 180.f, 0.f, 0.f};
   drfl.movel(p_insert, (float[2]){40.f, 15.f}, (float[2]){200.f, 80.f});
   drfl.mwait();

   // 5) Restore normal stiffness for precision steps
   float normalStiff[NUM_TASK] = {3000.f, 3000.f, 3000.f, 200.f, 200.f, 200.f};
   drfl.set_stiffnessx(normalStiff, COORDINATE_SYSTEM_TOOL, 0.2f);
   drfl.release_compliance_ctrl();

   printf("Dynamic stiffness control completed.\n");

**Notes & Best Practices**

- Adjust stiffness dynamically to balance **force compliance and positional accuracy**.  
- Use **low stiffness (1000–2000 N/m)** for contact or alignment phases.  
- Keep transition times short (0.3–0.5s) for smooth, real-time control response.  
- Combine with :ref:`task_compliance_ctrl <task_compliance_ctrl>` for advanced compliant task execution.  
- Always release compliance before high-speed motion or trajectory blending.
