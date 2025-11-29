.. _manual_alter_motion:

alter_motion (Manual Mode)
------------------------------------------
After enabling alter motion mode with :ref:`enable_alter_motion <manual_enable_alter_motion>`,  
use :ref:`alter_motion <alter_motion>` to apply **incremental real-time corrections**  
to the robot’s motion path while it’s actively moving.  
This allows a human operator to “nudge” or “trim” the TCP position interactively without re-executing a full command.

**Typical usage**

- Perform orientation corrections (e.g., tool leveling, contact alignment).  
- Common in manual welding start-point correction or camera-guided teaching.

.. Note::

    - Can only be called while alter motion mode is active.  
    - Input vector represents `[X, Y, Z, Rx, Ry, Rz]` in **fixed XYZ rotation order**.  

**Example: Incremental TCP Correction During Manual Teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1: Enable alter mode (assume done earlier)
       float fLimitDpos[2] = {5.0f, 3.0f};
       float fLimitDposPer[2] = {0.0f, 0.0f};
       drfl.enable_alter_motion(5, PATH_MODE_DPOS, COORDINATE_SYSTEM_BASE,
                                fLimitDpos, fLimitDposPer);

       // Step 2: Define a correction vector (move downwards)
       float dPos[6] = {0, 0, -0.2f, 0, 0, 0};  // -0.2 mm per cycle

       // Step 3: Apply small corrections in a loop
       for (int i = 0; i < 25; ++i) {
           drfl.alter_motion(dPos);
           std::this_thread::sleep_for(std::chrono::milliseconds(20));
       }

       printf("Manual fine adjustment complete.\n");

       // Step 4: Disable alter mode after completion
       drfl.disable_alter_motion();

       return 0;
   }

**Tips**

- Combine with camera or force feedback for semi-automatic fine-tuning.  
- Execute in a separate thread for smoother, continuous correction.  
- Use smaller increments (≤0.3 mm) when operating close to surfaces.
