.. _enum_monitoring_speed:

MONITORING_SPEED
------------------------------------------
This is an enumeration type constant that refers to the velocity mode of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 20 75

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SPEED_NORMAL_MODE
     - Normal Velocity Mode

   * - 1
     - SPEED_REDUCED_MODE
     - Deceleration Velocity Mode

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

    // speed mode enumerated value
    typedef enum {
        SPEED_NORMAL_MODE,
        SPEED_REDUCED_MODE
    } MONITORING_SPEED;
