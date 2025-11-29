.. _enum_force_mode:

FORCE_MODE
------------------------------------------
This is an enumeration type constant that refers to the display method for the location to move to when performing for control is controlled in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - FORCE_MODE_ABSOLUTE
     - Absolute Coordinate

   * - 1
     - FORCE_MODE_RELATIVE
     - Relative Coordinate

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       FORCE_MODE_ABSOLUTE = 0,
       FORCE_MODE_RELATIVE,
   } FORCE_MODE;
