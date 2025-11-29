.. _manual_disable_alter_motion:

disable_alter_motion (Manual Mode)
------------------------------------------
This section describes how to use :ref:`disable_alter_motion <disable_alter_motion>`  
to **terminate alter motion mode** safely after performing manual path adjustments.  
It restores normal motion control and prevents additional user-thread modifications.

**Typical usage**

- Disable once you’ve completed touch-up or calibration.  
- Prevent accidental operator input from altering the robot’s pose post-alignment.  
- Frequently called before recording new user frames or TCP positions.

.. Note::

    - Immediately deactivates alteration input.  
    - Should be called before switching back to jogging or Auto mode.

**Example: Safely Ending Alter Mode After Manual Correction**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // After performing manual fine-tuning
       printf("Finishing manual trim process...\n");

       drfl.disable_alter_motion();

       printf("Alter motion disabled. Robot control returned to normal state.\n");

       return 0;
   }

**Tips**

- Always disable before changing coordinate frames or saving pose data.  
- If alter mode remains active, it may interfere with future program commands.
