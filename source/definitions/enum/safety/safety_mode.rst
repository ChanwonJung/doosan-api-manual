.. _enum_safety_mode:

SAFETY_MODE
------------------------------------------
It is an enumerated constant for setting the subsequent operation at the time of a protective stop, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SAFETY_MODE_MANUAL
     - Manual mode

   * - 1
     - SAFETY_MODE_AUTONOMOUS
     - Autonomous mode

   * - 2
     - SAFETY_MODE_RECOVERY
     - Recovery mode

   * - 3
     - SAFETY_MODE_BACKDRIVE
     - Backdrive mode

   * - 4
     - SAFETY_MODE_MEASURE
     - Measure mode

   * - 5
     - SAFETY_MODE_INITIALIZE
     - Initializing mode

   * - 6
     - SAFETY_MODE_LAST
     - Reserved for the last safety mode index

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SAFETY_MODE_MANUAL,
       SAFETY_MODE_AUTONOMOUS,
       SAFETY_MODE_RECOVERY,
       SAFETY_MODE_BACKDRIVE,
       SAFETY_MODE_MEASURE,
       SAFETY_MODE_INITIALIZE,
       SAFETY_MODE_LAST,
   } SAFETY_MODE;
