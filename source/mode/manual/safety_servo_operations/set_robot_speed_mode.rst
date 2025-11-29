.. _manual_set_robot_speed_mode:

set_robot_speed_mode (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_robot_speed_mode <set_robot_speed_mode>` during **Manual (Teach)** operations.  
This function sets the robot’s **speed mode** — either **Normal** or **Reduced** — to control the maximum allowable velocity.  
It is mainly used during teaching to ensure safe motion speeds while the operator is near the robot.

**Typical usage**

- Switch to **Reduced Speed Mode** (safety speed limit) during manual teaching or hand-guided operation.  
- Set **Normal Speed Mode** after teaching is complete for faster verification or playback.  
- Apply reduced speed dynamically when entering safety zones or performing fine position adjustments.  
- Combine with :ref:`get_robot_speed_mode <manual_get_robot_speed_mode>` to confirm the active speed state.

.. Note::

    - In Manual mode, **Reduced Speed** is automatically enforced when safety sensors are active.  
    - Speed mode transitions may be restricted by system-level safety configuration.

**Example: Switch between Reduced and Normal speed during teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <chrono>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       cout << "[Speed] Setting Reduced Speed Mode for safe teaching...\n";
       if (drfl.set_robot_speed_mode(SPEED_MODE_REDUCED))
           cout << "[Speed] Reduced speed mode activated.\n";
       else
           cout << "[Speed] Failed to set reduced speed mode.\n";

       // Simulate slow manual motion
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 20, 20);
       this_thread::sleep_for(chrono::seconds(2));

       cout << "[Speed] Switching to Normal Speed Mode for playback test...\n";
       drfl.set_robot_speed_mode(SPEED_MODE_NORMAL);

       return 0;
   }

**Tips**

- Always use **Reduced Speed Mode** when an operator is within the robot’s collaborative workspace.  
- Combine with :ref:`get_robot_system <manual_get_robot_system>` to ensure the robot is in **real hardware mode** before switching speed.  
- For automatic speed recovery logic, log transitions between modes to prevent unsafe accelerations.  
- Verify that external safety devices (light curtains, scanners) properly enforce reduced speed mode changes.
