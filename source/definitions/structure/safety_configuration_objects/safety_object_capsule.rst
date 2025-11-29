.. _struct_SAFETY_OBJECT_CAPSULE:

SAFETY_OBJECT_CAPSULE
=====================

This structure defines a **capsule-shaped safety object**,  
which represents a cylindrical body capped with two hemispheres at both ends.  
It is commonly used to define elongated tools or robot link boundaries for collision monitoring.

.. list-table::
   :widths: 10 28 22 8 45
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
     - Radius of the capsule body
   * - 4
     - ``_tTargetPos[2]``
     - :ref:`POINT_3D <struct_POINT_3D>` ``[2]``
     - -
     - **Capsule endpoints** |br|
       ``_tTargetPos[0]``: Lower vertex |br|  
       ``_tTargetPos[1]``: Upper vertex

Total size: 28 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_OBJECT_CAPSULE
   {
       /* Capsule radius [mm] */
       float _fRadius;
       /* Capsule endpoints: low(0), high(1) */
       POINT_3D _tTargetPos[2];
   } SAFETY_OBJECT_CAPSULE, *LPSAFETY_OBJECT_CAPSULE;
