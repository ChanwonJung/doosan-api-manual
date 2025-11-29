.. _check_position_condition_rel:

check_position_condition_rel
------------------------------------------
This function checks whether the **relative position** of a specified axis lies within the given range  
with respect to a defined **target position**.  
It can be called continuously inside control loops (e.g., ``while`` or ``if``) to monitor real-time motion conditions.

The axis and target position values are interpreted according to the reference coordinate system defined by  
:ref:`set_ref_coord <set_ref_coord>`.  
If ``eForceReference`` is set to ``COORDINATE_SYSTEM_TOOL``, the ``fTargetPos`` should be expressed in the **BASE** coordinate system.

Refer to :ref:`check_position_condition_abs <check_position_condition_abs>` for **absolute** position comparisons.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 957)

.. code-block:: cpp

   bool check_position_condition_rel(FORCE_AXIS eForceAxis,
                                     float fTargetMin,
                                     float fTargetMax,
                                     float fTargetPos[NUM_TASK],
                                     COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL) {
       return _check_position_condition_rel(_rbtCtrl, eForceAxis, fTargetMin, fTargetMax, fTargetPos, eForceReference);
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
     - Axis to evaluate (X, Y, Z, or Rx, Ry, Rz).
   * - fTargetMin
     - float
     - -
     - Minimum allowable deviation from the target position [mm or deg].
   * - fTargetMax
     - float
     - -
     - Maximum allowable deviation from the target position [mm or deg].
   * - fTargetPos
     - float[6]
     - -
     - Reference target position of six task coordinates.
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Reference coordinate system for relative comparison.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Condition **True** — current position within range.
   * - 0
     - Condition **False** — current position outside range.

**Example A — Manual Mode (Position Deviation Check During Teaching)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Teach mode active

       // 1) Define reference target pose
       float posTarget[6] = {400.f, 500.f, 600.f, 0.f, 180.f, 0.f};

       // 2) Check if current X position is within ±5 mm of target
       bool cond = drfl.check_position_condition_rel(FORCE_AXIS_X, -5.f, 5.f, posTarget, COORDINATE_SYSTEM_TOOL);

       printf("Relative X-position condition: %s\n", cond ? "TRUE" : "FALSE");
       return 0;
   }

**Example B — Auto Mode (Insertion Approach Verification)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Robot approaching target under compliance control

   // 1) Define target insertion position
   float targetPose[NUM_TASK] = {550.f, 200.f, 80.f, 180.f, 0.f, 0.f};

   // 2) Move near the insertion point
   drfl.movel(targetPose, (float[2]){80.f, 25.f}, (float[2]){300.f, 100.f});
   drfl.mwait();

   // 3) Check relative position condition along Z-axis
   bool bApproached = drfl.check_position_condition_rel(FORCE_AXIS_Z, -3.f, 2.f, targetPose, COORDINATE_SYSTEM_TOOL);

   if (bApproached)
       printf("Robot within insertion tolerance range.\n");
   else
       printf("Robot not yet in range.\n");

   // 4) Once in range, proceed with next task (e.g., force-controlled insertion)
   if (bApproached) {
       float fTarget[6] = {0.f, 0.f, 20.f, 0.f, 0.f, 0.f};
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);
   }

**Notes & Best Practices**

- Use ``check_position_condition_rel()`` for **fine approach detection**, **alignment checks**, or **position safety thresholds**.  
- When using ``COORDINATE_SYSTEM_TOOL``, always define ``fTargetPos`` in **BASE** coordinates.  
- Combine with :ref:`check_force_condition <check_force_condition>` for hybrid **force-position control** logic.  
- In Auto mode, call within control loops or conditional checks to trigger the next motion or task step dynamically.  
- For absolute coordinate comparison, use :ref:`check_position_condition_abs <check_position_condition_abs>`.
