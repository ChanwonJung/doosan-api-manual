.. _enum_path_mode:

PATH_MODE
------------------------------------------
This is an enumeration constant that means the path mode and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - PATH_MODE_DPOS
     - Cumulative

   * - 1
     - PATH_MODE_DVEL
     - Increment

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       PATH_MODE_DPOS = 0,
       PATH_MODE_DVEL
   } PATH_MODE;
