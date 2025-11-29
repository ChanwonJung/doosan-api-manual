.. _enum_add_up:

ADD_UP
------------------------------------------
It is an enumerated constant to indicate the state of the workpiece of the flange, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - ADD_UP_REPLACE
     - Replace workpiece

   * - 1
     - ADD_UP_ADD
     - Add workpiece

   * - 2
     - ADD_UP_REMOVE
     - Remove workpiece

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum{
       ADD_UP_REPLACE = 0,
       ADD_UP_ADD,
       ADD_UP_REMOVE,
   } ADD_UP;
