.. _struct_SAFETY_OBJECT_SPHERE:

SAFETY_OBJECT_SPHERE
====================

This structure defines a **spherical safety object** used in robot safety configuration.  
It represents a geometric boundary defined by a **radius** and a **center point**,  
which can be referenced by other configurations such as  
:ref:`CONFIG_TOOL_SHAPE <struct_CONFIG_TOOL_SHAPE>` or safety zone definitions.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fRadius``
     - ``float``
     - -
     - Radius of the spherical safety boundary
   * - 4
     - ``_tTargetPos``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Center position of the sphere in 3D space

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_OBJECT_SPHERE
   {
       /* Radius of the sphere [mm] */
       float _fRadius;
       /* Center position of the sphere (X, Y, Z) */
       POINT_3D _tTargetPos;
   } SAFETY_OBJECT_SPHERE, *LPSAFETY_OBJECT_SPHERE;
