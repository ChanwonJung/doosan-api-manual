.. _manual_set_robot_system:

set_robot_system (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_robot_system <set_robot_system>` during **Manual (Teach)** operations.  
This function configures the **operating system type** of the controller — whether to control a **real robot**,  
a **virtual simulation**, or an **emulator environment**.  
It is typically used when switching between simulation and real hardware during teaching, testing, or debugging.

**Typical usage**

- Switch from **virtual (simulation)** to **real robot** control before live motion testing.  
- Configure the controller to **emulator mode** for offline DRL program validation.  
- Automatically change system type when deploying a teaching procedure from PC to actual hardware.  
- Verify system consistency before issuing move or I/O commands.

.. Note::

    - Some system changes may require a controller reboot or reinitialization to take effect.  
    - It is recommended to ensure **servo power is OFF** before switching between real and virtual modes.

**Example: Switch to real robot system before starting teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - No motion currently in progress

       cout << "[System] Setting robot system to REAL hardware...\n";
       if (drfl.set_robot_system(ROBOT_SYSTEM_REAL))
           cout << "[System] Robot system set to REAL.\n";
       else
           cout << "[System] Failed to change robot system.\n";

       // Verify configuration
       ROBOT_SYSTEM sysType = drfl.get_robot_system();
       cout << "[System] Current system type: " << sysType << endl;

       // Continue with manual teaching sequence
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 30, 30);

       return 0;
   }

**Tips**

- Always verify **system mode** before starting motion to avoid commanding a virtual robot unintentionally.  
- Use :ref:`get_robot_system <manual_get_robot_system>` to confirm the current system state after change.  
- When switching between environments, ensure all safety configurations match the target hardware.  
- For DRL program debugging, emulator mode is ideal for safe verification before real execution.
