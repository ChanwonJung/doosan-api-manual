.. _check_orientation_condition_rel:

check_orientation_condition_rel
------------------------------------------
This function checks the **relative rotational difference** between the current tool orientation and a target orientation,  
along a specified axis, within a defined **minimum and maximum angular range**.  
It evaluates whether the angular deviation from the target orientation is within the specified thresholds,  
using the **Angle/Axis** representation for rotation.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 960)

.. code-block:: cpp

   bool check_orientation_condition(FORCE_AXIS eForceAxis,
                                    float fTargetMin[NUM_TASK],
                                    float fTargetMax[NUM_TASK],
                                    float fTargetPos[NUM_TASK],
                                    COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL) {
       return _check_orientation_condition_rel(_rbtCtrl, eForceAxis, fTargetMin, fTargetMax, fTargetPos, eForceReference);
   };

**Parameter**

.. list-table::
   :widths: 24 22 18 36
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eForceAxis
     - :ref:`FORCE_AXIS <enum_force_axis>`
     - -
     - Axis of rotation to evaluate (Rx, Ry, Rz).
   * - fTargetMin
     - float[6]
     - -
     - Minimum acceptable angular deviation (in degrees or radians depending on configuration).
   * - fTargetMax
     - float[6]
     - -
     - Maximum acceptable angular deviation.
   * - fTargetPos
     - float[6]
     - -
     - Target task position (pose reference) used for rotational comparison.
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Coordinate reference for orientation comparison (TOOL or BASE).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - The condition is **True** (orientation within the defined range).
   * - 0
     - The condition is **False** (orientation outside the specified range).

.. figure:: /tutorials/images/mode/check_orientation_condition_rel.png
   :alt: check_orientation_condition_rel
   :width: 80%
   :align: center

   check_orientation_condition_rel

.. raw:: html
      
   <br>     

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Manual (Teach) or Auto mode active

       // Define reference orientation (Rx, Ry, Rz in degrees)
       float posRef[6] = {400.f, 500.f, 600.f, 0.f, 180.f, 0.f};

       // Check if rotation around Ry is within ±15° from the reference orientation in TOOL frame
       bool cond = drfl.check_orientation_condition(FORCE_AXIS_Y, -15.f, 15.f, posRef, COORDINATE_SYSTEM_TOOL);

       printf("Orientation condition result: %s\n", cond ? "TRUE" : "FALSE");
       return 0;
   }

In this example, the function checks whether the current rotation about the **Ry axis**  
is within **±15°** of the reference pose orientation in the TOOL coordinate frame.

**Tips**

- Use this function for **relative orientation tracking** or **angular convergence monitoring** in both Manual and Auto modes.  
- Particularly useful in tasks requiring **screw alignment**, **peg-in-hole**, or **fine rotational adjustments**.  
- Combine with position checks to ensure both **location and orientation** are within desired tolerances.
