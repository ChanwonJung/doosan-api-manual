.. _manual_set_safe_stop_reset_type:

set_safe_stop_reset_type (Manual Mode)
------------------------------------------------
This section explains how to use :ref:`set_safe_stop_reset_type <set_safe_stop_reset_type>` during **Manual (Teach)** operations.  
This function sets the **reset behavior** of the robot after a **Safe Stop** or **Protective Stop** occurs.  
It determines whether the robot requires a manual confirmation or can automatically resume operation after a safety event. |br|
In Manual mode, this is typically used to ensure operator acknowledgment before the robot restarts.

**Typical usage**

- Configure the robot’s **Safe Stop recovery policy** during teaching or maintenance.  
- Require **manual reset** after an emergency or protective stop for enhanced operator safety.  
- Enable **automatic reset** for low-risk test or calibration tasks under supervision.  
- Combine with :ref:`get_last_alarm <manual_get_last_alarm>` to log or analyze safety-related events.

.. Note::

    - Should be configured **before starting motion** to ensure proper safety behavior.

**Example: Configure manual reset after a Protective Stop**

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
       // - Safety system initialized

       // 1) Set the reset type to MANUAL for added safety
       if (drfl.set_safe_stop_reset_type(SAFE_STOP_RESET_TYPE_MANUAL))
           std::printf("[Safety] Set Safe Stop Reset Type: MANUAL.\n");
       else
           std::printf("[Safety] Failed to set reset type.\n");

       // 2) Simulate motion or test teaching behavior
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 50, 50);

       // 3) Wait for a potential stop or recovery scenario
       while (drfl.check_motion() != 0)
           std::this_thread::sleep_for(std::chrono::milliseconds(200));

       // 4) (Optional) Log the stop cause
       drfl.get_last_alarm();

       return 0;
   }

**Tips**

- Always use **manual reset** in environments where a human is near the robot during operation.  
- For production-line verification or automated replay testing, ``AUTO`` mode can improve workflow speed.  
- After a stop, ensure reset is complete before sending new motion commands.  
- Combine with :ref:`release_protective_stop <manual_release_protective_stop>` for full recovery logic after a safety stop.
