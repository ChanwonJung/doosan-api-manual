.. _struct_MEASURE_TCP:

MEASURE_TCP
============

This structure defines the configuration data used for **Tool Center Point (TCP) measurement**.  
It specifies the reference coordinate system and multiple target poses used during the  
auto-measurement or calibration process.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetRef``
     - ``unsigned char``
     - 0 or 1
     - Reference frame selection |br|
       (0: Base, 1: Tool)
   * - 1
     - ``_fTargetPos``
     - ``float[4][6]``
     - -
     - Target reference positions (X, Y, Z, Rx, Ry, Rz) |br|
       for 4 measurement configurations

Total size: 97 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_TCP
   {
       /* Reference frame (0: base, 1: tool) */
       unsigned char _iTargetRef;

       /* Reference target positions [4][6] */
       float _fTargetPos[4][NUMBER_OF_JOINT];

   } MEASURE_TCP, *LPMEASURE_TCP;
