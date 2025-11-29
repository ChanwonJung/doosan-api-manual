.. _enum_force_axis:

FORCE_AXIS
------------------------------------------
This is an enumeration constant that means the definition criteria for the coordinate reference criteria, when performing force control in the robot controller and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - FORCE_AXIS_X
     - x axis

   * - 1
     - FORCE_AXIS_Y
     - y axis

   * - 2
     - FORCE_AXIS_Z
     - z axis

   * - 10
     - FORCE_AXIS_A
     - x axis rotation

   * - 11
     - FORCE_AXIS_B
     - y axis rotation

   * - 12
     - FORCE_AXIS_C
     - z axis rotation

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       FORCE_AXIS_X = 0,
       FORCE_AXIS_Y,
       FORCE_AXIS_Z, 
       FORCE_AXIS_A = 10,
       FORCE_AXIS_B,
       FORCE_AXIS_C,
   } FORCE_AXIS;
