.. _struct_VIRTUAL_FENCE_RESPONSE:

VIRTUAL_FENCE_RESPONSE
======================

This structure provides the **result data** from the virtual fence evaluation process,  
indicating whether the robot's position is within or outside each defined virtual fence boundary.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iCubeResult``
     - ``unsigned char[6]``
     - 0 or 1
     - Result flags for up to **6 cube-shaped fences** |br|
       0: Inside boundary, 1: Outside boundary
   * - 6
     - ``_iPolyResult``
     - ``unsigned char[6]``
     - 0 or 1
     - Result flags for up to **6 polygon-shaped fences** |br|
       0: Inside boundary, 1: Outside boundary
   * - 12
     - ``_iCylinderResult``
     - ``unsigned char``
     - 0 or 1
     - Result flag for **cylinder-shaped fence** |br|
       0: Inside, 1: Outside

Total size: 13 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _VIRTUAL_FENCE_RESPONSE
   {
       unsigned char _iCubeResult[6];      /* cube fence result flags (0: inside, 1: outside) */
       unsigned char _iPolyResult[6];      /* polygon fence result flags (0: inside, 1: outside) */
       unsigned char _iCylinderResult;     /* cylinder fence result flag (0: inside, 1: outside) */
   } VIRTUAL_FENCE_RESPONSE, *LPVIRTUAL_FENCE_RESPONSE;
