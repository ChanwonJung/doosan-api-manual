.. _manual_check_position_condition_rel:

check_position_condition_rel (Manual Mode)
--------------------------------------------------------
This section explains how to use :ref:`check_position_condition_rel <check_position_condition_rel>`  
during **Manual (Teach)** operations to verify whether the **relative position** of a specific axis  
is within a defined range compared to a given **target position**.  

It is mainly used for **fine alignment**, **approach verification**, and **assembly precision checks**  
when manually guiding or teaching robot positions relative to reference points.

To view the full API definition and parameter list, refer to  
:ref:`check_position_condition_rel <check_position_condition_rel>` in the **Common API section**.

**Typical usage**

- Evaluate whether the robot’s TCP has reached a **relative distance** from a predefined target pose.  
- Use for **fine-tuning insertion** or **approach distance** in assembly operations.  
- Perform dynamic monitoring in ``while`` or ``if`` loops for position-based event triggering.  
- Combine with :ref:`check_force_condition <manual_check_force_condition>` for **hybrid force–position logic**.

.. Note::

  - This function **does not move the robot**; it only checks the position condition using feedback.

**Example: Verify position offset from target pose**

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
       // - Robot positioned near the target pose

       // 1) Define target position (e.g., previously taught TCP pose)
       float targetPos[6] = {400.f, 500.f, 600.f, 0.f, 180.f, 0.f};

       printf("Checking if TCP X-axis is within ±5 mm from target...\n");

       // 2) Monitor relative offset between current and target position
       while (true) {
           bool inRange = drfl.check_position_condition_rel(FORCE_AXIS_X, -5.f, 5.f, targetPos, COORDINATE_SYSTEM_BASE);

           if (inRange) {
               printf("Relative position condition met: X-axis offset within ±5 mm.\n");
               break;
           } else {
               printf("Not yet within target range, adjusting position...\n");
           }

           std::this_thread::sleep_for(std::chrono::milliseconds(300));
       }

       printf("Position alignment complete.\n");
       return 0;
   }

In this example, the robot continuously checks whether its **X-axis position**  
is within ±5 mm of a predefined target pose. When the relative offset condition is satisfied,  
the loop exits, allowing the operator to proceed with the next step of the teaching process.

**Tips**

- Use this function to verify **fine positional alignment** during manual assembly or contact calibration.  
- Define the ``fTargetPos`` in **BASE** coordinates when checking TOOL-relative offsets.  
- For continuous control tasks, call this function periodically (50–200 ms) within motion loops.  
- Combine with :ref:`check_force_condition <manual_check_force_condition>`  
  for accurate and stable hybrid force–position applications.  
- For static position verification, use :ref:`check_position_condition_abs <manual_check_position_condition_abs>` instead.
