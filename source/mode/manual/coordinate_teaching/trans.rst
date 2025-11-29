.. _manual_trans:

trans (Manual Mode)
------------------------------------------
This section explains how to use :ref:`trans <trans>` during **Manual (Teach)** operations.  
This function performs a **translational and rotational offset transformation**  
on a given pose or position vector.  
It allows users to calculate a **new pose shifted by a given offset** in a specified reference frame  
— for example, moving a taught point by +50 mm along the Z-axis of the TOOL coordinate system.

**Typical usage**

- Apply small **offsets** to taught positions without re-teaching (e.g., +Z = 50 mm).  
- Compute a **target point** relative to the current TCP pose during calibration.  
- Adjust approach or retreat positions in **BASE** or **TOOL** coordinates.  
- Validate positional shifts numerically before applying actual motion commands.

.. Note::

    - This function performs **pure mathematical transformation** — it does **not** move the robot.

**Example: Calculate an offset position relative to the current TCP**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // Step 1. Get current TCP pose in TOOL frame
       float curPos[NUM_TASK] = {0};
       LPROBOT_TASK_POSE pCurPose = drfl.get_current_posx(COORDINATE_SYSTEM_TOOL);
       curPos[0] = pCurPose->_fX;  curPos[1] = pCurPose->_fY;  curPos[2] = pCurPose->_fZ;
       curPos[3] = pCurPose->_fRx; curPos[4] = pCurPose->_fRy; curPos[5] = pCurPose->_fRz;

       // Step 2. Define an offset (move 50 mm forward in TOOL Z)
       float offset[NUM_TASK] = {0, 0, 50, 0, 0, 0};

       // Step 3. Compute the new pose using trans()
       LPROBOT_POSE pNewPose = drfl.trans(curPos, offset,
                                          COORDINATE_SYSTEM_TOOL,
                                          COORDINATE_SYSTEM_TOOL);

       // Step 4. Print the result
       printf("[Offset Pose] X=%.3f  Y=%.3f  Z=%.3f  |  Rx=%.3f  Ry=%.3f  Rz=%.3f\n",
              pNewPose->_fX, pNewPose->_fY, pNewPose->_fZ,
              pNewPose->_fRx, pNewPose->_fRy, pNewPose->_fRz);

       return 0;
   }

In this example, the current TCP pose is retrieved in the **TOOL** frame,  
and a +50 mm offset along the tool’s Z-axis is applied.  
The resulting pose can be used as a **new target** for precise approach or retreat motions  
without manually re-teaching or moving the robot.

**Tips**

- Ideal for **approach/retreat path calculations** in Manual mode.  
- Combine with :ref:`coord_transform <manual_coord_transform>` to switch between coordinate frames.  
- Use TOOL frame offsets for end-effector-aligned adjustments (e.g., insertion or polishing).  
- Confirm the direction of the applied offset to avoid frame-orientation confusion.
