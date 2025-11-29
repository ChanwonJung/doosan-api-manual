.. _auto_check_motion:

check_motion (Auto Mode)
------------------------------------------
This section explains how to use :ref:`check_motion <check_motion>`  
during **Auto (Run)** operations to monitor the **real-time status**  
of the robot’s active motion command.

The function reports whether the robot is **idle**, **planning a trajectory**,  
or **executing a motion**, making it useful for building sequential or  
condition-based automation flows.

**Typical usage**

- Wait until a motion finishes before starting the next command.  
- Check whether the robot is still planning a trajectory (busy state).  
- Synchronize external systems (vision, conveyor, PLC) with robot movement.  
- Build custom asynchronous motion pipelines in Auto Mode.  

.. Note::

   Return values:  
   - **0** → No motion (idle)  
   - **1** → Motion is being planned (trajectory calculation)  
   - **2** → Motion is currently executing  

**Example: Waiting for Motion Completion Before Executing the Next Move**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float targetA[6] = {0, 0, 90, 0, 90, 0};
       float targetB[6] = {0, 0, 0,  0,  0,  0};

       // 1) Start first motion (asynchronous)
       drfl.amovej(targetA, 60, 30);

       // 2) Poll motion state until the robot becomes idle
       while (true) {
           int status = drfl.check_motion();

           if (status == 0) {            // Idle → previous motion finished
               drfl.movej(targetB, 60, 30);
               printf("First motion completed. Executing next motion.\n");
               break;
           }
       }

       return 0;
   }

In this example, the robot first moves asynchronously to *targetA*.  
The external application repeatedly calls ``check_motion()``  
until the robot reaches an **idle state (0)**, then executes the next motion.

**Tips**

- Ideal for chaining multiple motions without blocking the main thread.  
- Check for **1 (planning)** to detect when the controller is preparing a trajectory.  
- Useful when coordinating robot moves with camera capture or sensor triggers.  
- Combine with asynchronous commands like ``amovej`` and ``amovel``  
  to build advanced Auto Mode workflows.  
