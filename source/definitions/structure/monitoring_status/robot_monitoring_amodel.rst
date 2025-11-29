.. _struct_ROBOT_MONITORING_AMODEL:

ROBOT_MONITORING_AMODEL
=======================

This structure provides additional monitoring data specific to **A-Model robots**,  
including sensor readings and singularity indicators.

.. list-table::
   :widths: 10 28 15 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tSensor``
     - :ref:`ROBOT_MONITORING_SENSOR <struct_ROBOT_MONITORING_SENSOR>`
     - -
     - Sensor monitoring data (Force/Torque, Current, Acceleration)
   * - 60
     - ``_fSingularity``
     - ``float``
     - -
     - Singularity index (minimum singular value)

Total size: 64 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_MONITORING_AMODEL
   {
       /* sensor */
       ROBOT_MONITORING_SENSOR     _tSensor;
       /* singularity */
       float                       _fSingularity;
   } ROBOT_MONITORING_AMODEL, *LPROBOT_MONITORING_AMODEL;

   typedef ROBOT_MONITORING_AMODEL
      MONITORING_AMODEL, *LPMONITORING_AMODEL;