.. _struct_MEASURE_CONVEYOR_COORD_RESPONSE:

MEASURE_CONVEYOR_COORD_RESPONSE
===============================

This structure provides the **result of conveyor coordinate measurement**,  
including the encoder count-to-distance ratio and the calculated conveyor coordinate frame.  
It is typically returned after executing a conveyor calibration process.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iDistance2Count``
     - ``int``
     - -
     - Encoder counts per unit distance (count/mm)
   * - 4
     - ``_tPosCoord``
     - :ref:`POSITION <struct_POSITION>`
     - -
     - Calculated conveyor coordinate pose (X, Y, Z, Rx, Ry, Rz)

Total size: 28 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_CONVEYOR_COORD_RESPONSE
   {
       /* Encoder counts per distance (count/mm) */
       int _iDistance2Count;

       /* Conveyor coordinate position (X, Y, Z, Rx, Ry, Rz) */
       POSITION _tPosCoord;

   } MEASURE_CONVEYOR_COORD_RESPONSE, *LPMEASURE_CONVEYOR_COORD_RESPONSE;
