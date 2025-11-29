.. _manual_check_orientation_condition_abs:

check_orientation_condition_abs (Manual Mode)
--------------------------------------------------------
This function evaluates the **orientation difference** between the current tool pose and the target pose along a specified axis.  
It determines whether the angular deviation lies within the defined minimum and maximum thresholds.  

Internally, the controller computes the rotational difference using the **“Angle/Axis”** method,  
where the rotation vector expresses the shortest angular path between the current and target orientations.

This function is commonly used to verify precise tool orientation during **fine alignment**, **insertion**, or **assembly** tasks.  
For example, setting only the **Rx** axis allows checking the rotation offset around the X-axis,  
while ignoring the other rotational components.

**Typical usage**

- Use **fTargetMin** to check if the angular offset is **greater than or equal to** a specified threshold.  
- Use **fTargetMax** to check if the angular offset is **less than or equal to** a specified threshold.  
- Set both **fTargetMin** and **fTargetMax** to check if the current angular deviation is **within range**.  
- Apply this function for tasks like **alignment verification**, **fine rotational adjustments**, and **insertion tasks**.

.. Note::

    - The function uses the **Angle/Axis method** for computing the rotational difference, ensuring minimal rotational distance.  
    - If **eForceReference = COORDINATE_SYSTEM_TOOL**, define the target orientation in **BASE coordinates**.  
    - The angular deviation is measured in **degrees or radians**, depending on the configuration of the system.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Manual (Teach) mode active

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

- Use this function to ensure **alignment accuracy** before task execution, especially for tasks requiring precise rotation.  
- Combine with :ref:`check_position_condition <manual_check_position_condition>` to validate both position and orientation simultaneously.  
- The angle units (deg or rad) are based on the system's configuration settings, so check the system settings beforehand.  
- This function is particularly useful in **peg-in-hole**, **screw insertion**, and **teaching correction** tasks, where precise rotational alignment is crucial.
