.. _manual_set_auto_safety_move_stop:

set_auto_safety_move_stop (Manual Mode)
-------------------------------------------------------
This section explains how to use :ref:`set_auto_safety_move_stop <set_auto_safety_move_stop>` during **Manual (Teach)** operations.  
This function enables or disables the controller’s **automatic safety stop** behavior when a safety signal or risk condition is detected.  

In Manual mode, it is primarily used to test or temporarily override safety stop behavior for diagnostic or calibration purposes.

**Typical usage**

- Enable automatic stopping when a **safety sensor** (e.g., door, scanner) or **collision event** is triggered.  
- Temporarily disable auto-stop during **maintenance or controlled testing** (under strict supervision).  
- Use for verifying safety input signals or evaluating recovery logic after protective stops.  
- Combine with :ref:`set_safe_stop_reset_type <manual_set_safe_stop_reset_type>` to customize recovery policy.

.. Note::

    - When disabled, the controller will **not automatically halt** upon safety input — use only under safe, supervised conditions.  
    - Recommended to re-enable auto stop after diagnostic tasks.

**Example: Enable automatic safety stop during manual teaching**

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
       // - Manual (Teach) mode active

       cout << "[Safety] Enabling automatic safety stop...\n";
       if (drfl.set_auto_safety_move_stop(true))
           cout << "[Safety] Auto safety stop enabled successfully.\n";
       else
           cout << "[Safety] Failed to enable safety stop.\n";

       // Simulate operation and test response
       float qTarget[6] = {0, -30, 90, 0, 90, 0};
       drfl.movej(qTarget, 20, 20);
       this_thread::sleep_for(chrono::seconds(2));

       cout << "[Safety] Temporarily disabling safety stop for controlled test...\n";
       drfl.set_auto_safety_move_stop(false);
       this_thread::sleep_for(chrono::seconds(2));

       cout << "[Safety] Re-enabling safety stop after test.\n";
       drfl.set_auto_safety_move_stop(true);

       return 0;
   }

**Tips**

- Always **re-enable** automatic safety stop after calibration or test procedures.  
- Disabling this feature should only be done under **supervised and low-speed conditions**.  
- Combine with :ref:`get_last_alarm <manual_get_last_alarm>` to verify safety stop events and causes.  
- Useful for validating safety I/O and system integration during teach and setup phases.
