.. _auto_check_orientation_condition_rel:

check_orientation_condition_rel (Auto Mode)
-------------------------------------------
This section explains how to use :ref:`check_orientation_condition_rel <check_orientation_condition_rel>`
during Auto (Run) operations to verify whether the relative orientation between the current pose
and a reference pose lies within a specified angular range.

It is useful for monitoring orientation offsets, ensuring approach tolerances,
and validating alignment conditions during automated tasks.

**Typical usage**

- Set **fTargetMin** to check if the angular offset is **greater than or equal to** the threshold.  
- Set **fTargetMax** to check if the angular offset is **less than or equal to** the threshold.  
- Set both **fTargetMin** and **fTargetMax** to check if the angular deviation is **within range**.  
- Use this function in automated tasks such as **alignment**, **insertion**, and **robotic assembly** for checking orientation convergence.

.. Note::

    - The function measures **relative** angular deviation from the reference pose in the specified axis (Rx, Ry, or Rz).  
    - The angle unit (degrees or radians) depends on the system configuration.  
    - If ``eForceReference`` = ``COORDINATE_SYSTEM_TOOL``, define the reference pose in **BASE coordinates**.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, Auto mode active, servo ON

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

- Use this function to ensure **angular alignment** before executing automated tasks such as insertion, assembly, or robotic positioning.  
- Combine with :ref:`check_position_condition <auto_check_position_condition>` for **full 6D validation** (position and orientation) in robotic control.  
- The angle units (degrees or radians) depend on system settings, so confirm the unit configuration before use.  
- This function is particularly useful in **robotic assembly**, **peg-in-hole**, **screw insertion**, and **robot teaching correction** processes where precise rotational alignment is crucial.
