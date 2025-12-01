.. _manual_check_position_condition:

check_position_condition (Manual Mode)
------------------------------------------
This section explains how to use :ref:`check_position_condition <check_position_condition>`  
during **Manual (Teach)** operations to evaluate whether the **position of a specified axis**  
meets a defined range condition relative to a target position.

This function allows users to implement **conditional position checks** within teaching routines  
to verify **alignment**, **approach distance**, or **safety constraints** before executing the next motion.

**Typical usage**

- Verify whether the robot’s TCP has reached a specific position range before triggering the next step.  
- Monitor relative or absolute **position offsets** for **approach validation** or **contact detection**.  
- Use within ``while`` or ``if`` statements to create **looped condition checks** during teaching.  
- Switch between **absolute (global)** and **relative (offset)** comparisons using ``eMode``: |br| 
  - ``MOVE_MODE_ABSOLUTE``: compare absolute position within workspace. |br| 
  - ``MOVE_MODE_RELATIVE``: compare deviation from target pose. |br|

.. Note::

  - This function performs **read-only monitoring** and does not initiate motion.

**Example: Position Range Check in Manual Teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Robot connected and servo ON
       // - Manual (Teach) mode active
       // - Robot is near target pose

       // 1) Define a target pose (reference for comparison)
       float targetPose[6] = {400.f, 500.f, 600.f, 0.f, 180.f, 0.f};

       // 2) Check relative Z-axis offset (±5 mm tolerance)
       bool relCond = drfl.check_position_condition(FORCE_AXIS_Z, -5.f, 5.f, targetPose, MOVE_MODE_RELATIVE);

       // 3) Check absolute X-axis position (workspace limit)
       bool absCond = drfl.check_position_condition(FORCE_AXIS_X, 100.f, 200.f, targetPose, MOVE_MODE_ABSOLUTE, COORDINATE_SYSTEM_BASE);

       if (relCond)
           printf("Relative condition met: TCP Z within ±5 mm of target.\n");
       else
           printf("Relative condition not met.\n");

       if (absCond)
           printf("Absolute condition met: X-axis between 100–200 mm.\n");
       else
           printf("Absolute condition not met.\n");

       // 4) Example: loop until relative condition is satisfied
       while (!relCond) {
           relCond = drfl.check_position_condition(FORCE_AXIS_Z, -5.f, 5.f, targetPose, MOVE_MODE_RELATIVE);
           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       printf("Target range reached — ready for next task.\n");
       return 0;
   }

In this example, the function is used to check whether the robot’s **TCP position**  
satisfies both relative and absolute positional constraints before proceeding.  
It can be used to monitor **teaching accuracy**, **approach distance**, or **safety compliance**  
during manual motion control or calibration.

**Tips**

- Use ``MOVE_MODE_ABSOLUTE`` for verifying **workspace boundaries**, **teaching points**, or **safe zones**.  
- Use ``MOVE_MODE_RELATIVE`` for **approach or alignment tasks** where deviation from a reference is critical.  
- Combine with :ref:`check_force_condition <manual_check_force_condition>`  
  to create **force-position hybrid logic** during contact or assembly teaching.  
- For smoother monitoring, call this function periodically (every 50–200 ms).  
- Always ensure consistency between ``fTargetPos`` coordinates and the chosen reference frame (BASE or TOOL).
