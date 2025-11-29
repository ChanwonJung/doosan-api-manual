.. _manual_check_force_condition:

check_force_condition (Manual Mode)
------------------------------------------
This section explains how to use :ref:`check_force_condition <check_force_condition>` during **Manual (Teach)** operations  
to monitor whether the **measured external force or torque** on a specific axis is within a defined threshold range.  
It is mainly used for **contact detection**, **assembly validation**, and **force-based event triggering** during manual teaching.

To view the full API definition and parameters, refer to |br|
:ref:`check_force_condition <check_force_condition>` in the **Common API section**.

**Typical usage**

- Detect whether the **contact force** exceeds a safety or process threshold (e.g., during pressing or surface contact).  
- Monitor **external force feedback** during hand-guiding or compliance control to validate sensor readings.  
- Use within loops or conditional statements to trigger actions when a target force is reached.  
- Combine with :ref:`check_position_condition_abs <manual_check_position_condition_abs>`  
  or :ref:`check_position_condition_rel <manual_check_position_condition_rel>` for hybrid force–position logic.

.. Note::

  - The check compares the **absolute value** of the measured force/torque (ignores direction).  
  - The function does **not affect robot motion**, but is used for real-time monitoring or logic control.  
  - Typically used alongside :ref:`get_tool_force <manual_get_tool_force>` for visualization or debugging.

**Example: Monitor contact force during teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions:
       // - Connection established
       // - Manual (Teach) mode active
       // - Force/Torque sensor enabled

       printf("Monitoring Z-axis force between 5 N and 10 N...\n");

       // 1) Continuously check force condition while manually guiding the robot
       while (true) {
           bool withinRange = drfl.check_force_condition(FORCE_AXIS_Z, 5.f, 10.f, COORDINATE_SYSTEM_TOOL);

           if (withinRange) {
               printf("Force condition met: |Fz| between 5–10 N.\n");
               break;
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }

       // 2) Verify current force reading
       LPROBOT_FORCE pForce = drfl.get_tool_force(COORDINATE_SYSTEM_TOOL);
       if (pForce) {
           printf("[Force Snapshot] Fx=%.2f Fy=%.2f Fz=%.2f  |  Tx=%.2f Ty=%.2f Tz=%.2f\n",
               pForce->_fFx, pForce->_fFy, pForce->_fFz,
               pForce->_fTx, pForce->_fTy, pForce->_fTz);
       }

       printf("Teaching sequence can proceed safely.\n");
       return 0;
   }

In this example, the robot continuously checks the **Z-axis force magnitude**  
to determine whether it is between **5 N and 10 N**.  
When the condition is met, the loop exits, allowing the operator to safely continue  
with a force-controlled teaching or calibration task.

**Tips**

- Use ``check_force_condition()`` to detect **contact**, **alignment pressure**, or **assembly thresholds** in real time.  
- Combine with :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>`  
  and :ref:`set_desired_force <manual_set_desired_force>` for advanced force-guided teaching.  
- The function only checks **magnitude**, not direction — if you need directional sensitivity, use separate logic with sign checks.  
- Apply filtering or smoothing on force feedback if sensor noise causes false positives.  
- For visualization, log real-time readings using :ref:`get_tool_force <manual_get_tool_force>`.  
- Recommended check cycle: **10–50 ms** for stable monitoring without latency.
