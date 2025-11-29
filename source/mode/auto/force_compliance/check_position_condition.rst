.. _auto_check_position_condition:

check_position_condition (Auto Mode)
------------------------------------------
This function checks whether the **position of a specified axis** meets a defined range condition  
relative to a target position. It is commonly used in **Auto (Run)** mode for automated motion, process control, and safety validation.  
This function allows for continuous evaluation of position during execution, such as verifying **alignment**, **approach distance**, or **workspace boundaries** in real-time.

The function can be used to verify if the robot's TCP is within a defined position range before proceeding with the next motion or task.

**Typical usage**

- Monitor real-time position conditions to ensure the robot’s TCP is within a **safe range** or **target zone** during automated operations.  
- Check whether the robot’s position satisfies **relative or absolute positional constraints** during a task.  
- Use in **looped condition checks** inside motion control systems to pause or trigger actions based on position.  
- Switch between **absolute** (global) and **relative** (offset) comparisons using ``eMode`` |br| 
  - ``MOVE_MODE_ABSOLUTE``: compares the current position against the global workspace limits. |br| 
  - ``MOVE_MODE_RELATIVE``: compares deviation from a target pose. |br|

.. Note::

  - If ``eForceReference`` is ``COORDINATE_SYSTEM_TOOL``, define ``fTargetPos`` in **BASE** coordinates.  
  - This function performs **read-only monitoring** and does not initiate motion.

**Example: Position Range Check in Automated Motion**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Robot connected, servo ON
       // - Auto (Run) mode active
       // - Robot is executing an automated task

       // 1) Define target position (reference for comparison)
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
satisfies both relative and absolute positional constraints during automated motion.  
It can be used to monitor **safety compliance**, **approach distance**, or **task completion** during an automated process.

**Tips**

- Use ``MOVE_MODE_ABSOLUTE`` for **workspace boundary checks**, **target zone verification**, or **safe zone monitoring**.  
- Use ``MOVE_MODE_RELATIVE`` for **fine alignment tasks** where position deviation from a reference is critical (e.g., insertion, alignment).  
- Combine with :ref:`check_force_condition <auto_check_force_condition>`  
  for **force-position hybrid monitoring** during automated tasks.  
- For continuous monitoring, call this function periodically (every 50–200 ms).  
- Ensure consistency between ``fTargetPos`` coordinates and the chosen reference frame (BASE or TOOL).

