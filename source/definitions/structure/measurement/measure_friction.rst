.. _struct_MEASURE_FRICTION:

MEASURE_FRICTION
================

This structure defines the configuration parameters for **joint friction measurement**.  
It specifies the measurement type, selected joints, start positions, and motion ranges.  
Used in friction identification or dynamic calibration processes of each robot joint.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iType``
     - ``unsigned char``
     - 0~N
     - Friction measurement type (e.g., static, dynamic)
   * - 1
     - ``_iSelect``
     - ``unsigned char[6]``
     - 0 or 1
     - **Joint selection flag** |br|
       0: excluded |br|
       1: included in measurement
   * - 7
     - ``_fStart``
     - ``float[6]``
     - [deg]
     - Starting joint positions
   * - 31
     - ``_fRange``
     - ``float[6]``
     - [deg]
     - Motion range of each joint

Total size: 55 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_FRICTION
   {
       /* Measure type (0: static, 1: dynamic, etc.) */
       unsigned char _iType;

       /* Selected joints (1: enable, 0: disable) */
       unsigned char _iSelect[NUMBER_OF_JOINT];

       /* Start position per joint [deg] */
       float _fStart[NUMBER_OF_JOINT];

       /* Motion range per joint [deg] */
       float _fRange[NUMBER_OF_JOINT];

   } MEASURE_FRICTION, *LPMEASURE_FRICTION;
