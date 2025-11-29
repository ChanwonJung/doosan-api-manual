.. _auto_move_resume:

move_resume (Auto Mode)
------------------------------------------
This section explains how to use :ref:`move_resume <move_resume>`  
during **Auto (Run)** operations to **resume a robot motion** that was previously  
paused using :ref:`move_pause <auto_move_pause>`.

This function continues the exact motion trajectory from the point where it was suspended,  
making it useful for conditional or sensor-driven workflows where motion may need to stop  
temporarily but not be canceled.

**Typical usage**

- Resume motion after a brief inspection or vision-based alignment.  
- Continue movement once an external condition becomes valid again.  
- Restore robot motion after an operator checks the workspace.  
- Use in conjunction with asynchronous motion commands for event-driven automation.  

.. Note::

   - Ignored if there is **no currently paused motion**.  
   - Only resumes motion; the overall DRL program continues running independently.  

**Example: Resuming Motion After a Conditional Pause**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float target[6] = {0, 0, 90, 0, 90, 0};

       // 1) Start asynchronous motion
       drfl.amovej(target, 20, 40);

       // 2) Pause when joint 3 reaches threshold
       while (true) {
           LPPOSITION pos = drfl.get_current_pose(ROBOT_POSE_JOINT);
           if (!pos) continue;

           if (pos->_fTargetPos[2] >= 45) {
               drfl.move_pause();
               printf("Motion paused at J3 >= 45 degrees.\n");
               Sleep(3000);  // Wait three seconds
               break;
           }
       }

       // 3) Resume the paused motion
       if (!drfl.move_resume()) {
           printf("Failed to resume motion.\n");
           return -1;
       }

       printf("Motion resumed.\n");
       return 0;
   }

In this example, ``move_resume()`` is used to continue a suspended trajectory  
after the robot was paused mid-motion based on real-time joint position feedback.

**Tips**

- Always pair with :ref:`move_pause <auto_move_pause>` for full stop/resume control.  
- Effective with asynchronous moves (``amovej``, ``amovel``) in event-based sequences.  
- Ideal for workflows requiring motion interruption without canceling the path.  
- Use for inspection steps, alignment waits, or safety-aware slowdowns.  
