.. _enum_cog_reference:

COG_REFERENCE
------------------------------------------
It is an enumerated constant to indicate the coordinate system based on the position of the center of gravity of the flange, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - COG_REFERENCE_TCP
     - TCP

   * - 1
     - COG_REFERENCE_FLANGE
     - Flange

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum{
       COG_REFERENCE_TCP = 0,
       COG_REFERENCE_FLANGE,
   } COG_REFERENCE;
