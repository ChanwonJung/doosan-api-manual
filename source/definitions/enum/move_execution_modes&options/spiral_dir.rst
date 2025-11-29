.. _enum_spiral_dir:

SPIRAL_DIR
------------------------------------------
This is an enumeration type constant that defines the direction of spiral motion in the robot controller.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DR_SPIRAL_OUTWARD
     - Spiral motion progresses **outward** from the center point.

   * - 1
     - DR_SPIRAL_INWARD
     - Spiral motion progresses **inward** toward the center point.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       DR_SPIRAL_OUTWARD,
       DR_SPIRAL_INWARD,
   } SPIRAL_DIR;