.. _struct_SAFETY_OBJECT_POLYPRISM:

SAFETY_OBJECT_POLYPRISM
=======================

This structure defines a **polyprism-shaped safety object**,  
which is a 3D extrusion of a 2D polygon along the Z-axis. |br|
It can represent complex safety volumes such as polygonal fences or tool work envelopes.  
The shape is defined by multiple 2D vertices and vertical Z-axis limits.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iPointCount``
     - ``unsigned char``
     - 3~10
     - Number of polygon vertices (minimum 3, maximum 10)
   * - 1
     - ``_tPoint[10]``
     - :ref:`POINT_2D <struct_POINT_2D>` [10]
     - -
     - 2D coordinates of polygon vertices on the XY plane
   * - 81
     - ``_fZLoLimit``
     - ``float``
     - -
     - Lower Z-axis limit (bottom face)
   * - 85
     - ``_fZUpLimit``
     - ``float``
     - -
     - Upper Z-axis limit (top face)

Total size: 89 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_OBJECT_POLYPRISM
   {
       /* Number of polygon vertices (3–10) */
       unsigned char _iPointCount;
       /* 2D vertex coordinates */
       POINT_2D _tPoint[10];
       /* Lower Z limit [mm] */
       float _fZLoLimit;
       /* Upper Z limit [mm] */
       float _fZUpLimit;
   } SAFETY_OBJECT_POLYPRISM, *LPSAFETY_OBJECT_POLYPRISM;
