.. _manual_enable_alter_motion:

enable_alter_motion (Manual Mode)
------------------------------------------
This section explains how to use :ref:`enable_alter_motion <enable_alter_motion>` during **Manual (Teach)** operations.  
It activates **alter motion mode**, which lets you apply small trajectory corrections  
while a motion command (e.g., MoveL or MoveJ) is already running.  
This is especially useful for **fine-tuning approach paths**, adjusting tool orientation during contact,  
or visually correcting the TCP position under camera guidance.

**Typical usage**

- Enable before running a fine manual adjustment loop (using :ref:`alter_motion <manual_alter_motion>`).  
- Define movement limits for both **position** and **orientation** to ensure safe manual control.  
- Commonly used in precision teaching tasks such as welding start-point tuning or surface touch alignment.

.. Note::

    - Must be called in **user thread** before any alter commands.  
    - Once enabled, it remains active until explicitly disabled.  
    - The set limits prevent excessive tool displacement or orientation changes.

**Example: Enable Alter Motion with Safety Boundaries**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1: Ensure robot is connected and in Manual Mode
       // (Assume servo ON and safe workspace conditions)

       // Step 2: Define safety limits for manual correction
       float fLimitDpos[2]     = {5.0f, 3.0f};   // ±5 mm (position), ±3° (rotation)
       float fLimitDposPer[2]  = {0.0f, 0.0f};

       // Step 3: Enable alter motion to allow micro path correction
       drfl.enable_alter_motion(5, PATH_MODE_DPOS, COORDINATE_SYSTEM_BASE,
                                fLimitDpos, fLimitDposPer);

       printf("Alter motion enabled. You can now apply small path adjustments.\n");

       return 0;
   }

**Tips**

- Ideal to call just before visual or tactile alignment.  
- Accumulation amount or increment amount isn't be limited if limit_dPOS or limit_dPOS_per is None.
- Once alignment is done, use :ref:`disable_alter_motion <manual_disable_alter_motion>` to finalize the pose.
