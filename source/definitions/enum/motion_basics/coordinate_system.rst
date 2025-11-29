.. _enum_coordinate_system:

COORDINATE_SYSTEM
------------------------------------------
This is an enumeration type constant that means the coordinate system in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - COORDINATE_SYSTEM_BASE
     - Base coordinate

   * - 1
     - COORDINATE_SYSTEM_TOOL
     - Tool coordinate

   * - 2
     - COORDINATE_SYSTEM_WORLD
     - World coordinate

   * - 101
     - COORDINATE_SYSTEM_USER_MIN
     - User coordinate (101~200)

   * - 200
     - COORDINATE_SYSTEM_USER_MAX
     - User coordinate (101~200)

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   // reference coordinate enumerated value
   typedef enum {
       COORDINATE_SYSTEM_BASE = 0,
       COORDINATE_SYSTEM_TOOL,
       COORDINATE_SYSTEM_WORLD,
       COORDINATE_SYSTEM_USER_MIN = 101,
       COORDINATE_SYSTEM_USER_MAX = 200,
   } COORDINATE_SYSTEM;
