.. _enum_moveb_blending_type:

MOVEB_BLENDING_TYPE
------------------------------------------
This is an enumeration type constant that refers to the blending motion type for each waypoint when moveb motion is controlled in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MOVEB_BLENDING_TYPE_LINE
     - Line

   * - 1
     - MOVEB_BLENDING_TYPE_CIRLCE
     - Circle

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MOVEB_BLENDING_TYPE_LINE,
       MOVEB_BLENDING_TYPE_CIRLCE,
   } MOVEB_BLENDING_TYPE;
