.. _enum_parity_check:

PARITY_CHECK
------------------------------------------
This is an enumerated constant for parity check during serial communication, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - PARITY_CHECK_NONE
     - None check

   * - 1
     - PARITY_CHECK_EVEN
     - Even check

   * - 2
     - PARITY_CHECK_ODD
     - Odd check

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       PARITY_CHECK_NONE = 0,
       PARITY_CHECK_EVEN,
       PARITY_CHECK_ODD
   } PARITY_CHECK;
