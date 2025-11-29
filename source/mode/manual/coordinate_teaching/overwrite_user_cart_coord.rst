.. _manual_overwrite_user_cart_coord:

overwrite_user_cart_coord (Manual Mode)
------------------------------------------
This section explains how to use :ref:`overwrite_user_cart_coord <overwrite_user_cart_coord>`  
to **update (overwrite)** a previously saved user frame during manual teaching.  
It allows fine recalibration of an existing coordinate system without recreating it from scratch.  

**Typical usage**

- Adjust a stored user frame after fixture replacement or thermal drift.  
- Re-teach the frame using new measurement points and overwrite the existing one.  
- Combine with :ref:`calc_coord <manual_calc_coord>` to recompute the frame pose before overwriting.

.. Note::

    - The overwrite operation permanently replaces the target user frame in controller memory.  
    - Ensure that no motion program is using the frame during modification.  
    - For consistency, confirm updated values using :ref:`get_user_cart_coord <manual_get_user_cart_coord>` after overwriting.

**Example: Overwrite User Frame after Visual Recalibration**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Operator visually adjusts tool to new origin position
       printf("Adjusting workpiece origin...\n");
       std::this_thread::sleep_for(std::chrono::seconds(2)); // manual movement assumed

       // Step 2. Capture current TCP as new frame origin
       LPROBOT_TASK_POSE pPose = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);

       // Step 3. Overwrite USER1 frame with new base-relative pose
       drfl.overwrite_user_cart_coord(1, pPose, COORDINATE_SYSTEM_BASE);

       printf("USER1 frame overwritten with current TCP pose.\n");

       // Step 4. Verify by retrieving updated frame
       auto pNew = drfl.get_user_cart_coord(1);
       printf("New Origin: X=%.2f, Y=%.2f, Z=%.2f\n",
              pNew->_fOriginPos[0], pNew->_fOriginPos[1], pNew->_fOriginPos[2]);

       return 0;
   }

**Tips**

- Use after small physical adjustments to maintain positional consistency.  
- Avoid overwriting frames that are used in active motion programs.  
- Always confirm by reading the updated frame and comparing before and after.
