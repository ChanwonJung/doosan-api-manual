.. _manual_get_control_mode:

get_control_mode (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_control_mode <get_control_mode>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, this function is critical for verifying the **current control mode** of the robot  
before or during manual teaching.

**Typical usage**

- Confirm whether the robot is under **position**, **compliance**, or **external (real-time)** control.  
- Prevent accidental motion commands in the wrong control mode.  
- Used before jogging, force teaching, or switching between operation modes.

.. Note::

    - Typical modes include ``POSITION_CONTROL``, ``COMPLIANCE_CONTROL``, and ``DIRECT_TELEOP``.  
    - In manual teaching, it should usually report **POSITION_CONTROL**.

**Example: Checking Control Mode before Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Check current control mode before teaching
       CONTROL_MODE ctrl = drfl.get_control_mode();
       printf("Current Control Mode: %d\n", ctrl);

       if (ctrl == POSITION_CONTROL) {
           printf("Safe to jog in position control.\n");
           drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 10.0f);
       } else {
           printf("Jogging disabled: not in position control mode.\n");
       }

       return 0;
   }

**Tips**

- Always check the control mode before enabling jog or external force teaching.  
- If the mode is not `POSITION_CONTROL`, switch modes through the pendant or API command.  
- Helps prevent unexpected motion when switching between auto and manual control.
