.. _manual_change_collision_sensitivity:

change_collision_sensitivity (Manual Mode)
--------------------------------------------
This section explains how to use :ref:`change_collision_sensitivity <change_collision_sensitivity>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, it is frequently used during teaching to **temporarily adjust the robot’s collision detection sensitivity**  
for safer or more flexible manual manipulation.

**Typical usage**

- Reduce collision sensitivity when performing **tight-space teaching or contact-based tool alignment**.  
- Increase sensitivity to quickly detect unexpected impacts or resistance.  
- Restore default sensitivity after manual teaching to maintain standard safety thresholds.

.. Note::

    - Adjustment takes effect immediately and applies globally to all joints.  
    - Always reset sensitivity to the default after completing manual operations.

**Example: Temporarily reduce collision sensitivity during teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Servo power ON and motion enabled

       // 1) Lower collision sensitivity to allow contact alignment
       if (drfl.change_collision_sensitivity(5.0f))
           std::printf("[Collision Sensitivity] Temporarily set to 5.0\n");
       else
           std::printf("[Collision Sensitivity] Failed to adjust\n");

       // 2) Perform short manual motion
       drfl.jog(JOG_AXIS_JOINT_2, MOVE_REFERENCE_JOINT, 10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(800));
       drfl.stop(STOP_TYPE_SLOW);

       // 3) Restore default sensitivity
       drfl.change_collision_sensitivity(10.0f);
       std::printf("[Collision Sensitivity] Restored to default (10.0)\n");

       return 0;
   }

**Tips**

- Recommended to lower sensitivity **only temporarily** for contact-based tasks.  
- After teaching, restore to default (10.0) to comply with safety standards.  
- Combine with :ref:`servo_off <manual_servo_off>` and :ref:`set_safety_mode <manual_set_safety_mode>` for a complete safety routine.  
- For repetitive tasks, consider logging the current setting before modification and restoring afterward.
