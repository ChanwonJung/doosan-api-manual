.. _enum_move_reference:

MOVE_REFERENCE
------------------------------------------
This is an enumeration type constant that refers to the definition standard for the location to move to when motion is controlled with the work space as the standard in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MOVE_REFERENCE_BASE
     - Robot base standard

   * - 1
     - MOVE_REFERENCE_TOOL
     - Robot TCP standard

   * - 2
     - MOVE_REFERENCE_WORLD
     - Robot world coordinate

   * - 101
     - MOVE_REFERENCE_USER_MIN
     - User custom coordinate min (101~200)

   * - 200
     - MOVE_REFERENCE_USER_MAX
     - User custom coordinate max (101~200)

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MOVE_REFERENCE_BASE = COORDINATE_SYSTEM_BASE,
       MOVE_REFERENCE_TOOL = COORDINATE_SYSTEM_TOOL,
       MOVE_REFERENCE_WORLD = COORDINATE_SYSTEM_WORLD,
       MOVE_REFERENCE_USER_MIN = COORDINATE_SYSTEM_USER_MIN,
       MOVE_REFERENCE_USER_MAX = COORDINATE_SYSTEM_USER_MAX,
   } MOVE_REFERENCE;
