.. _manual_check_orientation_condition_rel:

check_orientation_condition_rel (Manual Mode)
--------------------------------------------------------
This function checks the **rotational difference** between the current tool pose and the target pose  
along a specific axis within a defined **minimum and maximum angular range**.  
It measures the **relative orientation** (min–max) from a given reference pose  
and evaluates whether the current orientation satisfies that condition.

The function uses the **Angle/Axis** method to compute the rotational offset  
between the current and reference orientations.  
If the axis is **Rx**, **Ry**, or **Rz**, the comparison is made about the corresponding rotational direction.

**Typical usage**

- Set **fTargetMin** to check if the angular offset is **greater than or equal to** the threshold.  
- Set **fTargetMax** to check if the angular offset is **less than or equal to** the threshold.  
- Set both **fTargetMin** and **fTargetMax** to check if the angular deviation is **within range**.  
- Use this function to monitor **angular convergence** during insertion, alignment, or rotation tasks in manual teaching.

.. Note::

    - The function measures **relative** angular deviation from the reference pose in the specified axis (Rx, Ry, or Rz).  
    - If ``eForceReference`` = ``COORDINATE_SYSTEM_TOOL``, define the reference pose in **BASE coordinates**.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Manual (Teach) mode active

       // 1) Define reference pose (Rx, Ry, Rz in degrees)
       float posRef[6] = {400.f, 500.f, 600.f, 0.f, 180.f, 0.f};

       // 2) Check whether rotation around Ry is within ±15° of the reference orientation
       bool cond = drfl.check_orientation_condition(FORCE_AXIS_Y, -15.f, 15.f, posRef, COORDINATE_SYSTEM_TOOL);

       printf("Orientation condition result: %s\n", cond ? "TRUE" : "FALSE");
       return 0;
   }

In this example, the function checks whether the current rotation about the **Ry axis**  
is within **±15°** of the reference pose orientation in the TOOL coordinate frame.

**Tips**

- Use this function to ensure **angular alignment** before executing tasks such as assembly or insertion.  
- Combine with :ref:`check_position_condition <manual_check_position_condition>` for **full 6D validation** (position and orientation).  
- The angle units (degrees or radians) depend on system settings, so confirm the unit configuration before use.  
- This function is useful in tasks requiring precise rotational alignment, such as **peg-in-hole**, **screw insertion**, and **teaching corrections**.
