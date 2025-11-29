.. _manual_set_robot_mode:

set_robot_mode (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_robot_mode <set_robot_mode>` during **Manual (Teach)** operations.  
This function switches the robot controller between **Manual (Teach)** and **Automatic (Run)** modes.  

It is essential for managing when operators can safely jog, teach, or execute DRL programs.

**Typical usage**

- Switch to **Manual Mode** before performing teaching, jogging, or calibration.  
- Change to **Automatic Mode** when executing a saved DRL program or remote control sequence.  
- Verify mode transition logic between external systems (e.g., PLC ↔ controller) for safety compliance.  
- Use in initialization routines to ensure the robot is in the correct mode before commanding motion.

.. Note::

    - Certain operations (e.g., motion, speed change) are restricted based on the active mode.  
    - Some controllers may require physical switch confirmation for safety (e.g., TP key or panel input).

**Example: Switch robot to Manual mode before jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;
   using namespace std;

   int main()
   {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Safety interlocks and servo power ready

       cout << "[Mode] Requesting switch to MANUAL mode...\n";
       if (drfl.set_robot_mode(ROBOT_MODE_MANUAL))
           cout << "[Mode] Successfully switched to MANUAL mode.\n";
       else
           cout << "[Mode] Failed to switch mode. Check TP or safety key.\n";

       // Simulate manual jogging operation
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 30, 30);
       this_thread::sleep_for(chrono::seconds(2));

       cout << "[Mode] Switching to AUTO mode for program execution...\n";
       drfl.set_robot_mode(ROBOT_MODE_AUTO);

       return 0;
   }

**Tips**

- Always confirm **Manual Mode** is active before enabling jog or teach functions.  
- Use :ref:`get_robot_mode <manual_get_robot_mode>` to verify the current mode after switching.  
- Combine with :ref:`set_robot_system <manual_set_robot_system>` to coordinate mode and system-level changes.  
- In hybrid systems, mode transitions should be logged to ensure traceability and operator safety.
