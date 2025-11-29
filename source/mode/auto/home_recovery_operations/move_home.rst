.. _auto_move_home:

move_home (Auto Mode)
------------------------------------------
This section explains how to use :ref:`move_home <move_home>`  
during **Auto (Run)** operations to execute the robot’s **homing sequence**,  
which returns each joint to its mechanical reference position.

Homing is essential when axes have drifted, lost reference, or require recalibration  
after manual movement, power cycles, or safety events.

**Typical usage**

- Restore all robot joints to their mechanical reference after an error or restart.  
- Realign axes when the robot detects positional drift or homing is required.  
- Ensure a reliable and consistent starting pose before executing an automated task.  
- Perform homing as part of a system initialization sequence.  

.. Note::

   - ``MOVE_HOME_MECHANIC`` is the common mode for standard homing operations.  
   - The second argument (``bRun``) controls whether to **execute (1)** or **stop (0)** the homing motion.  
   - After homing finishes, you may call :ref:`mwait <auto_mwait>` to ensure completion before issuing new moves.  

**Example: Executing a Full Homing Sequence**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Execute the default homing sequence (mechanical reference)
       if (!drfl.move_home(MOVE_HOME_MECHANIC, 1)) {
           printf("Failed to start homing sequence.\n");
           return -1;
       }

       printf("Homing sequence started.\n");

       // 2) Wait until homing motion is completed
       drfl.mwait();
       printf("Homing completed.\n");

       return 0;
   }

In this example, the robot performs a mechanical homing sequence  
to realign all axes. After the motion begins, ``mwait()`` is used  
to ensure that the robot completes homing before proceeding.

**Tips**

- Always perform homing after power cycles or when the robot reports a mastering/homing requirement.  
- Use homing as part of system initialization to guarantee consistent starting conditions.  
- The ``bRun = 0`` option can be used to stop an ongoing homing sequence if needed.  
- Combine with :ref:`get_user_home <auto_get_user_home>` or other positioning commands  
  to define safe recovery motions after homing.  
