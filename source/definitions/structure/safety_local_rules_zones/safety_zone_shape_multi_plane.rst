.. _struct_SAFETY_ZONE_SHAPE_MULTI_PLANE:

SAFETY_ZONE_SHAPE_MULTI_PLANE
=============================

This structure defines a **multi-plane safety zone**,  
composed of up to six planar boundaries that collectively form a custom-shaped 3D restricted region.  
It is primarily used to create complex convex boundaries with configurable Z-axis limits.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iValidPlane``
     - ``unsigned char[6]``
     - 0 or 1
     - Plane validity flag array |br|
       (0: inactive, 1: valid plane)
   * - 6
     - ``_tPlane``
     - :ref:`LINE_2D <struct_LINE_2D>` [6]
     - -
     - Line equation defining each plane in 2D (used to describe planar boundaries)
   * - 102
     - ``_fZLoLimit``
     - ``float``
     - -
     - Lower Z limit of the multi-plane region
   * - 106
     - ``_fZUpLimit``
     - ``float``
     - -
     - Upper Z limit of the multi-plane region
   * - 110
     - ``_tSpacePoint``
     - :ref:`POINT_2D <struct_POINT_2D>`
     - -
     - Reference point used to define spatial relation (inside/outside) of the zone

Total size: 118 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE_MULTI_PLANE
   {
       /* plane validity flag (1: valid, 0: invalid) */
       unsigned char _iValidPlane[6];    
       /* plane definitions (line representation) */
       LINE_2D _tPlane[6];
       /* height limits */
       float _fZLoLimit;
       float _fZUpLimit;
       /* reference point for inside/outside space determination */
       POINT_2D _tSpacePoint;
   } SAFETY_ZONE_SHAPE_MULTI_PLANE, *LPSAFETY_ZONE_SHAPE_MULTI_PLANE;
