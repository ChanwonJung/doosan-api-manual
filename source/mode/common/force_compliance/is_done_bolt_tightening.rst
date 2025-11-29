.. _is_done_bolt_tightening:

is_done_bolt_tightening
------------------------------------------
This function monitors the **tightening torque** on a specified axis and returns **True** if the defined target torque  
is reached within the given timeout duration.  
If the torque target is not achieved within the timeout, the function returns **False**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 962)

.. code-block:: cpp

    bool is_done_bolt_tightening(FORCE_AXIS eForceAxis, float fTargetTor = 0.f, float fTimeout = 0.f)
    {
        return _is_done_bolt_tightening(_rbtCtrl, eForceAxis, fTargetTor, fTimeout);
    };

**Parameter**

.. list-table::
   :widths: 25 20 15 40
   :header-rows: 1

   * - **Name**
     - **Data Type**
     - **Default**
     - **Description**
   * - ``eForceAxis``
     - :ref:`FORCE_AXIS <enum_FORCE_AXIS>`
     - -
     - Axis used for torque monitoring (e.g., ``FORCE_AXIS_X/Y/Z``). 
   * - ``fTargetTor``
     - ``float``
     - 0.0
     - Target torque value [N·m] for determining tightening completion.
   * - ``fTimeout``
     - ``float``
     - 0.0
     - Timeout duration [sec]. If 0, uses system default.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - ``true (1)``
     - Tightening complete — target torque achieved within timeout.
   * - ``false (0)``
     - Timeout expired before reaching target torque.

**Example A — Manual Mode (Torque Validation During Teaching)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connected, servo ON, manual (teach) mode
       // - Tool torque sensor enabled and calibrated

       // 1) Move to starting position
       float q0[6] = {0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f};
       drfl.movej(q0, 40.0);
       drfl.mwait();

       // 2) Enable compliance for torque-based operation
       float stiff[6] = {3000.f, 3000.f, 2000.f, 200.f, 200.f, 200.f};
       drfl.task_compliance_ctrl(stiff, COORDINATE_SYSTEM_TOOL);

       // 3) Monitor tightening torque (e.g., Z-axis, 10 N·m, 5 seconds)
       bool result = drfl.is_done_bolt_tightening(FORCE_AXIS_Z, 10.0f, 5.0f);

       if (result)
           printf("Tightening complete — target torque achieved.\n");
       else
           printf("Timeout — target torque not reached.\n");

       drfl.release_compliance_ctrl();
       return 0;
   }

**Example B — Auto Mode (Torque-Controlled Assembly Process)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Tool equipped with torque feedback

   // 1) Move to bolt location
   float p_target[NUM_TASK] = {550.f, 150.f, 120.f, 180.f, 0.f, 0.f};
   drfl.movel(p_target, (float[2]){80.f, 25.f}, (float[2]){300.f, 120.f});
   drfl.mwait();

   // 2) Enable compliance for torque application
   float stiff[NUM_TASK] = {2500.f, 2500.f, 1500.f, 150.f, 150.f, 150.f};
   drfl.task_compliance_ctrl(stiff, COORDINATE_SYSTEM_TOOL, 0.1f);

   // 3) Apply small force to maintain contact
   float fTarget[NUM_TASK] = {0.f, 0.f, 15.f, 0.f, 0.f, 0.f};
   unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
   drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);

   // 4) Monitor torque buildup (completion at 8 N·m, within 4 seconds)
   bool bTightened = drfl.is_done_bolt_tightening(FORCE_AXIS_Z, 8.0f, 4.0f);

   if (bTightened)
       printf("Bolt tightening successful — target torque reached.\n");
   else
       printf("Bolt tightening timeout — check tool or torque setting.\n");

   // 5) Release control
   drfl.release_force(0.3f);
   drfl.release_compliance_ctrl();

**Notes & Best Practices**

- Always ensure **force/compliance control** is active before torque monitoring.  
- Verify that the **tool’s torque sensor** is calibrated and operational.  
- In Auto mode, set appropriate timeout to prevent long blocking behavior in process cycles.  
- Combine with :ref:`check_force_condition <check_force_condition>` or :ref:`release_force <release_force>`  
  for safer and more adaptive torque-based automation workflows.  
- For multi-axis assembly or press-fitting, monitor torque in Z while limiting motion along X/Y axes.
