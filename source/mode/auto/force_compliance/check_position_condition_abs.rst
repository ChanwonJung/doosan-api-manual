.. _auto_check_position_condition_abs:

check_position_condition_abs (Auto Mode)
------------------------------------------
This section explains how to use :ref:`check_position_condition_abs <check_position_condition_abs>`  
during **Auto (Run)** operations to verify whether the **absolute position** of a specific axis  
is within a predefined range.  

It is mainly used to confirm **motion completion**, **position safety**, or **sequence transitions**  
in automated processes.

**Typical usage**

- Check if the robot has reached a **target position range** before executing the next step.  
- Verify that the TCP stays within **workspace limits** during automated operation.  
- Combine with :ref:`check_force_condition <auto_check_force_condition>`  
  to implement hybrid **position–force** conditions.  
- Use in loops or conditional statements for motion-based decision logic.

.. Note::
 
  - If ``eForceReference = COORDINATE_SYSTEM_TOOL``,  
    input positions should still be defined in **BASE coordinates**.  

**Example: Check TCP Position Range During Auto Motion**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Servo ON, Auto (Run) mode active

       // 1) Define motion path
       float startPos[6] = {400.f, 300.f, 500.f, 180.f, 0.f, 0.f};
       float endPos[6]   = {400.f, 300.f, 200.f, 180.f, 0.f, 0.f};

       // 2) Move toward the target position
       drfl.movel(endPos, (float[2]){80.f, 30.f}, (float[2]){200.f, 100.f});

       // 3) Continuously check Z-axis absolute position condition
       bool reached = false;
       while (!reached) {
           reached = drfl.check_position_condition_abs(FORCE_AXIS_Z, 195.f, 205.f, COORDINATE_SYSTEM_BASE);
           std::this_thread::sleep_for(std::chrono::milliseconds(100));
       }

       printf("Target Z-position range reached. Proceeding to next task.\n");
       drfl.stop(STOP_TYPE_QUICK);

       return 0;
   }

In this example, the robot moves downward while continuously monitoring  
its absolute Z-axis position. Once the TCP enters the target range (195–205 mm),  
the condition becomes **True**, and the robot stops or continues to the next sequence step.

**Tips**

- Use ``COORDINATE_SYSTEM_BASE`` for general workspace monitoring.  
- Apply narrow position ranges for **precise motion control** and broader ranges for **safe boundaries**.  
- Combine with ``check_force_condition()`` for synchronized force–position checks.  
- Poll periodically (every 50–100 ms) to ensure responsive and safe automation control.
