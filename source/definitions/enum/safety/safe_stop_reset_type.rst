.. _enum_safe_stop_reset_type:

SAFE_STOP_RESET_TYPE
------------------------------------------
This is an enumeration type constant that releases the operation state of the robot controller as STATE_SAFE_STOP and defines a series of motions afterward, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SAFE_STOP_RESET_TYPE_DEFAULT
     - Release of Simple State (Manual Mode)

   * - 0
     - SAFE_STOP_RESET_TYPE_PROGRAM_STOP
     - Program Termination (Automatic Mode)

   * - 1
     - SAFE_STOP_RESET_TYPE_PROGRAM_RESUME
     - Program Restart (Automatic Mode)

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SAFE_STOP_RESET_TYPE_DEFAULT = 0,
       SAFE_STOP_RESET_TYPE_PROGRAM_STOP = SAFE_STOP_RESET_TYPE_DEFAULT,
       SAFE_STOP_RESET_TYPE_PROGRAM_RESUME,
   } SAFE_STOP_RESET_TYPE;
