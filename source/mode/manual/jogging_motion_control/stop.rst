.. _manual_stop:

stop (Manual Mode)
------------------------------------------
This section describes how to use :ref:`stop <stop>` during **Manual (Teach)** operation.  
Although defined in **3.1 Common**, it is mainly used in Manual Jogging to:

- Instantly halt a running **jog / multi_jog**
- Apply a **soft stop** for smooth deceleration
- Recover from unexpected contact or operator intervention

**Typical usage**

- Use **`STOP_TYPE_QUICK`** for instant halt (e.g., fixture proximity).  
- Use **`STOP_TYPE_SLOW`** to reduce vibration after fine positioning.  
- After stopping, confirm completion with :ref:`mwait <mwait>` or :ref:`get_robot_state <get_robot_state>`.

.. Note::

    ``stop()`` only halts motion. It does not reset safety faults or clear protective stops.

**Example: Jog → Stop → Verify**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Jog along +X for 0.7s, then quick stop
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 15.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(700));
       drfl.stop(STOP_TYPE_QUICK);
       drfl.mwait();

       // Fine adjustment using TOOL frame, then soft stop
       float v_touch[6] = {3.0f, 0, 0, 0, 0, 0};
       drfl.multi_jog(v_touch, MOVE_REFERENCE_TOOL, 1.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(400));
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();

       return 0;
   }

**Tips**

- Map a pendant key to ``stop(STOP_TYPE_QUICK)`` for instant reaction.  
- Use ``STOP_TYPE_SLOW`` for stable final positioning after jogging.
