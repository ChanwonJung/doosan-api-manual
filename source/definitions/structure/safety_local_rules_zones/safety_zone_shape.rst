.. _struct_SAFETY_ZONE_SHAPE:

SAFETY_ZONE_SHAPE
=================

This structure defines the **core geometric description** of a safety zone,  
including its coordinate reference, shape type, dimensions, and boundary configuration.  
It serves as a **wrapper structure** that combines metadata (type, coordinate, margin, etc.)  
with the actual geometric data (:ref:`SAFETY_ZONE_SHAPE_DATA <union_SAFETY_ZONE_SHAPE_DATA>`).

.. list-table::
   :widths: 10 26 22 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iCoordinate``
     - ``unsigned char``
     - 0, 2
     - Coordinate system used for the safety zone |br| 
       (0: Base frame, 2: World frame)
   * - 1
     - ``_iShapeType``
     - ``unsigned char``
     - 0~5
     - **Geometry type of the safety zone** |br|
       0: Sphere |br|
       1: Cylinder |br| 
       2: Cuboid |br|
       3: Tilted Cuboid |br|
       4: Multi-Plane |br|
       5: Capsule
   * - 2
     - ``_tShapeData``
     - :ref:`SAFETY_ZONE_SHAPE_DATA <union_SAFETY_ZONE_SHAPE_DATA>`
     - -
     - Union structure containing the geometric parameters of the safety zone.
   * - 122
     - ``_fMargin``
     - ``float``
     - ± value
     - Margin offset for the zone boundary |br|  
       (Positive: Expand, Negative: Shrink)
   * - 126
     - ``_iValidSpace``
     - ``unsigned char``
     - 0 or 1
     - Defines whether the valid safety space is inside (0) or outside (1) the shape boundary.
   * - 127
     - ``_iReserved``
     - ``unsigned char[13]``
     - -
     - Reserved bytes for future extension and alignment.

Total size: 140 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE
   {
       /* coordinate reference: 0(base), 2(world) */
       unsigned char _iCoordinate;

       /* geometry object type:
          0(Sphere), 1(Cylinder), 2(Cuboid),
          3(Tilted Cuboid), 4(Multi-Plane), 5(Capsule) */
       unsigned char _iShapeType;

       /* geometry object data */
       SAFETY_ZONE_SHAPE_DATA _tShapeData;

       /* positive: expand, negative: shrink */
       float _fMargin;

       /* valid space (0: inside, 1: outside) */
       unsigned char _iValidSpace;

       /* reserved for future use */
       unsigned char _iReserved[13];
   } SAFETY_ZONE_SHAPE, *LPSAFETY_ZONE_SHAPE;

.. note::
   - The **_tShapeData** field uses a union to represent multiple shape types within a single memory layout.  
   - ``_fMargin`` enables fine-tuning of safety boundaries for precision applications.  
   - ``_iValidSpace`` distinguishes whether the robot should operate **inside** or **outside** the defined geometry.
