.. _enum_byte_size:

BYTE_SIZE
------------------------------------------
This is an enumerated constant about the size of data to be transmitted during serial communication, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - BYTE_SIZE_FIVEBITES
     - 5 bits

   * - 1
     - BYTE_SIZE_SIXBITS
     - 6 bits

   * - 2
     - BYTE_SIZE_SEVENBITS
     - 7 bits

   * - 3
     - BYTE_SIZE_EIGHTBITS
     - 8 bits

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       BYTE_SIZE_FIVEBITES = 5,
       BYTE_SIZE_SIXBITS,
       BYTE_SIZE_SEVENBITS,
       BYTE_SIZE_EIGHTBITS
   } BYTE_SIZE;
