.. _struct_SAFETY_ZONE_SHAPE_CAPSULE:

SAFETY_ZONE_SHAPE_CAPSULE
=========================

This structure defines a **capsule-shaped safety zone**,  
which consists of a cylindrical body capped by hemispherical ends.  
It is typically used to model elongated or rod-shaped safety regions.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tCenter1``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Center of the first hemispherical end
   * - 12
     - ``_tCenter2``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Center of the second hemispherical end
   * - 24
     - ``_fRadius``
     - ``float``
     - -
     - Radius of the capsule’s cylindrical body and hemispherical caps

Total size: 28 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE_CAPSULE
   {
       /* center of first hemisphere */
       POINT_3D _tCenter1;
       /* center of second hemisphere */
       POINT_3D _tCenter2;
       /* capsule radius (mm) */
       float _fRadius;
   } SAFETY_ZONE_SHAPE_CAPSULE, *LPSAFETY_ZONE_SHAPE_CAPSULE;
