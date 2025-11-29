.. _manual_set_safety_mode:

set_safety_mode (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_safety_mode <set_safety_mode>` during **Manual (Teach)** operations.  
This function sets the robot’s **safety operating mode** and determines how the robot behaves under specific safety conditions.  
It allows switching between **Normal**, **Reduced**, or **Collaborative** operation modes depending on safety events and system configuration.

**Typical usage**

- Change the robot’s operating safety mode during manual setup or collaborative teaching.  
- Apply **Reduced Speed Mode** or **Collaborative Mode** when working near humans.  
- Configure the robot’s response to safety triggers such as protective stops or external sensors.

.. Note::

    - The configured mode persists until modified or overridden by a new safety event.

**Example: Apply reduced speed mode for manual teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Servo power ON

       // 1) Set the robot to reduced speed mode triggered by manual teach event
       if (drfl.set_safety_mode(SAFETY_MODE_REDUCED, SAFETY_EVENT_RECOVERY))
           std::printf("[Safety Mode] Reduced speed mode activated for teaching.\n");
       else {
           std::printf("[Safety Mode] Failed to apply reduced speed mode.\n");
           return -1;
       }

       // 2) Perform safe manual motion
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 30, 20);
       drfl.mwait();

       // 3) Restore normal safety mode after teaching
       drfl.set_safety_mode(SAFETY_MODE_NORMAL, SAFETY_EVENT_RECOVERY);
       std::printf("[Safety Mode] Restored to normal mode.\n");

       return 0;
   }

**Tips**

- Always verify that the selected safety mode complies with site safety requirements.  
- Use **Reduced Mode** when performing proximity teaching or setup tasks.  
- Switching to **Collaborative Mode** requires compatible hardware and safety configuration.  
- Check the applied safety configuration using :ref:`get_safety_configuration_ex <manual_get_safety_configuration_ex2>`  
  or :ref:`get_safety_configuration_ex2_v3 <manual_get_safety_configuration_ex2_v3>`.  
- Combine with :ref:`change_collision_sensitivity <manual_change_collision_sensitivity>`  
  and :ref:`release_protective_stop <manual_release_protective_stop>` for a complete manual safety management routine.

