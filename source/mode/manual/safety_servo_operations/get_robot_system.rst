.. _manual_get_robot_system:

get_robot_system (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_robot_system <get_robot_system>` during **Manual (Teach)** operations.  
This function retrieves the **current robot system type** — whether the controller is connected to a **real robot**,  
a **virtual robot (simulation)**, or running in an **emulator** environment.  
It is particularly useful when developing or verifying teaching programs to ensure the correct operating context before motion execution.

**Typical usage**

- Check whether the connected system is a **real robot** or a **virtual (simulated)** controller.  
- Prevent physical motion commands from being sent in simulation-only sessions.  
- Dynamically adjust safety parameters or teaching procedures depending on the system type.  
- Use for conditional logic in hybrid testing environments (real + virtual setup).

.. Note::

    - The result is read-only and updated automatically upon connection.  
    - Use before motion or calibration commands to prevent unintended behavior on a live robot.

**Example: Verify system type before starting manual teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)

       ROBOT_SYSTEM sysType = drfl.get_robot_system();

       switch (sysType) {
           case ROBOT_SYSTEM_REAL:
               cout << "[System] Connected to a REAL robot.\n";
               cout << "Proceeding with manual teaching operations.\n";
               break;

           case ROBOT_SYSTEM_VIRTUAL:
               cout << "[System] Running on VIRTUAL controller.\n";
               cout << "Motion commands will be simulated.\n";
               break;

           case ROBOT_SYSTEM_EMULATOR:
               cout << "[System] Connected to EMULATOR environment.\n";
               cout << "Force/IO feedback may be limited.\n";
               break;

           default:
               cout << "[System] Unknown system type detected.\n";
               break;
       }

       return 0;
   }

**Tips**

- Always confirm the **system type** before executing any move commands during teaching.  
- When testing on a PC without a physical robot, expect ``ROBOT_SYSTEM_VIRTUAL`` or ``ROBOT_SYSTEM_EMULATOR``.  
- Combine with :ref:`get_robot_speed_mode <manual_get_robot_speed_mode>` to ensure safe speed limits in real environments.  
- Ideal for hybrid environments where development and verification alternate between virtual and real robots.
