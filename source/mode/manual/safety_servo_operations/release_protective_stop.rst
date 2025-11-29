.. _manual_release_protective_stop:

release_protective_stop (Manual Mode)
------------------------------------------
This section explains how to use :ref:`release_protective_stop <release_protective_stop>` during **Manual (Teach)** operations.  
This function releases the robot from a **protective stop state**, which occurs when a safety event or collision is detected.  
After the protective stop is cleared and verified, this command allows the robot to return to a normal operational state.

**Typical usage**

- Manually release the robot from a **protective or safety stop** condition after confirming it is safe to resume operation.  
- Reset safety-related errors (e.g., collision detection, protective zone violation) following inspection.  
- Resume motion or teaching once the stop condition has been cleared and acknowledged.

.. Note::

    - The robot must be in a **stopped and safe condition** before release can occur.  
    - Releasing a protective stop **does not re-enable servo power** — call :ref:`servo_off <manual_servo_off>` or re-enable motion as needed.

**Example: Release protective stop and resume manual operation**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Robot currently halted by a protective stop (collision, zone violation, etc.)

       // 1) Attempt to release protective stop
       if (drfl.release_protective_stop(RELEASE_MODE_MANUAL))
           std::printf("[Protective Stop] Released successfully (Manual Mode).\n");
       else {
           std::printf("[Protective Stop] Release failed. Confirm safety conditions.\n");
           return -1;
       }

       // 2) Wait for the robot state to return to idle
       while (drfl.check_motion() != 0)
           std::this_thread::sleep_for(std::chrono::milliseconds(200));

       // 3) Resume manual jog or motion after verification
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 50, 50);
       drfl.mwait();

       std::printf("[Protective Stop] Robot motion resumed.\n");
       return 0;
   }

**Tips**

- Always perform **visual inspection** and confirm safe clearance before calling this function.  
- For repetitive or automated releases, prefer ``RELEASE_MODE_AUTOMATIC`` only in controlled environments.  
- If the release fails repeatedly, check safety configuration via :ref:`get_safety_configuration_ex2 <manual_get_safety_configuration_ex2>` or  
  :ref:`get_safety_configuration_ex2_v3 <manual_get_safety_configuration_ex2_v3>`.  
- After a protective stop, you may need to **re-enable servo power** before motion can resume.  
- Combine with :ref:`set_safety_mode <manual_set_safety_mode>` for complete recovery procedures after safety events.
