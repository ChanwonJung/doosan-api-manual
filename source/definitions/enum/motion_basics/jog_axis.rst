.. _enum_jog_axis:

JOG_AXIS
------------------------------------------
This is an enumeration type constant that refers to each axis that executes jog control in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - JOG_AXIS_JOINT_1
     - No. 1 joint or axis of robot

   * - 1
     - JOG_AXIS_JOINT_2
     - No. 2 joint or axis of robot

   * - 2
     - JOG_AXIS_JOINT_3
     - No. 3 joint or axis of robot

   * - 3
     - JOG_AXIS_JOINT_4
     - No. 4 joint or axis of robot

   * - 4
     - JOG_AXIS_JOINT_5
     - No. 5 joint or axis of robot

   * - 5
     - JOG_AXIS_JOINT_6
     - No. 6 joint or axis of robot

   * - 6
     - JOG_AXIS_TASK_X
     - X axis of robot TCP

   * - 7
     - JOG_AXIS_TASK_Y
     - Y axis of robot TCP

   * - 8
     - JOG_AXIS_TASK_Z
     - Z axis of robot TCP

   * - 9
     - JOG_AXIS_TASK_RX
     - RX axis of robot TCP

   * - 10
     - JOG_AXIS_TASK_RY
     - RY axis of robot TCP

   * - 11
     - JOG_AXIS_TASK_RZ
     - RZ axis of robot TCP

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       JOG_AXIS_JOINT_1 = 0,
       JOG_AXIS_JOINT_2,
       JOG_AXIS_JOINT_3, 
       JOG_AXIS_JOINT_4, 
       JOG_AXIS_JOINT_5, 
       JOG_AXIS_JOINT_6, 
       JOG_AXIS_TASK_X,
       JOG_AXIS_TASK_Y,
       JOG_AXIS_TASK_Z,
       JOG_AXIS_TASK_RX,
       JOG_AXIS_TASK_RY,
       JOG_AXIS_TASK_RZ,
   } JOG_AXIS;
