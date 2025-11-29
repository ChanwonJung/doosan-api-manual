.. _auto_check_orientation_condition_abs:

check_orientation_condition_abs (Auto Mode)
-------------------------------------------
This section explains how to use :ref:`check_orientation_condition_abs <check_orientation_condition_abs>`
during Auto (Run) operations to verify whether the absolute orientation around a specified axis
falls within a predefined angular range.

It is primarily used to confirm orientation alignment, insertion readiness, and safe rotation limits
in automated assembly or precision motion sequences.

**Typical usage**

- Use **fTargetMin** to check if the angular offset is **greater than or equal to** a threshold.  
- Use **fTargetMax** to check if the angular offset is **less than or equal to** a threshold.  
- Set both **fTargetMin** and **fTargetMax** to check if the current angular deviation is **within the acceptable range**.  
- Commonly used for **positioning tasks** that require rotational alignment or validation during **process automation**.

.. Note::

    - The function uses the **Angle/Axis method** for computing the rotational difference, ensuring the shortest angular distance between the two poses.  
    - When ``eForceReference`` = ``COORDINATE_SYSTEM_TOOL``, the reference orientation should be defined in **BASE coordinates**.  
    - The angular deviation is typically measured in **degrees or radians**, depending on the configuration.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, Auto mode active, servo ON

       // Define target orientation range around Rx–Ry–Rz axes
       float minOri[6] = {0.f, 0.f, 0.f, -10.f, -10.f, -10.f};
       float maxOri[6] = {0.f, 0.f, 0.f, 10.f, 10.f, 10.f};

       // Check orientation deviation around Rz in TOOL coordinate
       bool cond = drfl.check_orientation_condition(FORCE_AXIS_Z, minOri, maxOri, COORDINATE_SYSTEM_TOOL);

       printf("Orientation within range: %s\n", cond ? "TRUE" : "FALSE");
       return 0;
   }

In this example, the function checks whether the current tool orientation lies within ±10°  
of the target orientation around the Z-axis (Rz) within the TOOL coordinate frame.

**Tips**

- Use this function for **automatic alignment checks** before initiating subsequent steps in the process.  
- Combine with :ref:`check_position_condition <auto_check_position_condition>` for full **6D validation** (position and orientation) during automated tasks.  
- Ensure the angle units (deg or rad) are consistent with the system configuration settings.  
- This function is especially useful in **robotic insertion tasks**, **screw driving**, and **fine-tuned assembly** operations, where precise rotational control is critical.
