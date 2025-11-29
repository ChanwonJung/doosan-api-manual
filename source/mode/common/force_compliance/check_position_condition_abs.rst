.. _check_position_condition_abs:

check_position_condition_abs
------------------------------------------
This function checks whether the **absolute position** of a specified axis lies within a defined range.  
It can be repeatedly evaluated inside conditional statements (e.g., ``while`` or ``if``)  
to monitor positional conditions in both teaching and automatic operations.

The input axis and range are interpreted according to the reference coordinate system  
defined by :ref:`set_ref_coord <set_ref_coord>`.  
If ``eForceReference`` is set to ``COORDINATE_SYSTEM_TOOL``,  
the position comparison is performed relative to the **BASE** coordinate system.

Refer to :ref:`check_position_condition_rel <check_position_condition_rel>` for **relative position** monitoring.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 956)

.. code-block:: cpp

   bool check_position_condition_abs(FORCE_AXIS eForceAxis,
                                     float fTargetMin,
                                     float fTargetMax,
                                     COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL) {
       return _check_position_condition_abs(_rbtCtrl, eForceAxis, fTargetMin, fTargetMax, eForceReference);
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
     - Axis to check the position range (X, Y, Z, Rx, Ry, Rz).
   * - fTargetMin
     - float
     - -
     - Minimum absolute threshold for the position value.
   * - fTargetMax
     - float
     - -
     - Maximum absolute threshold for the position value.
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Reference coordinate system for position comparison (TOOL, BASE, or WORLD).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Condition **True** — current position is within range.
   * - 0
     - Condition **False** — current position is outside range.

**Example A — Manual Mode (Teaching Position Validation)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Teach mode active

       // 1) Verify position conditions within defined ranges
       bool cx = drfl.check_position_condition_abs(FORCE_AXIS_X, 300.f, 400.f, COORDINATE_SYSTEM_BASE);
       bool cy = drfl.check_position_condition_abs(FORCE_AXIS_Y, -500.f, 500.f);
       bool cz = drfl.check_position_condition_abs(FORCE_AXIS_Z, 100.f, 200.f);

       printf("Check X,Y,Z positions: %d %d %d\n", cx, cy, cz);
       return 0;
   }

**Example B — Auto Mode (Process Position Monitoring)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Robot performing automated positioning

   // 1) Move toward a target point
   float p_target[NUM_TASK] = {550.f, 200.f, 120.f, 180.f, 0.f, 0.f};
   drfl.movel(p_target, (float[2]){100.f, 30.f}, (float[2]){400.f, 150.f});
   drfl.mwait();

   // 2) Verify position range for insertion readiness
   bool withinZ = drfl.check_position_condition_abs(FORCE_AXIS_Z, 90.f, 130.f, COORDINATE_SYSTEM_TOOL);
   bool withinY = drfl.check_position_condition_abs(FORCE_AXIS_Y, 180.f, 220.f, COORDINATE_SYSTEM_BASE);

   if (withinZ && withinY)
       printf("Robot within safe approach zone.\n");
   else
       printf("Robot out of expected range — check target alignment.\n");

   // 3) Proceed with force-controlled insertion once within range
   if (withinZ && withinY) {
       float fTarget[6] = {0.f, 0.f, 25.f, 0.f, 0.f, 0.f};
       unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
       drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);
   }

**Notes & Best Practices**

- Use ``check_position_condition_abs()`` to monitor **workspace limits**, **approach validation**, or **safety thresholds**.  
- Always ensure the coordinate frame consistency between your target and reference (TOOL vs BASE).  
- Combine with :ref:`check_force_condition <check_force_condition>` for hybrid **position–force control** logic.  
- In Auto mode, check position conditions dynamically to trigger the next motion phase.  
- For relative deviation monitoring (e.g., offset from a target pose), use :ref:`check_position_condition_rel <check_position_condition_rel>`.
