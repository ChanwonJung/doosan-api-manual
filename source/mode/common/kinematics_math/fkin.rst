.. _fkin:

fkin (forward kinematics)
------------------------------------------
This function computes the **TCP pose (Task Space Position and Orientation)**  
from the given **joint angles** in the robot's kinematic chain.  
It is the inverse operation of :ref:`ikin <ikin>`, converting joint values to Cartesian coordinates.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 670)

.. code-block:: cpp

    LPROBOT_POSE fkin(
        float fSourcePos[NUM_JOINT],
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _fkin(_rbtCtrl, fSourcePos, eTargetRef);
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
     - Joint positions for each axis (in degrees or radians, depending on system setting). |br|
       Represents the current robot configuration in joint space.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for TCP output.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_POSE <struct_ROBOT_POSE>`
     - Structure containing the resulting **TCP position** and **orientation** (x, y, z, Rx, Ry, Rz).
     
**Example**

.. code-block:: cpp

   float q1[6] = { 0.f, 90.f, 0.f, 90.f, 90.f, 0.f };
   drfl.movej(q1, 60, 30);  // Move robot to initial joint pose

   float q2[6] = { 30.f, 0.f, 0.f, 0.f, 90.f, 0.f };
   LPROBOT_POSE res = drfl.fkin(q2, COORDINATE_SYSTEM_WORLD);

   float vel[2] = { 100, 100 };
   float acc[2] = { 200, 200 };

   float tcp[6] = { 0 };
   for (int i = 0; i < 6; ++i)
       tcp[i] = res->_fPosition[i];

   drfl.movel(tcp, vel[0], acc[0]);

This example calculates the **forward kinematics** for joint angles `q2`  
in the **WORLD** coordinate system, producing a TCP pose `tcp`.  
The resulting pose is then used as a motion target for `movel()`,  
demonstrating how FK results can be directly reused for Cartesian control.
