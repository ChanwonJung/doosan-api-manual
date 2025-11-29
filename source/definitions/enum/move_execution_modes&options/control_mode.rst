.. _enum_control_mode:

CONTROL_MODE
------------------------------------------
This is an enumeration constant that means the robot controller control mode, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 3
     - CONTROL_MODE_POSITION
     - Position Control Mode

   * - 4
     - CONTROL_MODE_TORQUE
     - Torque Control mode

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       CONTROL_MODE_POSITION = 3,
       CONTROL_MODE_TORQUE
   } CONTROL_MODE;
