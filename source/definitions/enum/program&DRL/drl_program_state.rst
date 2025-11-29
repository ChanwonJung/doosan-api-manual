.. _enum_drl_program_state:

DRL_PROGRAM_STATE
------------------------------------------
This is an enumeration type constant that refers to the execution state of program in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DRL_PROGRAM_STATE_PLAY
     - Program Execution State

   * - 1
     - DRL_PROGRAM_STATE_STOP
     - Program Stop State

   * - 2
     - DRL_PROGRAM_STATE_HOLD
     - Program Hold State

   * - 3
     - DRL_PROGRAM_STATE_LAST
     - Internal end marker of the DRL_PROGRAM_STATE enumeration. |br|  
       Used to define the total number of valid program states.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       DRL_PROGRAM_STATE_PLAY,
       DRL_PROGRAM_STATE_STOP,
       DRL_PROGRAM_STATE_HOLD,
       DRL_PROGRAM_STATE_LAST
   } DRL_PROGRAM_STATE;
