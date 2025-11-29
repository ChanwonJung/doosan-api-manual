.. _enum_robot_axis:

ROBOT_AXIS
------------------------------------------
This is an enumeration type constant that refers to each axis of the robot or all axes in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - ROBOT_AXIS_1
     - No. 1 axis of robot

   * - 1
     - ROBOT_AXIS_2
     - No. 2 axis of robot

   * - 2
     - ROBOT_AXIS_3
     - No. 3 axis of robot

   * - 3
     - ROBOT_AXIS_4
     - No. 4 axis of robot

   * - 4
     - ROBOT_AXIS_5
     - No. 5 axis of robot

   * - 5
     - ROBOT_AXIS_6
     - No. 6 axis of robot

   * - 6
     - ROBOT_AXIS_ALL
     - All axes of robot

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       ROBOT_AXIS_1 = 0,
       ROBOT_AXIS_2,
       ROBOT_AXIS_3,
       ROBOT_AXIS_4,
       ROBOT_AXIS_5,
       ROBOT_AXIS_6,
       ROBOT_AXIS_ALL
   } ROBOT_AXIS;
