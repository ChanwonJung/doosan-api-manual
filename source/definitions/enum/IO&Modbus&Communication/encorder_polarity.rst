.. _enum_encorder_polarity:

ENCORDER_POLARITY
------------------------------------------
This enumeration type constant defines the signal polarity configuration of the encorder channels used in the robot system.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - ENCORDER_POLARITY_A
     - Encorder channel **A** polarity setting.

   * - 1
     - ENCORDER_POLARITY_B
     - Encorder channel **B** polarity setting.

   * - 2
     - ENCORDER_POLARITY_Z
     - Encorder channel **Z (index pulse)** polarity setting.

   * - 3
     - ENCORDER_POLARITY_S
     - Encorder **S (signal or synchronization)** channel polarity setting.

   * - 4
     - ENCORDER_POLARITY_LAST
     - Internal end marker of the ENCORDER_POLARITY enumeration. |br|
       It does **not represent a physical signal**, but defines the total number of valid polarity constants.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       ENCORDER_POLARITY_A,
       ENCORDER_POLARITY_B,
       ENCORDER_POLARITY_Z,
       ENCORDER_POLARITY_S,
       ENCORDER_POLARITY_LAST
   } ENCORDER_POLARITY;
