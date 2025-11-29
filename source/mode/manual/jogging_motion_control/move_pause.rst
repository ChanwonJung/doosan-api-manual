.. _manual_move_pause:

move_pause (Manual Mode)
------------------------------------------
This section describes how to use :ref:`move_pause <move_pause>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, it is often used in teaching to temporarily pause robot motion  
for inspection, safety confirmation, or intermediate alignment.

**Typical usage**

- Suspend an ongoing motion or teaching sequence without fully stopping the task.  
- Use together with :ref:`move_resume <move_resume>` to continue from the same position.  
- Recommended before manually adjusting a tool or checking workspace clearance.

.. Note::

    Unlike :ref:`stop <stop>`, this function **does not cancel** the motion;  
    it simply freezes it. The motion can be resumed immediately once it is safe.

**Example: Pause and Resume during Manual Teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Start a slow linear motion toward a target
       float target[6] = {600.0f, 100.0f, 450.0f, 180.0f, 0.0f, 90.0f};
       drfl.movel(target, 50, 50);

       // Pause midway for operator inspection
       std::this_thread::sleep_for(std::chrono::milliseconds(800));
       drfl.move_pause();
       printf("Motion paused. Checking workspace...\n");

       // After confirmation, resume the paused motion
       std::this_thread::sleep_for(std::chrono::milliseconds(1500));
       drfl.move_resume();
       drfl.mwait();  // wait until completion

       return 0;
   }

**Tips**

- Use ``move_pause()`` when you need to inspect or adjust something mid-teaching without losing motion data.  
- Always ensure **the robot is stationary** before entering the workspace for safety.  
- If you need to abort the motion completely, use :ref:`stop <stop>` instead.
