.. _struct_MEASURE_FRICTION_RESPONSE:

MEASURE_FRICTION_RESPONSE
=========================

This structure represents the **result data of joint friction measurement**,  
including the measurement status, error magnitude, friction characteristics in both motion directions,  
and joint temperature at the time of testing.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iResult``
     - ``unsigned char[6]``
     - 0 or 1
     - Measurement result per joint  
       (0: Fail, 1: Success)
   * - 6
     - ``_fError``
     - ``float[6]``
     - [N/m]
     - Measurement error for each joint
   * - 30
     - ``_fPositive``
     - ``float[4][6]``
     - [N·m]
     - Friction torque measured during **positive joint motion**
   * - 126
     - ``_fNegative``
     - ``float[4][6]``
     - [N·m]
     - Friction torque measured during **negative joint motion**
   * - 222
     - ``_fTemperature``
     - ``float[6]``
     - [°C]
     - Joint temperature at measurement time

Total size: 246 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_FRICTION_RESPONSE
   {
       /* Measurement result per joint (0: fail, 1: success) */
       unsigned char _iResult[NUMBER_OF_JOINT];

       /* Measurement error (N/m) */
       float _fError[NUMBER_OF_JOINT];

       /* Positive direction friction torque (4 samples per joint) */
       float _fPositive[4][NUMBER_OF_JOINT];

       /* Negative direction friction torque (4 samples per joint) */
       float _fNegative[4][NUMBER_OF_JOINT];

       /* Joint temperature (°C) */
       float _fTemperature[NUMBER_OF_JOINT];

   } MEASURE_FRICTION_RESPONSE, *LPMEASURE_FRICTION_RESPONSE;
