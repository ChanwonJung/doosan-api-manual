.. _manual_config_program_watch_variable:

config_program_watch_variable (Manual Mode)
------------------------------------------------------
This section explains how to use :ref:`config_program_watch_variable <config_program_watch_variable>`  
during **Manual (Teach)** operations.  
This function registers variables to be **monitored and displayed on the Teach Pendant (TP)** Watch tab  
while a DRL program is running or being manually executed.  
It allows operators to track variable values such as speed, torque, counters, or user-defined parameters in real time.

**Typical usage**

- Display selected variables on the TP for visual feedback during manual teaching.  
- Monitor changing process values (e.g., force, position, loop counters) while adjusting motions.  
- Debug user-defined DRL variables interactively without pausing the program.  
- Use with sensor or parameter tuning tasks for live observation.

.. Note::

    - The watch list can display multiple variables simultaneously.

**Example: Register and monitor custom teaching variables**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   CDRFLEx drfl;

   int main()
   {
       drfl.open_connection("192.168.137.100");

       // Example 1: Global variable - teaching speed
       bool result1 = drfl.config_program_watch_variable(VARIABLE_TYPE_GLOBAL,
                                                         DATA_TYPE_FLOAT,
                                                         "teach_speed",
                                                         "0.25");
       if (result1)
           cout << "[WATCH] Added variable 'teach_speed' (0.25)\n";

       // Example 2: Program variable - counter
       bool result2 = drfl.config_program_watch_variable(VARIABLE_TYPE_PROGRAM,
                                                         DATA_TYPE_INT,
                                                         "cycle_count",
                                                         "10");
       if (result2)
           cout << "[WATCH] Added variable 'cycle_count' (10)\n";

       // Example 3: String variable - operator name
       drfl.config_program_watch_variable(VARIABLE_TYPE_GLOBAL,
                                          DATA_TYPE_STRING,
                                          "operator_name",
                                          "\"John\"");
       cout << "[WATCH] Registered string variable 'operator_name' = John\n";

       cout << "[Teach] You can now view these variables in TP > Watch tab.\n";

       // Keep process alive for TP observation
       while (true)
           this_thread::sleep_for(chrono::seconds(3));

       return 0;
   }

When called, this function adds the specified variables to the **TP Watch panel**  
for real-time observation during teaching or DRL program execution.  
It helps users **verify logic correctness, parameter updates, and dynamic state changes**  
without interrupting robot operation.

**Tips**

- Use for live monitoring of global or program variables during teaching.  
- Combine with :ref:`set_on_tp_log <set_on_tp_log>` to track variable changes alongside log messages.  
- Useful for debugging loops, counters, and tuning parameters in real time.