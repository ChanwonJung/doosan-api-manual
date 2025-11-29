.. _enum_stop_type:

STOP_TYPE
------------------------------------------
This is an enumeration type constant that refers to the motion pause type that can stop the motion control when motion is controlled in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - STOP_TYPE_QUICK_STO
     - Internal reservation used

   * - 1
     - STOP_TYPE_QUICK
     - Quick Stop (maintenance of motion trajectory)

   * - 2
     - STOP_TYPE_SLOW
     - Slow Stop (maintenance of motion trajectory)

   * - 3
     - STOP_TYPE_HOLD
     - Emergency Stop

   * - 3
     - STOP_TYPE_EMERGENCY
     - Emergency Stop (alias of STOP_TYPE_HOLD)

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       STOP_TYPE_QUICK_STO = 0,
       STOP_TYPE_QUICK,
       STOP_TYPE_SLOW,
       STOP_TYPE_HOLD,
       STOP_TYPE_EMERGENCY = STOP_TYPE_HOLD,
   } STOP_TYPE;
