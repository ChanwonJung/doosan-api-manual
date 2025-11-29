.. _enum_move_mode:

MOVE_MODE
------------------------------------------
This is an enumeration type constant that refers to the display method for the location to move to when motion is controlled in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MOVE_MODE_ABSOLUTE
     - Absolute Coordinate

   * - 1
     - MOVE_MODE_RELATIVE
     - Relative Coordinate

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MOVE_MODE_ABSOLUTE = 0,
       MOVE_MODE_RELATIVE,
   } MOVE_MODE;
