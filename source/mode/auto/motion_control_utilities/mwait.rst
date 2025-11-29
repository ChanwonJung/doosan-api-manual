.. _auto_mwait:

mwait (Auto Mode)
------------------------------------------
This section explains how to use :ref:`mwait <mwait>`  
during **Auto (Run)** operations to wait until the robot finishes  
the **previously executed motion command**.

When paired with asynchronous motion commands such as ``amovej`` or ``amovel``,  
this function effectively turns them into **synchronous, sequential** operations—  
ensuring that the next step of the automation process does not begin  
until the robot has completely finished the current movement.

**Typical usage**

- Convert asynchronous motions into synchronous behavior when needed.  
- Ensure the robot completes a movement before triggering the next action.  
- Synchronize robot motion with external devices (e.g., cameras, conveyors).  
- Combine with ``amovej`` or ``amovel`` to allow background processing but still  
  enforce ordered motion execution.

.. Note::

   - Ignored if no previous motion is in progress.  
   - Particularly useful in complex automation pipelines that mix asynchronous and synchronous motion styles.  

**Example: Waiting for Asynchronous Motion to Finish Before Continuing**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // First target joint position
       float targetA[6] = {30, 30, 30, 30, 30, 30};

       // 1) Execute asynchronous motion
       drfl.amovej(targetA, 60, 120);
       printf("Asynchronous motion started.\n");

       // 2) Wait until the robot completes the motion
       if (!drfl.mwait()) {
           printf("Failed to wait for motion completion.\n");
           return -1;
       }

       printf("Motion complete. Executing next command.\n");

       // 3) Execute next synchronous motion
       float targetB[6] = {0, 0, 0, 0, 0, 0};
       drfl.movej(targetB, 40, 80);

       return 0;
   }

In this example, the robot begins an asynchronous motion using ``amovej()``.  
The external program then calls ``mwait()`` to block further execution  
until the motion finishes. After the movement is fully complete,  
the program performs the next motion safely and deterministically.

**Tips**

- Ideal for sequential pipelines where some steps can run in parallel  
  but motion completion must still be guaranteed before the next action.  
- Helps avoid race conditions or unsafe sequencing during Auto Mode.  
- Use whenever timing between robot movement and external systems matters.  
- Can be combined with :ref:`check_motion <auto_check_motion>` for more granular control.  
