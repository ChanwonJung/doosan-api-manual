.. _manual_manage_access_control:

manage_access_control (Manual Mode)
------------------------------------------
This section explains how to use :ref:`manage_access_control <manage_access_control>` during **Manual (Teach)** operations.  
This function is used to **request or release control authority** of the robot system,  
ensuring that only one client (PC, HMI, or external device) can actively command the robot at a time. |br|
In Manual mode, it is commonly used to obtain permission before jogging or executing any motion command.

**Typical usage**

- Request access control before performing **manual motion or configuration** operations.  
- Release access control after teaching is completed to allow other clients (e.g., Auto program) to take control.  
- Check or renew access if multiple clients are connected to the same robot controller.

.. Note::

    - Only **one controller session** can hold access at a time.  
    - Required before executing most motion or configuration commands in **Manual (Teach)** mode.

**Example: Request and release robot access control**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 1) Request access control to operate robot manually
       if (drfl.manage_access_control(MANAGE_ACCESS_CONTROL_REQUEST))
           std::printf("[Access Control] Control successfully requested.\n");
       else {
           std::printf("[Access Control] Request failed. Another client may have control.\n");
           return -1;
       }

       // 2) Perform simple manual move or teaching operation
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 50, 50);

       // Wait until motion is complete
       while (drfl.check_motion() != 0)
           std::this_thread::sleep_for(std::chrono::milliseconds(100));

       // 3) Release access after finishing teaching
       if (drfl.manage_access_control(MANAGE_ACCESS_CONTROL_RELEASE))
           std::printf("[Access Control] Released successfully.\n");
       else
           std::printf("[Access Control] Release failed.\n");

       return 0;
   }

**Tips**

- Always call ``manage_access_control(MANAGE_ACCESS_CONTROL_REQUEST)`` before issuing any motion in **Manual or Auto mode**.  
- When multiple clients are connected, only one can have **exclusive control**.  
- To prevent session timeout, periodically call ``manage_access_control(MANAGE_ACCESS_CONTROL_RENEW)``.  
- After completing operations, **release control** explicitly to allow other users or applications to connect safely.  
- In a multi-PC environment, use :ref:`get_robot_state <get_robot_state>` to verify which client currently holds access authority.
