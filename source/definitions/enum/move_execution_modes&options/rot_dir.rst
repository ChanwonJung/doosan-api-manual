.. _enum_rot_dir:

ROT_DIR
------------------------------------------
This is an enumeration type constant that defines the rotational direction used for motion or tool orientation control.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DR_ROT_FORWARD
     - Rotates in the **forward (clockwise)** direction.

   * - 1
     - DR_ROT_REVERSE
     - Rotates in the **reverse (counterclockwise)** direction.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       DR_ROT_FORWARD,
       DR_ROT_REVERSE,
   } ROT_DIR;
