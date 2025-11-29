.. _enum_program_stop_cause:

PROGRAM_STOP_CAUSE
------------------------------------------
This is an enumeration type constant that refers to the termination reason when the program is terminated in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - PROGRAM_STOP_CAUSE_NORMAL
     - Normal Program Termination

   * - 1
     - PROGRAM_STOP_CAUSE_FORCE
     - Forced Program Termination

   * - 2
     - PROGRAM_STOP_CAUSE_ERROR
     - Program Termination Caused by Inside/Outside Errors

   * - 3
     - PROGRAM_STOP_CAUSE_LAST
     - Internal end marker of the PROGRAM_STOP_CAUSE enumeration. |br|
       Used to define the total number of valid stop cause states.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       PROGRAM_STOP_CAUSE_NORMAL,
       PROGRAM_STOP_CAUSE_FORCE,        
       PROGRAM_STOP_CAUSE_ERROR,
       PROGRAM_STOP_CAUSE_LAST
   } PROGRAM_STOP_CAUSE;
