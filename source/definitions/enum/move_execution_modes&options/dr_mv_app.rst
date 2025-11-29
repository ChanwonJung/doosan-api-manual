.. _enum_dr_mv_app:

DR_MV_APP
------------------------------------------
This is an enumeration type constant that specifies the application option used during robot motion execution.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DR_MV_APP_NONE
     - No specific application option is applied.

   * - 1
     - DR_MV_APP_WELD
     - Motion is executed with **welding application mode** enabled.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       DR_MV_APP_NONE,
       DR_MV_APP_WELD
   } DR_MV_APP;
