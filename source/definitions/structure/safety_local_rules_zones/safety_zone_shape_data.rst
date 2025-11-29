.. _union_SAFETY_ZONE_SHAPE_DATA:

SAFETY_ZONE_SHAPE_DATA
======================

This **union** defines a flexible data container for multiple **safety zone shape types**,  
allowing a single structure to represent spheres, cylinders, cuboids, capsules, or other complex 3D zone geometries.  
It is used in conjunction with zone configuration structures (e.g., :ref:`CONFIG_SAFETY_ZONE <struct_CONFIG_SAFETY_ZONE>`).

The union ensures efficient memory use by sharing a single data block across different shape definitions.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Shape Type**
     - **Remarks**
   * - 0
     - ``_tSphere``
     - :ref:`SAFETY_ZONE_SHAPE_SPHERE <struct_SAFETY_ZONE_SHAPE_SPHERE>`
     - Sphere
     - Defines a spherical zone using center and radius.
   * - 0
     - ``_tCylinder``
     - :ref:`SAFETY_ZONE_SHAPE_CYLINDER <struct_SAFETY_ZONE_SHAPE_CYLINDER>`
     - Cylinder
     - Defines a cylindrical zone with radius and Z-limits.
   * - 0
     - ``_tCuboid``
     - :ref:`SAFETY_ZONE_SHAPE_CUBOID <struct_SAFETY_ZONE_SHAPE_CUBOID>`
     - Cuboid
     - Defines a rectangular box aligned with global axes.
   * - 0
     - ``_tOBB``
     - :ref:`SAFETY_ZONE_SHAPE_TILTED_CUBOID <struct_SAFETY_ZONE_SHAPE_TILTED_CUBOID>`
     - Tilted Cuboid
     - Defines an oriented (rotated) box using local axes.
   * - 0
     - ``_tMultiPlane``
     - :ref:`SAFETY_ZONE_SHAPE_MULTI_PLANE <struct_SAFETY_ZONE_SHAPE_MULTI_PLANE>`
     - Multi-Plane
     - Defines a convex volume bounded by up to six planar surfaces.
   * - 0
     - ``_tCapsule``
     - :ref:`SAFETY_ZONE_SHAPE_CAPSULE <struct_SAFETY_ZONE_SHAPE_CAPSULE>`
     - Capsule
     - Defines a capsule zone (cylinder with hemispherical ends).
   * - 0
     - ``_iBuffer``
     - ``unsigned char[120]``
     - Raw memory buffer
     - Used for unified memory mapping across all shape types.

Total size: 120 bytes (maximum shared buffer)

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef union _SAFETY_ZONE_SHAPE_DATA
   {
       SAFETY_ZONE_SHAPE_SPHERE        _tSphere;
       SAFETY_ZONE_SHAPE_CYLINDER      _tCylinder;
       SAFETY_ZONE_SHAPE_CUBOID        _tCuboid;
       SAFETY_ZONE_SHAPE_TILTED_CUBOID _tOBB;
       SAFETY_ZONE_SHAPE_MULTI_PLANE   _tMultiPlane;
       SAFETY_ZONE_SHAPE_CAPSULE       _tCapsule;
       unsigned char                   _iBuffer[120];
   } SAFETY_ZONE_SHAPE_DATA, *LPSAFETY_ZONE_SHAPE_DATA;

.. note::
   - This union enables a **polymorphic representation** of safety zone shapes.
   - Only **one shape field** is valid at a time depending on the selected zone type.
   - ``_iBuffer`` serves as the **raw binary memory region** for data serialization or protocol transmission.
