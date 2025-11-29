.. _manual_set_user_cart_coord3:

set_user_cart_coord (2-vector, Manual Mode)
-------------------------------------------------
This section explains how to use :ref:`set_user_cart_coord3 <set_user_cart_coord3>`  
during **Manual (Teach)** operations.  
It defines a user coordinate system using the **2-vector method**,  
where two direction vectors and one origin point are provided.  

This approach is preferred when direction vectors are already known  
(e.g., from CAD or vision alignment).

**Typical usage**

- Define precise frames using known direction vectors (e.g., from measured normals).  
- Align coordinate frames using sensor or camera-derived axis data.  
- Common in automation or vision-guided calibration tasks.

.. Note::

    - Inputs: `fTargetVec[2][3]` (two direction vectors: X and Y) + `fTargetOrg[3]` (origin).  
    - Orientation is normalized internally for orthogonality.  
    - Provides highly accurate frame definition when vector data is known.  
    - The reference coordinate system (`eTargetRef`) defines the source frame (commonly BASE).

**Example: Define Frame from Measured Direction Vectors**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Define direction vectors and origin (example values)
       float vecXY[2][3] = {
           {1.0f, 0.0f, 0.0f},   // +X direction vector
           {0.0f, 1.0f, 0.0f}    // +Y direction vector
       };
       float origin[3] = {200.0f, 100.0f, 150.0f};  // mm

       // Step 2. Create user frame using 2-vector definition
       int user_id = drfl.set_user_cart_coord(vecXY, origin, COORDINATE_SYSTEM_BASE);

       printf("USER%d frame defined using 2-vector method.\n", user_id);

       // Step 3. Verify by retrieving the new frame
       auto pUser = drfl.get_user_cart_coord(user_id);
       printf("Origin: X=%.2f Y=%.2f Z=%.2f\n",
              pUser->_fOriginPos[0], pUser->_fOriginPos[1], pUser->_fOriginPos[2]);

       return 0;
   }

**Tips**

- Use when vector directions are pre-computed or measured by external sensors.  
- Recommended for automated frame calibration or offline programming.  
- To verify orthogonality, compare with :ref:`get_orientation_error <get_orientation_error>`.  
- Avoid using raw vectors from noisy data without normalization.
