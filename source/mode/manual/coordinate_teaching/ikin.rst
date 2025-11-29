.. _manual_ikin:

ikin (Manual Mode)
------------------------------------------
This section explains how to use :ref:`ikin <ikin>` during **Manual (Teach)** operations.  
This function computes the **inverse kinematics (IK)** solution for a given target pose.  
It converts a desired Cartesian position and orientation `[X, Y, Z, Rx, Ry, Rz]`  
into the corresponding **joint angles** `[J1 ... J6]`,  
allowing users to verify or simulate reachable configurations before actual motion execution.

**Typical usage**

- Calculate joint angles for a **desired TCP pose** without moving the robot.  
- Validate whether a target position is **kinematically reachable**.  
- Compare multiple IK solutions (solution spaces) for collision-free teaching.  
- Generate approach or backup poses numerically during calibration.

.. Note::

    - This function does **not** move the robot; it only performs mathematical IK computation.  
    - For direct motion, use :ref:`movej <auto_movej>` or :ref:`movel <auto_movel>` with the calculated result.

**Example: Compute joint angles for a target pose**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // Step 1. Define a target pose (in BASE frame)
       float targetPose[NUM_TASK] = {400.0f, 0.0f, 300.0f, 180.0f, 0.0f, 180.0f};

       // Step 2. Select solution space (0: default / elbow-down)
       unsigned char solSpace = 0;

       // Step 3. Perform inverse kinematics calculation
       LPROBOT_POSE pJoints = drfl.ikin(targetPose, solSpace, COORDINATE_SYSTEM_BASE);

       // Step 4. Print the computed joint values
       if (pJoints) {
           printf("[IK Result] J1=%.3f  J2=%.3f  J3=%.3f  J4=%.3f  J5=%.3f  J6=%.3f\n",
                  pJoints->_fX, pJoints->_fY, pJoints->_fZ,
                  pJoints->_fRx, pJoints->_fRy, pJoints->_fRz);
       } else {
           printf("[IK Result] Target pose not reachable.\n");
       }

       return 0;
   }

In this example, a target Cartesian pose is defined in the **BASE frame**,  
and :ref:`ikin <ikin>` is used to compute the joint angles that achieve that pose.  
This allows the operator to test reachability or prepare motion commands offline  
without physically moving the robot arm.

**Tips**

- Use for **offline pose verification** or **alternative configuration testing**.  
- If no solution is found, check for singularities or unreachable workspace limits.  
- Compare with :ref:`fkin <manual_fkin>` to confirm pose consistency between forward and inverse models.  
- Record multiple IK solutions (different `iSolutionSpace`) to select the optimal path for constrained environments.
