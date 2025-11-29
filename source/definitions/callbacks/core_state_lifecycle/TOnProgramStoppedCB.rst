.. _cb_tonprogramstoppedcb:

TOnProgramStoppedCB
------------------------------------------
This is a callback function for checking if program execution in the robot controller  
has been completely terminated when the program stops due to **errors** or **user commands**  
during execution in **automatic mode**.  |br|
As the callback function is executed automatically upon the event,  
a code that requires excessive execution time (within **50 msec**) should not be performed inside it.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnProgramStoppedCB)(const PROGRAM_STOP_CAUSE);

   // registration API (internal + wrapper)
   DRFL_API void _SetOnProgramStopped(LPROBOTCONTROL pCtrl, TOnProgramStoppedCB pCallbackFunc);
   void SetOnProgramStopped(TOnProgramStoppedCB pCallbackFunc)
   {
       _SetOnProgramStopped(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - eStopCause
     - :ref:`PROGRAM_STOP_CAUSE <enum_PROGRAM_STOP_CAUSE>`
     - -
     - Cause of the program termination (e.g., user stop, error, safety, etc.).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <cstdio>
   using namespace DRAFramework;

   // Called automatically when a running DRL program stops or terminates
   void OnProgramStoppedCB(const PROGRAM_STOP_CAUSE eStopCause)
   {
       switch (eStopCause)
       {
       case PROGRAM_STOP_CAUSE_USER_STOP:
           std::printf("[PROGRAM STOP] User requested stop.\n");
           break;

       case PROGRAM_STOP_CAUSE_ERR_OCCURED:
           std::printf("[PROGRAM STOP] Error occurred during execution.\n");
           // Optionally check for error code or perform recovery logic
           break;

       case PROGRAM_STOP_CAUSE_SAFETY_STOP:
           std::printf("[PROGRAM STOP] Safety stop triggered.\n");
           break;

       case PROGRAM_STOP_CAUSE_NORMAL_END:
           std::printf("[PROGRAM STOP] Program completed normally.\n");
           break;

       default:
           std::printf("[PROGRAM STOP] Unknown stop cause: %d\n", eStopCause);
           break;
       }
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           std::printf("Failed to connect to controller.\n");
           return -1;
       }

       // Register callback for program stop event
       drfl.set_on_program_stopped(OnProgramStoppedCB);

       // Example: start DRL program and wait for callback
       drfl.play_drl_start("example_program");

       while (true) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback is invoked when any DRL program running in Auto mode terminates (normal or abnormal).  
- Use this to perform **cleanup**, **logging**, or **restart preparation** when the program ends.  
- Avoid performing time-consuming operations or blocking calls inside the callback (execution < 50 ms).
