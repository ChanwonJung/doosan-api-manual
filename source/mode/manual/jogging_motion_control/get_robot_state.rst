.. _manual_get_robot_state:

get_robot_state (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_robot_state <get_robot_state>` during **Manual (Teach)** operations.  
While defined in **3.1 Common**, this function is essential to monitor the **real-time operational state** of the robot  
before or during teaching.

**Typical usage**

- Confirm if the robot is currently **moving**, **stopped**, **paused**, or in **error** state.  
- Used in conjunction with :ref:`mwait <mwait>` to ensure safe sequencing.  
- Display current robot status on pendant or GUI during manual operation.

.. Note::

  - Common states include: |br|
    - `STATE_STANDBY` : Idle, ready to move. |br|  
    - `STATE_MOVING` : Motion active. |br|
    - `STATE_PAUSED` : Motion paused by operator. |br|  
    - `STATE_EMERGENCY_STOP` : Emergency stop engaged.

**Example: Check Robot State before Next Command**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Start a short jog
       drfl.jog(JOG_AXIS_TASK_Z, MOVE_REFERENCE_BASE, -10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(400));
       drfl.stop(STOP_TYPE_SLOW);

       // Poll robot state until stopped
       ROBOT_STATE state;
       do {
           state = drfl.get_robot_state();
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       } while (state == STATE_MOVING);

       printf("Robot motion stopped. Safe for next command.\n");

       return 0;
   }

**Tips**

- Regularly query ``get_robot_state()`` during manual teaching to monitor motion progress.  
- Use it to implement “wait until stop” logic or automatic UI updates.  
- Combine with :ref:`get_robot_mode <manual_get_robot_mode>` to distinguish Manual vs. Auto operation.
