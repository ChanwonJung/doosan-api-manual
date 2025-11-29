.. _struct_SAFETY_ZONE_SHAPE_CYLINDER:

SAFETY_ZONE_SHAPE_CYLINDER
==========================

This structure defines the **cylindrical safety zone**,  
used to represent vertical or radial restricted areas within the robot workspace.  
It is parameterized by a 2D center, a radius, and Z-axis height limits.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tCenter``
     - :ref:`POINT_2D <struct_POINT_2D>`
     - -
     - 2D center position (X, Y) of the cylindrical base
   * - 8
     - ``_fRadius``
     - ``float``
     - -
     - Cylinder radius (mm)
   * - 12
     - ``_fZLoLimit``
     - ``float``
     - -
     - Minimum Z limit of the cylinder (bottom surface)
   * - 16
     - ``_fZUpLimit``
     - ``float``
     - -
     - Maximum Z limit of the cylinder (top surface)

Total size: 20 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE_CYLINDER
   {
       /* base center (X, Y) */
       POINT_2D _tCenter;
       /* cylinder radius (mm) */
       float _fRadius;
       /* bottom and top height limits */
       float _fZLoLimit;
       float _fZUpLimit;
   } SAFETY_ZONE_SHAPE_CYLINDER, *LPSAFETY_ZONE_SHAPE_CYLINDER;
