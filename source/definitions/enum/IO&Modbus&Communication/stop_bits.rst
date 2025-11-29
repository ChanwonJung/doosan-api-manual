.. _enum_stop_bits:

STOP_BITS
------------------------------------------
This is an enumerated constant about Stopbits indicating the end of a frame during serial communication, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - STOPBITS_ONE
     - 1 bit

   * - 1
     - STOPBITS_TWO
     - 2 bits

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       STOPBITS_ONE = 1,
       STOPBITS_TWO
   } STOP_BITS;
