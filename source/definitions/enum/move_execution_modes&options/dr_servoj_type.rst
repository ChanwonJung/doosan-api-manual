.. _enum_dr_servoj_type:

DR_SERVOJ_TYPE
------------------------------------------
This is an enumeration type constant that defines the execution type of the ServoJ motion command in the robot controller.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DR_SERVO_OVERRIDE
     - ServoJ motion executes immediately, overriding any previously queued motion.

   * - 1
     - DR_SERVO_QUEUE
     - ServoJ motion is queued and executed sequentially after the current motion.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       DR_SERVO_OVERRIDE = 0,
       DR_SERVO_QUEUE = 1,
   } DR_SERVOJ_TYPE;
