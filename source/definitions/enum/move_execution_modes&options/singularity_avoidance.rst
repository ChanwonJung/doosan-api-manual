.. _enum_singularity_avoidance:

SINGULARITY_AVOIDANCE
------------------------------------------
This is an enumeration constant that means the method of avoiding singularity, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SINGULARITY_AVOIDANCE_AVOID
     - Auto Avoidance Mode

   * - 1
     - SINGULARITY_AVOIDANCE_STOP
     - reduce / warning / task stop

   * - 2
     - SINGULARITY_AVOIDANCE_VEL
     - Variable Speed

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SINGULARITY_AVOIDANCE_AVOID = 0,
       SINGULARITY_AVOIDANCE_STOP,
       SINGULARITY_AVOIDANCE_VEL,
   } SINGULARITY_AVOIDANCE;
