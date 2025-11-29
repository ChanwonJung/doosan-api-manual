.. _manual_get_user_cart_coord:

get_user_cart_coord (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_user_cart_coord <get_user_cart_coord>` during **Manual (Teach)** operations.  
It retrieves the **pose (origin and orientation)** of a user-defined coordinate system,  
allowing you to verify or visually confirm previously taught user frames on the pendant or GUI.  

This is essential when validating frame calibration accuracy or reusing a stored frame for new teaching tasks.

**Typical usage**

- Inspect an existing user frame before teaching new positions in that frame.  
- Compare the retrieved origin and orientation with the current TCP pose.  
- Log or visualize user frame data for maintenance or frame re-teaching.  

.. Note::

       - The return type is :ref:`USER_COORDINATE <struct_USER_COORDINATE>`, containing both the frame pose and reference.  
       - Coordinate IDs (0–9) correspond to the user frames stored in the controller.  
       - Retrieving the frame does not affect the currently active coordinate system.

**Example: Display a Stored User Frame**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Retrieve user frame with ID = 1
       LPUSER_COORDINATE pUser = drfl.get_user_cart_coord(1);

       // Step 2. Print origin and orientation
       printf("[USER1 Coordinate]\n");
       printf("Origin: X=%.2f, Y=%.2f, Z=%.2f\n",
              pUser->_fOriginPos[0], pUser->_fOriginPos[1], pUser->_fOriginPos[2]);
       printf("Orientation: Rx=%.2f, Ry=%.2f, Rz=%.2f\n",
              pUser->_fOriginAng[0], pUser->_fOriginAng[1], pUser->_fOriginAng[2]);

       // Step 3. (Optional) Check base reference
       printf("Reference Frame: %d\n", pUser->_iRef);

       return 0;
   }

**Tips**

- Use before performing :ref:`coord_transform <manual_coord_transform>` to verify the source frame.  
- Helps confirm whether the current user frame matches the physical fixture.  
- Always check both **origin** and **orientation** values, not only position.
