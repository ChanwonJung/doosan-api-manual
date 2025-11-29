.. _auto_is_done_bolt_tightening:

is_done_bolt_tightening (Auto Mode)
------------------------------------------
This section explains how to use :ref:`is_done_bolt_tightening <is_done_bolt_tightening>`  
during **Auto (Run)** operations to monitor and validate **torque-based fastening completion**.  
The function checks whether the tool’s **measured torque** along a specific axis reaches  
a user-defined target value (N·m) within the given timeout period.

It is primarily used during **automated assembly**, **bolt fastening**, or **torque verification**  
to confirm when the tightening process has reached the required torque threshold.

**Typical usage**

- Validate whether the robot has completed the desired bolt tightening torque during automated processes.  
- Implement conditional logic (``while`` or ``if``) to detect the completion of torque-based assembly in automation.  
- Combine with :ref:`task_compliance_ctrl <auto_task_compliance_ctrl>` for torque-controlled automated operations.  
- Log or display torque achievement feedback for process validation or automated quality assurance.

.. Note::

  - This function is **non-blocking** and can be called iteratively in auto control loops during automated processes.

**Example: Automated Torque Verification During Bolt Tightening**

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
       // - Auto mode active, servo ON
       // - Torque/force sensor calibrated
       // - Robot positioned near the tightening location

       // 1) Move to initial bolt position
       float fPos1[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       drfl.movej(fPos1, 30.0);
       drfl.mwait();

       // 2) Enable compliance control for torque-based operation
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
This allows real-time validation of torque completion during automated tightening processes.

**Tips**

- Always activate :ref:`task_compliance_ctrl <auto_task_compliance_ctrl>` before using this function for automated tightening.  
- Set ``fTargetTor`` based on the required torque for the specific tightening task.  
- Adjust ``fTimeout`` to accommodate the expected duration of the automated tightening process.  
- Use ``FORCE_AXIS_Z`` for typical bolt-tightening applications (rotational torque) in auto mode.  
- Combine with :ref:`check_force_condition <auto_check_force_condition>` to ensure  
  both torque and force thresholds are satisfied before proceeding with the next task in the automated cycle.  
- For automated cycles, consider calling this function periodically (every 100–200 ms)  
  to detect torque achievement in real time during the tightening phase of automated operations.
