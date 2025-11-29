.. _enum_task_axis:

TASK_AXIS
------------------------------------------
This is an enumeration type constant that refers to each axis of robot with the standard of work space coordinate system in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - TASK_AXIS_X
     - X axis of robot TCP

   * - 1
     - TASK_AXIS_Y
     - Y axis of robot TCP

   * - 2
     - TASK_AXIS_Z
     - Z axis of robot TCP

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   // motion command axis type enumerated value
   typedef enum {
       TASK_AXIS_X = 0,
       TASK_AXIS_Y,
       TASK_AXIS_Z, 
   } TASK_AXIS;
