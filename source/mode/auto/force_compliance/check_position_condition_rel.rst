.. _auto_check_position_condition_rel:

check_position_condition_rel (Auto Mode)
------------------------------------------
This section explains how to use :ref:`check_position_condition_rel <auto_check_position_condition_rel>`  
during **Auto (Run)** operations to check whether the **relative position** of a specific axis  
is within the defined range with respect to a given **target position**.  

It can be used in repetitive conditions (``while`` or ``if`` statements) to monitor real-time positional limits.  
This function is particularly useful for verifying **approach tolerances**, **alignment checks**, and **motion completion**.

**Typical usage**

- Verify that the robot's TCP is within a defined **relative position range** before proceeding with the next task.  
- Monitor **position deviations** during automated tasks, ensuring the robot stays within safety limits.  
- Combine with :ref:`check_force_condition <auto_check_force_condition>` to implement hybrid **position–force** logic in control loops.  
- Useful in processes like **insertion**, **assembly**, or **surface following**.

.. Note::

    - The function evaluates the **relative displacement** of the current position (TCP) from the provided reference pose (`fTargetPos`) along the given axis (`eForceAxis`).  
    - When using ``COORDINATE_SYSTEM_TOOL``, the reference pose (`fTargetPos`) should be in the **BASE** coordinate system.  
    - If absolute position conditions are needed, use :ref:`check_position_condition_abs <auto_check_position_condition_abs>` instead.

**Example: Relative Position Verification During Automated Motion**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       
       // Preconditions:
       // - Auto mode active
       // - Servo ON
       
       // Define target position (in TOOL frame)
       float targetPos[6] = {400.f, 300.f, 500.f, 0.f, 180.f, 0.f};

       // 1) Move robot to target position
       drfl.movel(targetPos, (float[2]){80.f, 30.f}, (float[2]){200.f, 100.f});
       drfl.mwait();

       // 2) Check if the current Z-position is within a range of ±5 mm of target
       bool condition = drfl.check_position_condition_rel(FORCE_AXIS_Z, -5.f, 5.f, targetPos, COORDINATE_SYSTEM_TOOL);

       if (condition) {
           printf("Relative Z-position condition satisfied.\n");
       } else {
           printf("Relative Z-position condition not met.\n");
       }

       return 0;
   }

This example demonstrates checking the **relative position** of the robot’s TCP (along the Z-axis) against a defined target pose.  
The condition is checked within a specified range (±5 mm) relative to the target pose.

**Tips**

- Use ``check_position_condition_rel()`` to ensure precise positioning during automated tasks, especially for **approaching** or **aligning** tasks.  
- In combination with **hybrid control**, monitor both position and force to ensure safe and efficient task execution.  
- Use **short ranges** for fine adjustments and **broader ranges** for coarse movements.  
- Call this function inside control loops for continuous monitoring and decision-making.
