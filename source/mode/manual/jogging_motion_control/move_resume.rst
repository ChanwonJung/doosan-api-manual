.. _manual_move_resume:

move_resume (Manual Mode)
------------------------------------------
This section describes how to use :ref:`move_resume <move_resume>` during **Manual (Teach)** operations.  
While the function is defined in **3.1 Common**, it is mainly used to **continue** a paused motion  
after :ref:`move_pause <move_pause>` has been called.

**Typical usage**

- Resume a temporarily paused motion at the same velocity and trajectory.  
- Commonly used after workspace inspection, tool alignment, or safety verification.  
- Works in combination with :ref:`mwait <mwait>` to ensure complete motion recovery.

.. Note::

  - The robot must have been paused using :ref:`move_pause <move_pause>` before calling this function.  
  - If the motion was stopped with :ref:`stop <stop>`, it cannot be resumed —  
    a new motion command must be issued instead.

**Example: Pause, Inspect, and Resume**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Start motion toward a workpiece
       float pos[6] = {500.0f, 150.0f, 400.0f, 180.0f, 0.0f, 90.0f};
       drfl.movel(pos, 50, 50);

       // Pause for visual inspection
       std::this_thread::sleep_for(std::chrono::milliseconds(800));
       drfl.move_pause();
       printf("Motion paused for inspection.\n");

       // Resume after confirmation
       std::this_thread::sleep_for(std::chrono::milliseconds(1200));
       drfl.move_resume();

       // Wait until motion completes
       drfl.mwait();

       return 0;
   }

**Tips**

- Use ``move_resume()`` immediately after inspection or alignment to continue the exact paused trajectory.  
- If the pause duration is long, recheck the robot state using :ref:`get_robot_state <get_robot_state>`  
  before resuming to ensure communication and servo status are stable.  
- For emergency interruptions, use :ref:`stop <stop>` instead of pause/resume.
