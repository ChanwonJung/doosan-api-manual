.. _struct_GRAVITY_PARAM_DATA:

GRAVITY_PARAM_DATA
==================

This structure defines the **gravity calibration parameters** used for  
compensating gravitational effects in the robot’s dynamic control model.  
It includes both mechanical and calibration coefficients.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tClParam``
     - :ref:`COUNTER_BALANCE_PARAM_DATA <struct_COUNTER_BALANCE_PARAM_DATA>`
     - -
     - Counterbalance system mechanical parameters
   * - 16
     - ``_tCrParam``
     - :ref:`CALIBRATION_PARAM_DATA <struct_CALIBRATION_PARAM_DATA>`
     - -
     - Calibration coefficients for gravity compensation model

Total size: 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _GRAVITY_PARAM_DATA
   {
       /* Counterbalance mechanical parameters */
       COUNTER_BALANCE_PARAM_DATA _tClParam;

       /* Calibration coefficients */
       CALIBRATION_PARAM_DATA _tCrParam;

   } GRAVITY_PARAM_DATA, *LPGRAVITY_PARAM_DATA;

   /* Alias for gravity calibration response */
   typedef GRAVITY_PARAM_DATA
       CALIBRATE_GRAVITY_RESPONSE, *LPCALIBRATE_GRAVITY_RESPONSE;