.. _enum_robot_system:

ROBOT_SYSTEM
------------------------------------------
This is an enumeration type constant that refers to the operation system of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 20 75

   * - Rank
     - Constant Name
     - Description

   * - 0
     - ROBOT_SYSTEM_REAL
     - Actual Robot System

   * - 1
     - ROBOT_SYSTEM_VIRTUAL
     - Virtual Robot System

   * - 2
     - ROBOT_SYSTEM_LAST
     - Internal end marker of the ROBOT_SYSTEM enumeration. |br|
       It does **not represent a system mode**, but defines |br|
       the total number of valid constants within this enumeration. |br|  
       Used internally for boundary checking and array size definitions.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   // robot system enumerated value
   typedef enum {
       ROBOT_SYSTEM_REAL,
       ROBOT_SYSTEM_VIRTUAL,
       ROBOT_SYSTEM_LAST
   } ROBOT_SYSTEM;
