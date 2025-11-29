.. _struct_CALIBRATION_PARAM_DATA:

CALIBRATION_PARAM_DATA
======================

This structure defines **sensor calibration coefficients**  
used to convert raw sensor data into calibrated physical values  
using a linear or polynomial calibration model.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_Ax``
     - ``float``
     - -
     - Calibration coefficient A
   * - 4
     - ``_Bx``
     - ``float``
     - -
     - Calibration coefficient B
   * - 8
     - ``_Cx``
     - ``float``
     - -
     - Calibration coefficient C
   * - 12
     - ``_Dx``
     - ``float``
     - -
     - Calibration coefficient D

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CALIBRATION_PARAM_DATA
   {
       /* Calibration polynomial coefficients */
       float _Ax;   /* A term */
       float _Bx;   /* B term */
       float _Cx;   /* C term */
       float _Dx;   /* D term */

   } CALIBRATION_PARAM_DATA, *LPCALIBRATION_PARAM_DATA;