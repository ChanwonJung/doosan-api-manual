.. _enum_robot_space:

ROBOT_SPACE
------------------------------------------
This is an enumeration type constant that refers to the coordinate space controlling robot in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - ROBOT_SPACE_JOINT
     - Joint coordinate space control mode. |br| 
       Each axis of the robot is controlled individually by joint position.

   * - 1
     - ROBOT_SPACE_TASK
     - Task coordinate space control mode. |br|
       The robot motion is controlled in Cartesian (TCP) space.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       ROBOT_SPACE_JOINT,
       ROBOT_SPACE_TASK,
   } ROBOT_SPACE;