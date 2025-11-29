.. _struct_ROBOT_MONITORING_SENSOR:

ROBOT_MONITORING_SENSOR
=======================

This structure provides real-time monitoring data from both external and internal sensors,  
including **force/torque**, **current**, and **acceleration** sensor readings.

.. list-table::
   :widths: 10 28 15 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fActualFTS``
     - ``float[6]``
     - -
     - Force/Torque sensor values (Fx, Fy, Fz, Tx, Ty, Tz)
   * - 24
     - ``_fActualCS``
     - ``float[6]``
     - -
     - Current sensor values for each joint.
   * - 48
     - ``_fActualACS``
     - ``float[3]``
     - -
     - Acceleration sensor values (X, Y, Z).

Total size: 60 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_SENSOR
   {
       float _fActualFTS[NUMBER_OF_JOINT];  /* Force Torque Sensor Value */
       float _fActualCS[NUMBER_OF_JOINT];   /* Current Sensor Value */
       float _fActualACS[3];                /* Accelerate Sensor Value */
   } ROBOT_MONITORING_SENSOR, *LPROBOT_MONITORING_SENSOR;

.. note::
   - ``_fActualFTS`` corresponds to the 6-axis force/torque sensor.
   - ``_fActualCS`` provides per-joint current readings.
   - ``_fActualACS`` represents the acceleration values (X, Y, Z).
