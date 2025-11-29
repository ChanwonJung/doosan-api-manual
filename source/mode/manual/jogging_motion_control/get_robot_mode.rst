.. _manual_get_robot_mode:

get_robot_mode (Manual Mode)
------------------------------------------
This section describes how to use :ref:`get_robot_mode <get_robot_mode>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, this function is essential for checking whether the robot is in **Manual (Teach)** or **Auto** mode.

**Typical usage**

- Verify the robot’s current operation mode before sending jog or motion commands.  
- Automatically adjust GUI or input permissions depending on mode.  
- Prevent unintended auto commands when in manual state.

.. Note::

    - Typical values: |br|
    - ``ROBOT_MODE_MANUAL``: Teach pendant or manual control. |br|
    - ``ROBOT_MODE_AUTO``:  Program or external control. |br|
    - In manual teaching, this should return **ROBOT_MODE_MANUAL**.

**Example: Ensure Robot is in Manual Mode**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       ROBOT_MODE mode = drfl.get_robot_mode();
       if (mode == ROBOT_MODE_MANUAL) {
           printf("Robot is in Manual mode. Jogging enabled.\n");
           drfl.jog(JOG_AXIS_TASK_Y, MOVE_REFERENCE_BASE, 10.0f);
       } else {
           printf("Robot is not in Manual mode. Jogging disabled.\n");
       }

       return 0;
   }

**Tips**

- Always confirm **Manual mode** before manual motion or teaching.  
- For safety, restrict jog or multi_jog commands when in Auto mode.  
- Integrate this check into any teaching GUI or remote jog control application.
