.. _struct_SAFETY_OBJECT:

SAFETY_OBJECT
=============

This structure defines a **generic safety object**,  
which specifies the reference coordinate system, object type, and corresponding geometric data.  
It serves as a unified representation of various safety object types  
(sphere, capsule, cube, oriented box, and polygon-prism),  
referencing the :ref:`SAFETY_OBJECT_DATA <union_SAFETY_OBJECT_DATA>` union for the actual geometry.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetRef``
     - ``unsigned char``
     - -
     - Reference coordinate system index |br| 
       (0: Base, 1: Tool, 2: World)
   * - 1
     - ``_iObjectType``
     - ``unsigned char``
     - 0~4
     - **Geometry object type** |br|
       (0: Sphere, 1: Capsule, 2: Cube |br| 
       3: Oriented Box, 4: Polygon-Prism)
   * - 2
     - ``_tObject``
     - :ref:`SAFETY_OBJECT_DATA <union_SAFETY_OBJECT_DATA>`
     - -
     - Geometry data for the selected object type

Total size: 102 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_OBJECT
   {
       /* Reference coordinate system (e.g., Base, Tool, World) */
       unsigned char _iTargetRef;

       /* Geometry type: 
          0: Sphere
          1: Capsule
          2: Cube
          3: Oriented Box
          4: Polygon-Prism
       */
       unsigned char _iObjectType;

       /* Geometry object data */
       SAFETY_OBJECT_DATA _tObject;

   } SAFETY_OBJECT, *LPSAFETY_OBJECT;
