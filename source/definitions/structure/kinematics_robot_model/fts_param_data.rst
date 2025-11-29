.. _struct_FTS_PARAM_DATA:

FTS_PARAM_DATA
===============

This structure defines the **Force Torque Sensor (FTS)** calibration parameters,  
representing the offset values for each joint’s torque sensor channel.  
It is used for sensor bias compensation during robot calibration.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fOffset``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Offset values for each joint’s force/torque sensor reading

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _FTS_PARAM_DATA
   {
       /* Offset for each joint */
       float _fOffset[NUMBER_OF_JOINT];

   } FTS_PARAM_DATA, *LPFTS_PARAM_DATA;

   /* Alias for FTS calibration result */
   typedef FTS_PARAM_DATA
       CALIBRATE_FTS_RESPONSE, *LPCALIBRATE_FTS_RESPONSE;