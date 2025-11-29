.. _struct_SAFETY_ZONE_SHAPE_TILTED_CUBOID:

SAFETY_ZONE_SHAPE_TILTED_CUBOID
===============================

This structure defines a **tilted cuboid safety zone**,  
representing a 3D rectangular region that is not necessarily aligned with the global coordinate axes.  
It is described by an origin point and three end points defining the local **U**, **V**, and **W** axes of the cuboid.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tOrigin``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Starting point (origin) of the tilted cuboid
   * - 12
     - ``_tUAxisEnd``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Endpoint of the **U-axis** (local X-axis direction)
   * - 24
     - ``_tVAxisEnd``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Endpoint of the **V-axis** (local Y-axis direction)
   * - 36
     - ``_tWAxisEnd``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Endpoint of the **W-axis** (local Z-axis direction)

Total size: 48 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE_TILTED_CUBOID
   {
       /* origin point of the tilted cuboid */
       POINT_3D _tOrigin;
       /* local U-axis endpoint */
       POINT_3D _tUAxisEnd;
       /* local V-axis endpoint */
       POINT_3D _tVAxisEnd;
       /* local W-axis endpoint */
       POINT_3D _tWAxisEnd;
   } SAFETY_ZONE_SHAPE_TILTED_CUBOID, *LPSAFETY_ZONE_SHAPE_TILTED_CUBOID;
