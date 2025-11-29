.. _check_force_condition:

check_force_condition
------------------------------------------
This function checks whether the **measured external force or torque** along a specified axis  
is within a user-defined range (magnitude-based, independent of direction).  
It can be repeatedly evaluated inside ``while`` or ``if`` statements to implement  
conditional logic in both teaching and automatic operation modes.

When measuring **force**, the ``eForceAxis`` is interpreted relative to the reference coordinate system  
defined by :ref:`set_ref_coord <set_ref_coord>`.  
When monitoring **moment**, ``eForceAxis`` corresponds to the tool coordinate.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 955)

.. code-block:: cpp

   bool check_force_condition(FORCE_AXIS eForceAxis,
                              float fTargetMin,
                              float fTargetMax,
                              COORDINATE_SYSTEM eForceReference = COORDINATE_SYSTEM_TOOL) {
       return _check_force_condition(_rbtCtrl, eForceAxis, fTargetMin, fTargetMax, eForceReference);
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
     - Axis to check for force or torque (e.g., FORCE_AXIS_X, Y, Z, Rx, Ry, Rz).
   * - fTargetMin
     - float
     - -
     - Minimum threshold for the measured magnitude.
   * - fTargetMax
     - float
     - -
     - Maximum threshold for the measured magnitude.
   * - eForceReference
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - ``COORDINATE_SYSTEM_TOOL``
     - Reference coordinate frame in which the measurement is interpreted.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Condition **True** — current force/torque magnitude is within range.
   * - 0
     - Condition **False** — current force/torque magnitude is outside range.

**Example A — Manual Mode (Force Validation During Teaching)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Teach mode active

       // 1) Continuously monitor Z-axis force (TOOL frame)
       bool fCond = false;
       while (true) {
           fCond = drfl.check_force_condition(FORCE_AXIS_Z, 5.f, 10.f, COORDINATE_SYSTEM_TOOL);
           if (fCond) {
               printf("Force condition met: 5–10 N on Z-axis.\n");
               break;
           }
       }

       // Continue teaching sequence after contact detection
       return 0;
   }

**Example B — Auto Mode (Force-Based Insertion Trigger)**

.. code-block:: cpp

   // Preconditions:
   // - Auto mode active
   // - Robot in motion with force sensing enabled

   // 1) Approach the insertion point
   float p_target[NUM_TASK] = {550.f, 200.f, 100.f, 180.f, 0.f, 0.f};
   drfl.movel(p_target, (float[2]){100.f, 30.f}, (float[2]){400.f, 150.f});

   // 2) Wait until sufficient contact force is detected on Z-axis
   bool contact = false;
   while (!contact) {
       contact = drfl.check_force_condition(FORCE_AXIS_Z, 15.f, 30.f, COORDINATE_SYSTEM_TOOL);
   }

   printf("Contact detected (Z-force 15–30 N). Proceeding to next step.\n");

   // 3) Once contact detected, apply force control
   float fTarget[6] = {0.f, 0.f, 25.f, 0.f, 0.f, 0.f};
   unsigned char dir[6] = {0, 0, 1, 0, 0, 0};
   drfl.set_desired_force(fTarget, dir, COORDINATE_SYSTEM_TOOL, 0.3f);

**Notes & Best Practices**

- ``check_force_condition()`` compares the **absolute magnitude** of the force or torque (sign ignored).  
- Useful for **contact detection**, **insertion feedback**, or **load verification**.  
- Combine with :ref:`check_position_condition_abs <check_position_condition_abs>` or  
  :ref:`check_position_condition_rel <check_position_condition_rel>` for hybrid force–position conditions.  
- Apply appropriate thresholds to prevent false triggers caused by minor sensor noise.  
- For multi-axis monitoring, call the function separately per axis or integrate it in custom logic loops.  
- To implement active force response after detection, combine with :ref:`set_desired_force <set_desired_force>` and :ref:`release_force <release_force>`.
