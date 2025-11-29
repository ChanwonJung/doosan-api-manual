.. _enum_log_group:

LOG_GROUP
------------------------------------------
This is an enumeration type constant that refers to the alarm group bell in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - LOG_GROUP_RESERVED
     - Internal reservation state

   * - 1
     - LOG_GROUP_SYSTEMFMK
     - Lower Level Controller (Framework)

   * - 2
     - LOG_GROUP_MOTIONLIB
     - Lower Level Controller (Algorithm)

   * - 3
     - LOG_GROUP_SMARTTP
     - Higher Level Controller (GUI)

   * - 4
     - LOG_GROUP_INVERTER
     - Robot Inverter Board

   * - 5
     - LOG_GROUP_SAFETYCONTROLLER
     - Safety Board (Safety Controller)

   * - 6
     - LOG_GROUP_LAST
     - Internal end marker for enumeration definition

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       LOG_GROUP_SYSTEMFMK = 1,
       LOG_GROUP_MOTIONLIB,
       LOG_GROUP_SMARTTP,
       LOG_GROUP_INVERTER,
       LOG_GROUP_SAFETYCONTROLLER,
       LOG_GROUP_LAST,
   } LOG_GROUP;
