.. _auto_drl_start:

drl_start (Auto Mode)
------------------------------------------
This section explains how to use :ref:`drl_start <drl_start>`  
during **Auto (Run)** operations to start a **DRL (Doosan Robotics Language)** program  
from an external application (e.g., PC, PLC gateway).

The function is typically used to trigger **pre-defined task logic** or  
**inline DRL scripts** that describe motion, I/O handling, and simple control flow  
while the robot is already in **Auto Mode**.

**Typical usage**

- Start a DRL task when a production cycle begins (e.g., from a PC HMI).  
- Execute an inline DRL script for simple repetitive motions or testing.  
- Trigger different DRL routines depending on product type or workcell state.  
- Integrate with external systems (MES/PLC) to control task start without using the teach pendant.  

.. Note::

    - The robot must be in **Auto (Run)** mode and ready state  
      (e.g., ``eSTATE_STANDBY`` or equivalent) before calling ``drl_start``.  
    - The DRL string must follow the same syntax as programs created on the controller.  

**Example: Starting a Simple DRL Loop in Auto Mode**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Connect & initialize (omitted here – handled in common setup code)
       //    e.g., drfl.open_connection("192192.168.137.100");
       //          drfl.set_robot_system(ROBOT_SYSTEM_REAL);

       // 2) Define a simple DRL program as a string
       //    - Repeats a back-and-forth joint motion three times.
       std::string drlProgram =
           "loop = 0\\r\\n"
           "while loop < 3:\\r\\n"
           "    movej(posj(10,10,10,10,10,10), vel=60, acc=60)\\r\\n"
           "    movej(posj(0,0,0,0,0,0), vel=60, acc=60)\\r\\n"
           "    loop = loop + 1\\r\\n"
           "end\\r\\n";

       // 3) Ensure robot is in Auto Mode and ready
       if (drfl.get_robot_mode() == ROBOT_MODE_AUTONOMOUS &&
           drfl.get_robot_state() == eSTATE_STANDBY) {

           // Choose target robot system:
           // - ROBOT_SYSTEM_REAL    : real robot (field)
           // - ROBOT_SYSTEM_VIRTUAL : virtual system (simulation/test)
           ROBOT_SYSTEM targetSystem = ROBOT_SYSTEM_REAL;

           if (!drfl.drl_start(targetSystem, drlProgram)) {
               std::cerr << "Failed to start DRL program." << std::endl;
               return -1;
           }

           std::cout << "DRL program started in Auto Mode." << std::endl;
       } else {
           std::cerr << "Robot is not in Auto/Standby state. Cannot start DRL." << std::endl;
       }

       return 0;
   }

In this example, once the robot is switched to **Auto Mode** and reaches  
the **Standby** state, the external application starts a simple DRL loop  
on the target robot system using ``drl_start``.

**Tips**

- Combine with :ref:`drl_stop <auto_drl_stop>` and :ref:`drl_pause <auto_drl_pause>`  
  to implement start/stop buttons in your external UI.  
- Use ``ROBOT_SYSTEM_VIRTUAL`` during development to verify DRL logic  
  without moving a real robot.  
- Keep DRL strings small and focused; for large logic, consider storing DRL files  
  on the controller and using higher-level program management APIs if available.  
- Log the DRL script or its version ID when starting tasks to simplify debugging  
  in production environments.
