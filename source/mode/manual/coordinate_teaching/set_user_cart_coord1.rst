.. _manual_set_user_cart_coord1:

set_user_cart_coord (1-point, Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_user_cart_coord1 <set_user_cart_coord1>`  
during **Manual (Teach)** operations.  
It defines a user coordinate system (USER frame) using **one origin pose** relative to a reference coordinate system.  

This is the fastest way to create a simple user frame parallel to the reference frame,  
usually **BASE**.

**Typical usage**

- Define a user frame parallel to BASE but offset in position.  
- Quickly register temporary work frames for short tasks.  
- Simplify teaching when orientation does not need adjustment.

.. Note::

    - Requires only one origin pose: `fTargetPos[NUM_TASK]`.  
    - The orientation of the reference frame (e.g., BASE) is used as-is.  
    - Returns the assigned user frame ID.

**Example: Create USER Frame Parallel to BASE**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Move TCP to the desired new frame origin
       printf("Jog robot to new frame origin...\n");

       // Step 2. Capture current TCP position (relative to BASE)
       LPROBOT_TASK_POSE pCur = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);

       // Step 3. Create USER1 frame parallel to BASE
       int user_id = drfl.set_user_cart_coord(1, (float*)pCur, COORDINATE_SYSTEM_BASE);

       printf("USER%d frame created (parallel to BASE)\n", user_id);

       // Step 4. Verify registration
       auto pUser = drfl.get_user_cart_coord(user_id);
       printf("Origin X=%.2f, Y=%.2f, Z=%.2f\n",
              pUser->_fOriginPos[0], pUser->_fOriginPos[1], pUser->_fOriginPos[2]);

       return 0;
   }

**Tips**

- Use when only positional offset is needed (orientation identical to BASE).  
- Ideal for tabletop or flat fixtures.  
- To modify orientation, use the 3-point or 2-vector method below.
