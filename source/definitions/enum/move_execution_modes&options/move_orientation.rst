.. _enum_move_orientation:

MOVE_ORIENTATION
------------------------------------------
This is an enumeration type constant that defines the orientation maintenance method of the robot TCP during motion commands in the robot controller.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DR_MV_ORI_TEACH
     - Orientation follows the current teaching direction |br|
       (default orientation tracking mode).

   * - 1
     - DR_MV_ORI_FIXED
     - Orientation is fixed during motion. |br|
       The TCP direction does not change even when the path curves.

   * - 2
     - DR_MV_ORI_RADIAL
     - Orientation changes radially with respect to the target or reference point.

   * - 3
     - DR_MV_ORI_INTENT
     - Orientation changes according to the intended motion vector or path direction.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       DR_MV_ORI_TEACH,
       DR_MV_ORI_FIXED,
       DR_MV_ORI_RADIAL,
       DR_MV_ORI_INTENT,
   } MOVE_ORIENTATION;
