.. _struct_SAFETY_OBJECT_CUBE:

SAFETY_OBJECT_CUBE
==================

This structure defines a **cuboid safety object**,  
representing an axis-aligned box defined by two opposite 3D points.  
It is typically used to describe rectangular regions or simple bounding boxes  
within safety zones or tool configurations.

.. list-table::
   :widths: 10 28 22 8 45
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tTargetPos[2]``
     - :ref:`POINT_3D <struct_POINT_3D>` ``[2]``
     - -
     - **Opposite vertices of the cuboid** |br|
       ``_tTargetPos[0]``: Lower vertex  |br|
       ``_tTargetPos[1]``: Upper vertex

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_OBJECT_CUBE
   {
       /* Cube vertices: low(0), high(1) */
       POINT_3D _tTargetPos[2];
   } SAFETY_OBJECT_CUBE, *LPSAFETY_OBJECT_CUBE;
