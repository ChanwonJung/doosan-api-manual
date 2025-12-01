.. _jog:

jog (Manual Mode)
------------------------------------------
This is a function for executing the control of jog movement for each axis of the robot in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 757)

.. code-block:: cpp

    bool jog(JOG_AXIS eJogAxis, MOVE_REFERENCE eMoveReference, float fVelocity) {
        return _jog(_rbtCtrl, eJogAxis, eMoveReference, fVelocity);
    };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eJogAxis
     - :ref:`JOG_AXIS <enum_jog_axis>` 
     - -
     - Refer to the Definition of Constant and Enumeration Type.
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - -
     - Refer to the Definition of Constant and Enumeration Type.
   * - fVelocity
     - float
     - -
     - **Jog Velocity** |br|
       +: Positive Direction |br|
       0: Stop |br|
       -: Negative Direction

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
       // (Assume connection / mode / servo are already prepared in the sample environment)

       // 1) Coarse approach along BASE +X at 20% speed (hold-to-run style)
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 20.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(800)); // keep jogging for 0.8s
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 0.0f);        // stop jogging

       // 2) Fine approach along TOOL -Z at 5% speed
       drfl.jog(JOG_AXIS_TASK_Z, MOVE_REFERENCE_TOOL, -5.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(600)); // creep closer
       drfl.jog(JOG_AXIS_TASK_Z, MOVE_REFERENCE_TOOL, 0.0f);        // stop jogging

       // 3) Safety back-off along BASE -X at 10% speed, then stop
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, -10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(500));
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 0.0f);

       return 0;
   }

This example demonstrates a teach workflow: a **coarse approach** in the **BASE** frame,  
a **fine approach** in the **TOOL** frame with a small negative Z jog (tool toward the work),  
and a **safety back-off**. Each jog is sustained for a short duration  
and then stopped by sending velocity `0`.
