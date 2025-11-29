.. _manual_check_position_condition_abs:

check_position_condition_abs (Manual Mode)
--------------------------------------------------------
This section explains how to use :ref:`check_position_condition_abs <check_position_condition_abs>`  
during **Manual (Teach)** operations to verify whether the **absolute position** of a specific axis  
lies within a defined threshold range.  

It is mainly used for **safety zone validation**, **teaching point confirmation**,  
or **position-dependent task logic** during hand-guiding or step-by-step teaching.

To view the full API definition and parameter list, refer to  
:ref:`check_position_condition_abs <check_position_condition_abs>` in the **Common API section**.

**Typical usage**

- Validate that the robot’s TCP or joint position stays within a predefined **safety boundary**.  
- Monitor whether the robot has reached a desired position range before performing another operation.  
- Use within ``while`` or ``if`` statements to create **conditional movement logic**.  
- Combine with :ref:`check_force_condition <manual_check_force_condition>` for hybrid **position–force control** tasks.

.. Note::

    - This function does not command motion — it only checks current position values from internal feedback.

**Example: Verify position limits before proceeding**

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
       // - Manual (Teach) mode active
       // - Robot positioned near the target region

       printf("Checking TCP Z-axis position within ±5 mm tolerance...\n");

       // 1) Monitor absolute position range along Z-axis in BASE frame
       while (true) {
           bool inZone = drfl.check_position_condition_abs(FORCE_AXIS_Z, -5.f, 5.f, COORDINATE_SYSTEM_BASE);

           if (inZone) {
               printf("Position condition met: Z-axis within ±5 mm.\n");
               break;
           } else {
               printf("Z-axis out of range, adjusting manually...\n");
           }

           std::this_thread::sleep_for(std::chrono::milliseconds(300));
       }

       // 2) Optional safety or confirmation check
       bool withinXY = drfl.check_position_condition_abs(FORCE_AXIS_X, -100.f, 100.f)
                    && drfl.check_position_condition_abs(FORCE_AXIS_Y, -100.f, 100.f);

       if (withinXY)
           printf("Robot within safe XY workspace.\n");
       else
           printf("Outside safe XY zone. Adjust before proceeding.\n");

       return 0;
   }

In this example, the robot continuously checks if its **Z-axis TCP position** is within ±5 mm  
from the reference plane while teaching. Once inside the safe range, the condition becomes ``TRUE`` (1),  
allowing the operator to continue with the next instruction safely.

**Tips**

- Use this function to implement **teaching safeguards**, ensuring the robot remains in safe boundaries.  
- Combine with :ref:`check_force_condition <manual_check_force_condition>` for position-based contact validation.  
- The function can be called periodically (e.g., every 50–200 ms) for smooth real-time monitoring.  
- Always confirm the coordinate reference consistency (TOOL vs BASE vs WORLD)  
  before applying threshold logic.  
- For **relative deviation checks**, use :ref:`check_position_condition_rel <manual_check_position_condition_rel>` instead.
