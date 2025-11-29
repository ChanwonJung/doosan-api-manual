.. _manual_set_user_cart_coord2:

set_user_cart_coord (3-point, Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_user_cart_coord2 <set_user_cart_coord2>`  
during **Manual (Teach)** operations.  
It defines a user coordinate system using the **3-point method**,  
where the user specifies three poses: origin, X-direction, and Y-plane points.  

This method defines both position and orientation of the work frame based on real surface data.

**Typical usage**

- Create a user frame aligned to a workpiece surface.  
- Define a frame tilted or rotated relative to BASE.  
- Use for welding jigs, assembly tables, or camera calibration.

.. Note::

    - Inputs: `fTargetPos[3][NUM_TASK]` (O, Xp, Yp) and `fTargetOrg[3]`.  
    - Orientation is automatically computed and normalized.  
    - Must be done carefully to avoid collinear point selection.  
    - Reference (`eTargetRef`) usually set to `COORDINATE_SYSTEM_BASE`.

**Example: Define a Workpiece Frame with 3 Physical Points**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float points[3][NUM_TASK];
       float origin[3];

       printf("Teaching USER frame using 3 physical points...\n");

       // Step 1. Record origin (corner of workpiece)
       auto pO = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
       memcpy(points[0], pO, sizeof(float)*NUM_TASK);
       origin[0] = pO->_fX; origin[1] = pO->_fY; origin[2] = pO->_fZ;

       // Step 2. Move +X and record
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 5.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(600));
       drfl.stop(STOP_TYPE_SLOW);
       auto pX = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
       memcpy(points[1], pX, sizeof(float)*NUM_TASK);

       // Step 3. Move +Y and record
       drfl.jog(JOG_AXIS_TASK_Y, MOVE_REFERENCE_BASE, 5.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(600));
       drfl.stop(STOP_TYPE_SLOW);
       auto pY = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
       memcpy(points[2], pY, sizeof(float)*NUM_TASK);

       // Step 4. Register user frame based on 3-point calibration
       int user_id = drfl.set_user_cart_coord(points, origin, COORDINATE_SYSTEM_BASE);

       printf("USER%d frame successfully defined using 3-point method.\n", user_id);

       return 0;
   }

**Tips**

- Ensure the three points are not collinear and represent the actual plane.  
- Best for slanted surfaces or tilted fixtures.  
- Combine with :ref:`calc_coord <manual_calc_coord>` for pre-verification.  
- Use :ref:`coord_transform <manual_coord_transform>` to validate alignment.
