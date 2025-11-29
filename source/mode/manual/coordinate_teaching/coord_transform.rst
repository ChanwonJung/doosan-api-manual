.. _manual_coord_transform:

coord_transform (Manual Mode)
------------------------------------------
This section explains how to use :ref:`coord_transform <coord_transform>` during **Manual (Teach)** operations.  
It converts a given **pose (position + orientation)** from one coordinate system to another  
— for example, from **BASE** to **USER**, or from **TOOL** to **WORLD**.  

During manual teaching, this function is commonly used to **validate frame definitions**,  
check transformation consistency, or preview how a measured point appears in another reference frame  
before committing frame calibration with :ref:`set_user_cart_coord1 <set_user_cart_coord1>`.

**Typical usage**

- Convert a pose captured in the **BASE** frame into the **USER** frame for verification.  
- Compare two poses under different coordinate references.  
- Confirm that the calculated user frame aligns with the expected workpiece geometry.  
- Preview pose relationships before writing to permanent frame data.

.. Note::

    - Input and output are both ``ROBOT_TASK_POSE`` or float[6] arrays in order `[X, Y, Z, Rx, Ry, Rz]`.  
    - Source and target coordinate systems can be **BASE**, **TOOL**, **WORLD**, or any defined **USER** frame.  
    - This function performs only mathematical transformation — it does **not** change the active coordinate frame of the controller.  
    - Combine with :ref:`calc_coord <manual_calc_coord>` to validate computed frames before saving.

**Example: Transform a Measured Pose from BASE → USER Frame**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Assume the robot is in Manual Mode with servo ON
       // and a user frame has been previously defined (USER[1]).
       printf("Verifying pose transformation between BASE and USER[1]...\n");

       // Step 2. Get the current TCP pose in the BASE frame
       LPROBOT_TASK_POSE pBasePose = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
       printf("[BASE Pose]\n");
       printf("X: %.3f, Y: %.3f, Z: %.3f | Rx: %.3f, Ry: %.3f, Rz: %.3f\n",
              pBasePose->_fX, pBasePose->_fY, pBasePose->_fZ,
              pBasePose->_fRx, pBasePose->_fRy, pBasePose->_fRz);

       // Step 3. Transform that pose into the USER frame (temporary check)
       LPROBOT_TASK_POSE pUserPose =
           drfl.coord_transform(pBasePose, COORDINATE_SYSTEM_BASE, COORDINATE_SYSTEM_USER);

       // Step 4. Display transformed pose for comparison
       printf("\n[Transformed Pose - USER Frame]\n");
       printf("x: %.3f, y: %.3f, z: %.3f | rx: %.3f, ry: %.3f, rz: %.3f\n",
              pUserPose->_fX, pUserPose->_fY, pUserPose->_fZ,
              pUserPose->_fRx, pUserPose->_fRy, pUserPose->_fRz);

       // Step 5. Optionally, verify by transforming back USER → BASE
       LPROBOT_TASK_POSE pBaseCheck =
           drfl.coord_transform(pUserPose, COORDINATE_SYSTEM_USER, COORDINATE_SYSTEM_BASE);

       printf("\n[Re-Transformed Pose - BASE Frame]\n");
       printf("X: %.3f, Y: %.3f, Z: %.3f | Rx: %.3f, Ry: %.3f, Rz: %.3f\n",
              pBaseCheck->_fX, pBaseCheck->_fY, pBaseCheck->_fZ,
              pBaseCheck->_fRx, pBaseCheck->_fRy, pBaseCheck->_fRz);

       return 0;
   }

**Tips**

- Use this function to **numerically verify frame correctness** after teaching a new user coordinate.  
- If the transformed position of a known reference point appears offset or rotated,  
  recheck the input sequence used in :ref:`calc_coord <manual_calc_coord>`.  
- During teaching, prefer previewing with ``coord_transform`` before saving to controller memory.  
- Combine with :ref:`get_current_rotm <manual_get_current_rotm>` to confirm orientation integrity across frames.
