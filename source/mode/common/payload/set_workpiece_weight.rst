.. _set_workpiece_weight:

set_workpiece_weight
------------------------------------------
This function configures the **weight and center of gravity (COG)** of the currently mounted workpiece.  
It combines the tool parameters (set via :ref:`set_tool <set_tool>`) with the workpiece’s own weight and balance information  
to calculate the total end-effector dynamics used in control and safety calculations.  

It is particularly useful for tasks where the workpiece mass changes dynamically or multiple payloads are handled.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 677)

.. code-block:: cpp

    bool set_workpiece_weight(
        float fWeight = 0.0,
        float fCog[3] = COG_DEFAULT,
        COG_REFERENCE eCogRef = COG_REFERENCE_TCP,
        ADD_UP eAddUp = ADD_UP_REPLACE,
        float fStartTime = -10000,
        float fTransitionTime = -10000
    ) {
        return _set_workpiece_weight(_rbtCtrl, fWeight, fCog, eCogRef, eAddUp, fStartTime, fTransitionTime);
    };

.. Caution::
   - Workpiece weight change is allowed **only when both Collision Detection and TCP SLF Violation check are muted** or disabled during Auto Mode. |br| 
   - In the current version, Collision Detection considers the function mute when Collision Sensitivity is overridden to 0 and TCP SLF considers the function mute when the TCP SLF Limit is overridden to the maximum. This override can be set using Collision Sensitivity Reduction Zone and Custom Zone.
   - Otherwise, trigger an SS1 protective stop unless the workpiece weight is set to zero.
   - If the robot stops due to an error and needs to be manually restored, place the robot in the desired position in the Recovery Mode and unload the workpiece through Servo On and I/O operation while the corresponding zones are activated in Auto Mode.
   - When changing the set tool weight, the workpiece weight is initialized to 0.
   - When using the :ref:`set_tool <set_tool>` and :ref:`set_workpiece_weight <set_workpiece_weight>` in succession, you must use the :ref:`wait <mwait>` function as much as transition_time between time. Otherwise, there may be errors in the weight change.

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fWeight
     - float
     - 0.0
     - Workpiece weight in kilograms (kg).
   * - fCog
     - float[3]
     - [0, 0, 0]
     - Center of gravity of the workpiece in millimeters [x, y, z].
   * - eCogRef
     - :ref:`COG_REFERNCE <enum_cog_reference>`
     - COG_REFERENCE_TCP
     - Reference coordinate system for the COG.
   * - eAddUp
     - :ref:`ADD_UP <enum_add_up>`
     - ADD_UP_REPLACE
     - **Behavior when updating workpiece info** |br|
       DR_REPLACE(0): Replace existing workpiece |br|  
       DR_ADD(1): Add workpiece data  |br|
       DR_REMOVE(2): Remove existing workpiece
   * - fStartTime
     - float
     - -10000
     - Start time (in seconds) for the workpiece weight change.
   * - fTransitionTime
     - float
     - -10000
     - Transition time (in seconds) for gradually applying weight change.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — workpiece weight not applied
   * - 1
     - Success — weight and COG information successfully updated

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set safety mode to autonomous before changing payload info
       drfl.set_safety_mode(SAFETY_MODE_AUTONOMOUS, SAFETY_MODE_EVENT_NONE);

       // Apply new workpiece weight (2.5 kg) with COG at (0, 0, 50 mm)
       float fCog[3] = {0.f, 0.f, 50.f};
       drfl.set_workpiece_weight(2.5f, fCog);

       // Stop autonomous mode once weight setting is done
       drfl.set_safety_mode(SAFETY_MODE_AUTONOMOUS, SAFETY_MODE_EVENT_STOP);
   }

This example demonstrates how to safely apply a new workpiece weight and COG configuration  
while switching to autonomous mode to ensure smooth transition without triggering safety stops.
