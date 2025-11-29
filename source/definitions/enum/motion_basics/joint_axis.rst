.. _enum_joint_axis:

JOINT_AXIS
------------------------------------------
This is an enumeration type constant that refers to each axis of robot with the standard of joint space coordinate system in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - JOINT_AXIS_1
     - No. 1 joint or axis of robot

   * - 1
     - JOINT_AXIS_2
     - No. 2 joint or axis of robot

   * - 2
     - JOINT_AXIS_3
     - No. 3 joint or axis of robot

   * - 3
     - JOINT_AXIS_4
     - No. 4 joint or axis of robot

   * - 4
     - JOINT_AXIS_5
     - No. 5 joint or axis of robot

   * - 5
     - JOINT_AXIS_6
     - No. 6 joint or axis of robot

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       JOINT_AXIS_1 = 0,
       JOINT_AXIS_2,
       JOINT_AXIS_3, 
       JOINT_AXIS_4, 
       JOINT_AXIS_5, 
       JOINT_AXIS_6, 
   } JOINT_AXIS;
