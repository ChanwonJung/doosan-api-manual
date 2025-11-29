.. _struct_SAFETY_ZONE_SHAPE_SPHERE:

SAFETY_ZONE_SHAPE_SPHERE
========================

This structure defines the **geometric parameters of a spherical safety zone**,  
which is used to detect robot or object intrusion based on a specified center point and radius.

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
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Center position of the sphere (X, Y, Z)
   * - 12
     - ``_fRadius``
     - ``float``
     - -
     - Radius of the spherical zone (mm)

Total size: 16 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE_SPHERE
   {   
       /* center position (X, Y, Z) */
       POINT_3D _tCenter;
       /* sphere radius (mm) */
       float _fRadius;
   } SAFETY_ZONE_SHAPE_SPHERE, *LPSAFETY_ZONE_SHAPE_SPHERE;
