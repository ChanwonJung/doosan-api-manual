.. _enum_move_home:

MOVE_HOME
------------------------------------------
This is an enumeration constant that is related to the coordinate system to be referenced when homing. It is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MOVE_HOME_MECHANIC
     - Mechanical home position [0, 0, 0, 0, 0, 0]

   * - 1
     - MOVE_HOME_USER
     - User home position (custom)

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MOVE_HOME_MECHANIC,
       MOVE_HOME_USER
   } MOVE_HOME;
