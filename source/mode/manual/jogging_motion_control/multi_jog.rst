.. _multi_jog:

multi_jog (Manual Mode)
------------------------------------------
This function performs **simultaneous jog control** for multiple task axes (X, Y, Z, Rx, Ry, Rz)  
of the robot in the controller. Unlike :ref:`jog <jog>`, which moves a single axis at a time,  
`multi_jog` allows **coordinated manual motion** by assigning velocity values for all six axes.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 758)

.. code-block:: cpp

    bool multi_jog(float fTargetPos[NUM_TASK], MOVE_REFERENCE eMoveReference, float fVelocity) {
        return _multi_jog(_rbtCtrl, fTargetPos, eMoveReference, fVelocity);
    };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[NUM_TASK]
     - -
     - Velocity command array for each task axis. |br|
       The array elements correspond to **[X, Y, Z, Rx, Ry, Rz]**. |br|
       Positive and negative values indicate direction and magnitude (% of rated speed).
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - -
     - Coordinate system reference. |br|
       Can be **COORDINATE_SYSTEM_BASE**, **COORDINATE_SYSTEM_TOOL**, or **COORDINATE_SYSTEM_WORLD**.
   * - fVelocity
     - float
     - -
     - Overall scaling factor for the combined jog velocity. |br|
       Used to limit or amplify the motion speed across all axes.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // (Assume connection, mode, and servo activation are completed)

       // Scenario: Simultaneously move along +X and +Y to approach a target diagonally,
       // then tilt the tool slightly in Rx, and finally retreat in the opposite direction.

       // 1) Diagonal jog (+X, +Y) at 15% speed in BASE frame
       float vel1[6] = {15.0f, 15.0f, 0.0f, 0.0f, 0.0f, 0.0f};
       drfl.multi_jog(vel1, MOVE_REFERENCE_BASE, 1.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(800));
       drfl.multi_jog(vel1, MOVE_REFERENCE_BASE, 0.0f); // stop jogging

       // 2) Small tool rotation in +Rx (5%) and -Ry (5%) for alignment
       float vel2[6] = {0.0f, 0.0f, 0.0f, 5.0f, -5.0f, 0.0f};
       drfl.multi_jog(vel2, MOVE_REFERENCE_TOOL, 1.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(600));
       drfl.multi_jog(vel2, MOVE_REFERENCE_TOOL, 0.0f); // stop rotation

       // 3) Retreat diagonally (-X, -Y) for safety
       float vel3[6] = {-10.0f, -10.0f, 0.0f, 0.0f, 0.0f, 0.0f};
       drfl.multi_jog(vel3, MOVE_REFERENCE_BASE, 1.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(500));
       drfl.multi_jog(vel3, MOVE_REFERENCE_BASE, 0.0f);

       return 0;
   }

This example shows a **diagonal and multi-axis teaching operation**:  
the robot first jogs diagonally in the **BASE** frame, performs a **small rotational correction** in the **TOOL** frame,  
and finally executes a **safe retreat motion**. Each motion is maintained for a short duration  
and then halted by setting all target velocities to `0`.
