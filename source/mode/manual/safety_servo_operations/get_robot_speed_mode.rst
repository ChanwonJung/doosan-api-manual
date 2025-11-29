.. _manual_get_robot_speed_mode:

get_robot_speed_mode (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_robot_speed_mode <get_robot_speed_mode>` during **Manual (Teach)** operations.  
This function retrieves the robot’s **current speed mode**, which determines whether the controller is operating  
in **normal** or **reduced-speed (safety)** mode.  
It is primarily used during manual teaching to verify that the robot is running at a safe speed before motion execution.

**Typical usage**

- Check whether the robot is currently in **Reduced Speed Mode** before starting teaching motion.  
- Verify that speed mode automatically switches when entering **safety zones** or restricted environments.  
- Display or log the speed mode for operator awareness during manual control.  
- Combine with :ref:`set_robot_speed_mode <set_robot_speed_mode>` to enforce safe operation limits.

.. Note::

    - The result is read-only and changes automatically depending on system and safety conditions.  
    - Always verify speed mode before executing motion in shared human–robot environments.

**Example: Check current speed mode before manual movement**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       SPEED_MODE spdMode = drfl.get_robot_speed_mode();

       if (spdMode == SPEED_MODE_REDUCED) {
           cout << "[Speed Mode] Reduced speed active. Safe for manual teaching.\n";
       } 
       else if (spdMode == SPEED_MODE_NORMAL) {
           cout << "[Speed Mode] Normal operation speed.\n";
           cout << "Warning: Verify safety before continuing.\n";
       } 
       else {
           cout << "[Speed Mode] Unknown speed mode detected.\n";
       }

       return 0;
   }

**Tips**

- Always ensure **Reduced Speed Mode** is active when teaching in close proximity to the robot.  
- Use :ref:`set_robot_speed_mode <set_robot_speed_mode>` in automatic procedures to switch safely between modes.  
- Log mode transitions to validate safety compliance during manual sessions.  
- Combine with :ref:`get_robot_system <manual_get_robot_system>` to verify environment context (real or virtual).
