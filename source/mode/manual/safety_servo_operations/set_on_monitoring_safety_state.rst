.. _manual_set_on_monitoring_safety_state:

set_on_monitoring_safety_state (Manual Mode)
-------------------------------------------------------
This section explains how to use :ref:`set_on_monitoring_safety_state <set_on_monitoring_safety_state>` during **Manual (Teach)** operations.  
This function registers a **callback** that is triggered whenever the robot’s **safety state changes** — such as entering or leaving a protective stop,  
switching between safety modes, or detecting a safety-related fault.

**Typical usage**

- Monitor **real-time safety state transitions** during manual teaching.  
- Log or display safety status changes (e.g., Protective Stop, Reduced Mode, Safety Error).  
- Trigger user-defined recovery or alert routines in response to safety events.

.. Note::

    - The callback executes automatically whenever the controller’s **safety state** updates.  
    - The monitoring continues until explicitly replaced or the connection is closed.  
    - The callback should be lightweight — avoid blocking operations or long computations inside it.

**Example: Register a safety state monitoring callback**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   // 1) Define the callback function
   void OnSafetyStateChanged(const LPROBOT_MONITORING_SAFETY_STATE pSafety) {
       std::printf("[Safety State Changed]\n");
       std::printf(" Mode: %d | Protective Stop: %d | Reduced Mode: %d | Error: %d\n",
                   pSafety->_iSafetyMode,
                   pSafety->_bProtectiveStop,
                   pSafety->_bReducedModeActive,
                   pSafety->_bSafetyError);
   }

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 2) Register safety monitoring callback
       drfl.set_on_monitoring_safety_state(OnSafetyStateChanged);
       std::printf("[Safety Monitor] Safety state callback registered.\n");

       // 3) Keep program running to receive events
       while (true) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       return 0;
   }

**Tips**

- Use this callback to detect transitions such as: |br|
    - Entering **Protective Stop** or **Emergency Stop**  
    - Switching between **Normal** and **Reduced Speed** modes  
    - Occurrence or clearance of **Safety Faults**  
- For comprehensive status diagnostics, combine this with: |br|
    - :ref:`get_safety_configuration_ex <manual_get_safety_configuration_ex2>` or  
        :ref:`get_safety_configuration_ex_v3 <manual_get_safety_configuration_ex2_v3>` to inspect configuration details  
    - :ref:`release_protective_stop <manual_release_protective_stop>` for controlled recovery  
- Avoid heavy logic in the callback — delegate extended processing to a separate thread or event handler.  
- The callback remains valid until manually re-registered or the session is terminated.
