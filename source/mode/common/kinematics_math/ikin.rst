.. _ikin:

ikin
------------------------------------------
This function receives the input data of joint angles (`fSourcePos`) or equivalent forms (`float[6]`)  
in the joint space and returns the TCP (objects in the task space) based on the ref coordinate (`eTargetRef`).

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 666)

.. code-block:: cpp

    LPROBOT_POSE ikin(
        float fSourcePos[NUM_TASK],
        unsigned char iSolutionSpace,
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _ikin(_rbtCtrl, fSourcePos, iSolutionSpace, eTargetRef);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fSourcePos
     - float[6]
     - -
     - Input joint angles (or equivalent task data) representing the robot's pose for six axes.
   * - iSolutionSpace
     - unsigned char
     - -
     - Solution space index (0–7). |br|
       Indicates which inverse kinematics configuration to use (e.g., elbow up/down, wrist flip, etc.).
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for the calculated TCP.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_POSE <struct_robot_pose>`
     - Calculated TCP pose (x, y, z, Rx, Ry, Rz) in the specified |br| 
       `eTargetRef` coordinate system.

**Example**

.. code-block:: cpp

   float x1[6] = { 370.9, 719.7, 651.5, 90, -180, 0 };
   LPROBOT_POSE res = drfl.ikin(x1, 2);

   float q1[6] = { 0 };
   for (int i = 0; i < 6; i++) {
       q1[i] = res->_fPosition[i];
   }

   drfl.movej(q1, 60, 30);

In this example, the function computes the **inverse kinematics** to determine  
the TCP pose of the robot corresponding to a given joint configuration.  
By selecting `iSolutionSpace`, the user can control which configuration (among multiple possible IK solutions)  
the robot should maintain when executing subsequent motion commands.
