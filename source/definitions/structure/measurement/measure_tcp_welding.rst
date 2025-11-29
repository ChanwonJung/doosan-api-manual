.. _struct_MEASURE_TCP_WELDING:

MEASURE_TCP_WELDING
===================

This structure contains the information required for **welding TCP (Tool Center Point) measurement**.  
It defines the measurement mode, stick-out value, and the reference position of each joint.  
Typically used during **welding tool calibration** or **TCP offset identification**.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iMode``
     - ``unsigned char``
     - 0 or 1
     - Measurement mode |br|
       (0: No measurement, 1: Measurement)
   * - 1
     - ``_fStickout``
     - ``float``
     - -
     - Stick-out value (mm)
   * - 5
     - ``_fTargetPos``
     - ``float[9][6]``
     - -
     - Target reference positions for 9 joints |br|
       Each row represents a 3D position (X, Y, Z)

Total size: 221 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_TCP_WELDING
   {
       /* Orientation measurement mode (0: no measurement, 1: measurement) */
       unsigned char _iMode;

       /* Stick-out value in mm */
       float _fStickout;

       /* Reference position for each joint [9][6] */
       float _fTargetPos[9][NUMBER_OF_JOINT];

   } MEASURE_TCP_WELDING, *LPMEASURE_TCP_WELDING;
