.. _union_SAFETY_OBJECT_DATA:

SAFETY_OBJECT_DATA
==================

This is an **object structure information** for safe space configuration,  
which stores various types of safety object geometries (sphere, capsule, cube, OBB, and polyprism).  
Each member represents a specific geometric type and refers to its respective structure definition.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - Sphere object
     - :ref:`SAFETY_OBJECT_SPHERE <struct_SAFETY_OBJECT_SPHERE>`
     - -
     - Refer to the Definition of Struct
   * - 16
     - Capsule object
     - :ref:`SAFETY_OBJECT_CAPSULE <struct_SAFETY_OBJECT_CAPSULE>`
     - -
     - Refer to the Definition of Struct
   * - 28
     - Cube object
     - :ref:`SAFETY_OBJECT_CUBE <struct_SAFETY_OBJECT_CUBE>`
     - -
     - Refer to the Definition of Struct
   * - 48
     - OBB object
     - :ref:`SAFETY_OBJECT_OBB <struct_SAFETY_OBJECT_OBB>`
     - -
     - Refer to the Definition of Struct
   * - 89
     - Polyprism object
     - :ref:`SAFETY_OBJECT_POLYPRISM <struct_SAFETY_OBJECT_POLYPRISM>`
     - -
     - Refer to the Definition of Struct
   * - 100
     - Reserved space
     - ``unsigned char[100]``
     - -
     - Reserved space (for alignment or future expansion)

Total size: 100 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef union _SAFETY_OBJECT_DATA
   {
       SAFETY_OBJECT_SPHERE    _tSphere;       /* Sphere object */
       SAFETY_OBJECT_CAPSULE   _tCapsule;      /* Capsule object */
       SAFETY_OBJECT_CUBE      _tCube;         /* Cube object */
       SAFETY_OBJECT_OBB       _tOBB;          /* Oriented bounding box object */
       SAFETY_OBJECT_POLYPRISM _tPolyPrism;    /* Polygonal prism object */
       unsigned char           _iBuffer[100];  /* Reserved buffer space */
   } SAFETY_OBJECT_DATA, *LPSAFETY_OBJECT_DATA;
