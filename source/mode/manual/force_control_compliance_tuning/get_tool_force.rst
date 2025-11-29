.. _manual_get_tool_force:

get_tool_force (Manual Mode)
------------------------------------------

This section explains how to use :ref:`get_tool_force <get_tool_force>` during **Manual (Teach)** operations  
to **monitor the real-time 6-axis force and torque values** measured at the robot’s **tool (flange) sensor**.  
It is mainly used for **contact detection**, **force tuning**, and **compliance control validation** during teaching.

**Typical usage**

- Observe live **Fx, Fy, Fz (force)** and **Tx, Ty, Tz (torque)** data while adjusting compliance parameters.  
- Verify tool calibration and load compensation results.  
- Detect contact or pressing force while manually testing assembly or polishing operations.

.. Note::

  - Use this function **only for reading**; it does not affect robot motion.  
  - The function is available in **all modes**, but most commonly used in **Manual (Teach)** for compliance validation.

**Example: Read and display tool force during manual compliance test**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Force/Torque sensor at the tool flange is enabled

       // 1) Continuously monitor tool force in TOOL frame
       for (int i = 0; i < 10; ++i) {
           LPROBOT_FORCE pForce = drfl.get_tool_force(COORDINATE_SYSTEM_TOOL);
           if (pForce) {
               std::printf("[Tool Force] Fx=%.2f Fy=%.2f Fz=%.2f  |  Tx=%.2f Ty=%.2f Tz=%.2f\n",
                   pForce->_fFx, pForce->_fFy, pForce->_fFz,
                   pForce->_fTx, pForce->_fTy, pForce->_fTz);
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       return 0;
   }

In this example, the host PC continuously retrieves **real-time force and torque readings**  
from the robot’s flange-mounted sensor while in teaching mode.  
The printed data can be used to verify applied forces, detect surface contact,  
or tune compliance parameters interactively for safe manual operation.

**Tips**

- Always call this function **after compliance or force control activation** (e.g., :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>`).  
- If readings seem unstable, check sensor calibration and grounding.  
- Use ``COORDINATE_SYSTEM_TOOL`` for end-effector-based tasks (e.g., polishing, insertion).  
- Combine with :ref:`check_force_condition <manual_check_force_condition>` for real-time safety or task completion checks.
