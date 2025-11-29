.. _enum_blending_speed_type:

BLENDING_SPEED_TYPE
------------------------------------------
This is an enumeration type constant that refers to the blending velocity type for each waypoint when motion is controlled in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - BLENDING_SPEED_TYPE_DUPLICATE
     - Processing by duplicating the velocity of the previous |br|
       motion and that of the following motion

   * - 1
     - BLENDING_SPEED_TYPE_OVERRIDE
     - Processing by overriding the velocity of the previous |br|
       motion to that of the following motion

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       BLENDING_SPEED_TYPE_DUPLICATE = 0,
       BLENDING_SPEED_TYPE_OVERRIDE,
   } BLENDING_SPEED_TYPE;
