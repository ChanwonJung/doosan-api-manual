.. _manual_is_done_bolt_tightening:

is_done_bolt_tightening (Manual Mode)
------------------------------------------
This section explains how to use :ref:`is_done_bolt_tightening <is_done_bolt_tightening>`  
during **Manual (Teach)** operations to monitor and validate **torque-based fastening completion**.  
The function checks whether the tool’s **measured torque** along a specific axis reaches  
a user-defined target value (N·m) within the given timeout period.

It is primarily used during **assembly teaching**, **bolt fastening**, or **torque verification**  
to confirm when the tightening process has reached the required torque threshold.

**Typical usage**

- Validate that a bolt or nut has reached the desired tightening torque during manual operation.  
- Implement conditional logic (``while`` or ``if``) to detect completion of torque-based assembly.  
- Combine with :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>` for torque-controlled teaching.  
- Record or display torque achievement feedback for process validation or manual calibration.

.. Note::

  - This function is **non-blocking** and can be called iteratively in manual teaching loops.

**Example: Manual Torque Verification During Bolt Tightening**

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
       // - Servo ON and Manual (Teach) mode active
       // - Torque/force sensor properly calibrated
       // - Robot positioned near tightening location

       // 1) Move to initial bolt position
       float fPos1[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       drfl.movej(fPos1, 30.0);
       drfl.mwait();

       // 2) Enable compliance control for torque-based teaching
       drfl.task_compliance_ctrl();

       // 3) Monitor tightening torque (target = 10 N·m, timeout = 5 sec)
       bool bTightened = drfl.is_done_bolt_tightening(FORCE_AXIS_Z, 10.0f, 5.0f);

       // 4) Display result
       if (bTightened)
           std::printf("Tightening complete: torque reached 10 N·m or higher.\n");
       else
           std::printf("Timeout: target torque not reached within 5 seconds.\n");

       // 5) Release compliance control after verification
       drfl.release_compliance_ctrl();

       return 0;
   }

In this example, the robot checks whether the applied torque on the **Z-axis**  
reaches **10 N·m** within **5 seconds** while operating under compliance control.  
This allows real-time validation of torque completion during manual teaching or assembly calibration.

**Tips**

- Always activate :ref:`task_compliance_ctrl <manual_task_compliance_ctrl>` before using this function.  
- Set ``fTargetTor`` based on the torque requirement of the tightening process.  
- Adjust ``fTimeout`` to accommodate the expected tightening duration.  
- Use ``FORCE_AXIS_Z`` for typical bolt-tightening applications (rotational torque).  
- Combine with :ref:`check_force_condition <manual_check_force_condition>` to ensure  
  both torque and force thresholds are satisfied before proceeding.  
- For automated tightening cycles, consider calling this function periodically (every 100–200 ms)  
  to detect torque achievement in real time during manual teaching.
