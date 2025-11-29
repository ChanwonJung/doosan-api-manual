.. _enum_log_level:

LOG_LEVEL
------------------------------------------
This is an enumeration type constant that refers to the alarm level in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - LOG_LEVEL_RESERVED
     - Internal reservation state

   * - 1
     - LOG_LEVEL_SYSINFO
     - Informative messages about simple functions and operational errors

   * - 2
     - LOG_LEVEL_SYSWARN
     - Robot stop state caused by simple function and operational error

   * - 3
     - LOG_LEVEL_SYSERROR
     - Robot stop state caused by safety issue or device error

   * - 4
     - LOG_LEVEL_LAST
     - Internal end marker for enumeration definition

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {    
       LOG_LEVEL_SYSINFO = 1,
       LOG_LEVEL_SYSWARN,
       LOG_LEVEL_SYSERROR,
       LOG_LEVEL_LAST
   } LOG_LEVEL;
