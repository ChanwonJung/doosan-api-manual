.. _enum_spline_velocity_option:

SPLINE_VELOCITY_OPTION
------------------------------------------
This is an enumeration type constant that refers to velocity control option of each waypoint when spline motion is controlled in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SPLINE_VELOCITY_OPTION_DEFAULT
     - Variable velocity motion

   * - 1
     - SPLINE_VELOCITY_OPTION_CONST
     - Constant velocity motion

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SPLINE_VELOCITY_OPTION_DEFAULT,
       SPLINE_VELOCITY_OPTION_CONST,
   } SPLINE_VELOCITY_OPTION;
