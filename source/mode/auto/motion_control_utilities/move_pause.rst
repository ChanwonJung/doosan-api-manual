.. _auto_move_pause:

move_pause (Auto Mode)
------------------------------------------
This section explains how to use :ref:`move_pause <move_pause>`  
during **Auto (Run)** operations to temporarily **pause an active robot motion**  
without stopping the DRL program itself.

This command is useful when motion must be halted immediately based on  
sensor conditions, inspection requirements, or synchronization with external systems.

**Typical usage**

- Pause movement mid-trajectory when a sensor threshold is reached.  
- Temporarily stop motion to allow vision alignment or operator intervention.  
- Implement conditional motion control in combination with asynchronous moves.  
- Use in advanced automation where motion timing depends on external events.  

.. Note::

   - The function is ignored if no motion is currently active.  
   - Only suspends the motion—DRL program flow continues once motion is resumed.  

**Example: Pausing Motion When Joint Angle Reaches a Threshold**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float target[6] = {0, 0, 90, 0, 90, 0};

       // 1) Start asynchronous joint motion
       drfl.amovej(target, 20, 40);

       // 2) Monitor joint position during motion
       while (true) {
           LPPOSITION pose = drfl.get_current_pose(ROBOT_POSE_JOINT);
           if (!pose) continue;

           // Pause motion when the 3rd joint exceeds 45°
           if (pose->_fTargetPos[2] >= 45) {
               drfl.move_pause();
               printf("Motion paused at J3 >= 45 deg.\n");
               Sleep(3000);  // 3-second wait
               break;
           }
       }

       // 3) Resume the paused motion
       drfl.move_resume();
       printf("Motion resumed.\n");

       return 0;
   }

In this example, the robot continuously monitors joint position  
during asynchronous motion. When the 3rd joint reaches a threshold,  
``move_pause()`` suspends the trajectory, and ``move_resume()``  
continues the motion after a delay.

**Tips**

- Combine with :ref:`move_resume <auto_move_resume>` for dynamic stop/resume control.  
- Works best with asynchronous commands such as ``amovej`` and ``amovel``.  
- Ideal for sensor-driven motion adjustment, inspection, or synchronization routines.  
- Useful when motion should pause without stopping the entire DRL program.  
