.. _enum_release_mode:

RELEASE_MODE
------------------------------------------
It is an enumerated constant for setting the subsequent operation at the time of a protective stop, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - RELEASE_MODE_STOP
     - Program Stop

   * - 1
     - RELEASE_MODE_RESUME
     - Program Resume

   * - 2
     - RELEASE_MODE_RELEASE
     - Release protective stop

   * - 3
     - RELEASE_MODE_RESET
     - Interlock Reset

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       RELEASE_MODE_STOP = 0,
       RELEASE_MODE_RESUME,
       RELEASE_MODE_RELEASE,
       RELEASE_MODE_RESET
   } RELEASE_MODE;
