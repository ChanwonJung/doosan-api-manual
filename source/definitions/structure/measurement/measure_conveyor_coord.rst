.. _struct_MEASURE_CONVEYOR_COORD:

MEASURE_CONVEYOR_COORD
======================

This structure defines the **conveyor coordinate measurement** inputs,  
including a reference teach point (Q1), up to five measurement teach points (P1~P5),  
and the corresponding **encoder counts** captured at each point.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tPosTeachPointQ``
     - :ref:`POSITION <struct_POSITION>`
     - -
     - Reference teach point **Q1** (X, Y, Z, Rx, Ry, Rz)
   * - 24
     - ``_nTeachCount``
     - ``unsigned char``
     - 0~5
     - Number of used teach points (**P1~P5**)
   * - 28
     - ``_tPosTeachPointP``
     - :ref:`POSITION <struct_POSITION>` ``[5]``
     - -
     - Teach points **P1~P5** (pose array)
   * - 148
     - ``_EncoderCount``
     - ``unsigned int[5]``
     - -
     - Encoder counts captured at **P1~P5**

Total size: 168 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_CONVEYOR_COORD
   {
       /* Q1 */
       POSITION      _tPosTeachPointQ;

       /* Number of Teaching Point (P1~P5) */
       unsigned char _nTeachCount;

       /* P1~P5 */
       POSITION      _tPosTeachPointP[5];

       /* Encoder Count Values for P1~P5 */
       unsigned int  _EncoderCount[5];

   } MEASURE_CONVEYOR_COORD, *LPMEASURE_CONVEYOR_COORD;
