.. _manual_fkin:

fkin (Manual Mode)
------------------------------------------
This section explains how to use :ref:`fkin <fkin>` during **Manual (Teach)** operations.  
This function performs **forward kinematics (FK)** calculation —  
it converts a given set of **joint angles** `[J1 ... J6]` into the corresponding **Cartesian pose** `[X, Y, Z, Rx, Ry, Rz]`.  
It is commonly used to **verify taught joint configurations**,  
visualize TCP position, or confirm the correctness of inverse kinematics calculations.

**Typical usage**

- Compute the TCP or flange pose corresponding to a known set of joint values.  
- Validate that a manually entered or recorded joint pose leads to the expected Cartesian position.  
- Check forward/inverse kinematics consistency during calibration or debugging.  
- Log end-effector poses during joint-space motion teaching.

.. Note::

    - This function performs **only a mathematical computation** and does **not** move the robot.  
    - For the inverse process, use :ref:`ikin <manual_ikin>`.

**Example: Compute Cartesian pose from joint angles**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // Step 1. Define joint angles (degrees)
       float jointAngles[NUM_JOINT] = {0.0f, -30.0f, 60.0f, 0.0f, 45.0f, 0.0f};

       // Step 2. Compute forward kinematics in BASE frame
       LPROBOT_POSE pPose = drfl.fkin(jointAngles, COORDINATE_SYSTEM_BASE);

       // Step 3. Display result
       if (pPose) {
           printf("[FK Result] X=%.3f  Y=%.3f  Z=%.3f  |  Rx=%.3f  Ry=%.3f  Rz=%.3f\n",
                  pPose->_fX, pPose->_fY, pPose->_fZ,
                  pPose->_fRx, pPose->_fRy, pPose->_fRz);
       } else {
           printf("[FK Result] Calculation failed.\n");
       }

       return 0;
   }

In this example, a predefined joint configuration is passed to :ref:`fkin <fkin>`,  
which returns the TCP pose in the **BASE** coordinate system.  
It provides a quick way to **visualize robot posture** and **numerically verify pose accuracy**  
before commanding physical motion or recording the frame.

**Tips**

- Ideal for **pose verification**, **simulation**, or **frame calibration** in Manual mode.  
- Use together with :ref:`ikin <manual_ikin>` to cross-check consistency between FK and IK results.  
- For TCP validation, compare FK output with :ref:`get_current_posx <manual_get_current_posx>`.  
- Ensure units match (degrees for joint angles, millimeters for Cartesian coordinates).
