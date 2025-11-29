.. _check_position_condition:

check_position_condition
------------------------------------------
This function checks whether the **position of a specified axis** lies within a defined range  
with respect to a given **target position**, supporting both **absolute** and **relative** comparison modes.  

When ``eMode`` is ``MOVE_MODE_RELATIVE``, it behaves as  
:ref:`check_position_condition_rel <check_position_condition_rel>`.  
When ``eMode`` is ``MOVE_MODE_ABSOLUTE``, it behaves as  
:ref:`check_position_condition_abs <check_position_condition_abs>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 958)

.. code-block:: cpp

   bool check_position_condition(FORCE_AXIS eForceAxis,
                                 float fTargetMin,
                                 float fTargetMax,
                                 float fTargetPos[NUM_TASK],
                                 MOVE_MODE eMode = MOVE_MODE_ABSOLUTE,
                                 COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL) {
       return _check_position_condition(_rbtCtrl, eForceAxis, fTargetMin, fTargetMax, fTargetPos, eMode, eForceReference);
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
     - Axis to check position condition (X, Y, Z or rotation axes Rx, Ry, Rz).
   * - fTargetMin
     - float
     - -
     - Minimum threshold value for position comparison.
   * - fTargetMax
     - float
     - -
     - Maximum threshold value for position comparison.
   * - fTargetPos
     - float[6]
     - -
     - Reference target task position for comparison (X, Y, Z, Rx, Ry, Rz).
   * - eMode
     - :ref:`MOVE_MODE <enum_move_mode>`
     - ``MOVE_MODE_ABSOLUTE``
     - **Specifies comparison mode** |br|
       MOVE_MODE_ABSOLUTE: compares current position to global coordinates. |br|
       MOVE_MODE_RELATIVE: compares deviation relative to target position.
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Reference coordinate system for comparison (BASE, TOOL, WORLD, etc.).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Condition **True** — position is within defined range.
   * - 0
     - Condition **False** — position is outside defined range.

**Example A — Manual Mode (Teaching Position Validation)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Teach mode active

       // Define reference target pose
       float targetPose[6] = {400.f, 500.f, 600.f, 0.f, 180.f, 0.f};

       // 1) Check relative Z-axis offset from target (±5 mm)
       bool relCond = drfl.check_position_condition(FORCE_AXIS_Z, -5.f, 5.f, targetPose, MOVE_MODE_RELATIVE);

       // 2) Check absolute X-axis position range in BASE frame
       bool absCond = drfl.check_position_condition(FORCE_AXIS_X, 100.f, 200.f, targetPose, MOVE_MODE_ABSOLUTE, COORDINATE_SYSTEM_BASE);

       printf("Relative condition (Z): %s\n", relCond ? "TRUE" : "FALSE");
       printf("Absolute condition (X): %s\n", absCond ? "TRUE" : "FALSE");

       return 0;
   }

**Example B — Auto Mode (Process Approach Detection)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Robot executing approach motion

   // Define target pose for insertion
   float targetPose[NUM_TASK] = {550.f, 200.f, 80.f, 180.f, 0.f, 0.f};

   // Move near target
   drfl.movel(targetPose, (float[2]){80.f, 25.f}, (float[2]){300.f, 100.f});
   drfl.mwait();

   // Check if Z position is within ±3 mm of target (relative check)
   bool inRange = drfl.check_position_condition(FORCE_AXIS_Z, -3.f, 3.f, targetPose, MOVE_MODE_RELATIVE, COORDINATE_SYSTEM_TOOL);

   if (inRange)
       printf("Robot has reached insertion tolerance zone.\n");
   else
       printf("Robot not yet in target range.\n");

   // Proceed to next force-controlled insertion step if within range
   if (inRange) {
       float fForce[6] = {0.f, 0.f, 20.f, 0.f, 0.f, 0.f};
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
       drfl.set_desired_force(fForce, dir, COORDINATE_SYSTEM_TOOL, 0.3f);
   }

**Notes & Best Practices**

- Use ``MOVE_MODE_ABSOLUTE`` for **global safety validation**, zone checks, or workspace boundary logic.  
- Use ``MOVE_MODE_RELATIVE`` for **approach precision**, **fine motion alignment**, or **contact tolerance verification**.  
- When ``eForceReference`` is ``COORDINATE_SYSTEM_TOOL``, define ``fTargetPos`` in **BASE** coordinates.  
- The function only evaluates conditions; it does not perform motion commands.  
- Combine with :ref:`check_force_condition <check_force_condition>` for **hybrid force-position control**.  
- For continuous monitoring, call periodically (every 50–200 ms) inside motion or feedback loops.
