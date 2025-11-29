.. _enum_output_type:

OUTPUT_TYPE
------------------------------------------
It is an enumerated constant to indicate the output type of the digital output installed on the flange, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - OUTPUT_TYPE_PNP
     - PNP

   * - 1
     - OUTPUT_TYPE_NPN
     - NPN

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum{
       OUTPUT_TYPE_PNP = 0,
       OUTPUT_TYPE_NPN,
   } OUTPUT_TYPE;
