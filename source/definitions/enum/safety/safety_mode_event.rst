.. _enum_safety_mode_event:

SAFETY_MODE_EVENT
------------------------------------------
It is an enumerated constant to indicate the current event state of the safety board, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SAFETY_MODE_EVENT_ENTER
     - Enter event (safety mode entry)

   * - 1
     - SAFETY_MODE_EVENT_MOVE
     - Move event (safety mode active)

   * - 2
     - SAFETY_MODE_EVENT_STOP
     - Stop event (safety mode stop)

   * - 3
     - SAFETY_MODE_EVENT_LAST
     - Reserved for the last safety mode event index

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SAFETY_MODE_EVENT_ENTER,
       SAFETY_MODE_EVENT_MOVE,
       SAFETY_MODE_EVENT_STOP,
       SAFETY_MODE_EVENT_LAST,
   } SAFETY_MODE_EVENT;
