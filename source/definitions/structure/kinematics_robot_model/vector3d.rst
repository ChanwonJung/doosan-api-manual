.. _struct_VECTOR3D:
.. _struct_NORMAL_VECTOR_RESPONSE:

VECTOR3D
========

This structure defines a **3-dimensional vector** representation  
used for expressing spatial direction, displacement, or surface normals.  
It is commonly used in geometric calculations and orientation operations.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[3]``
     - -
     - Vector components along X, Y, Z axes

Total size: 12 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _VECTOR3D
   {
       /* Vector components (X, Y, Z) */
       float _fTargetPos[3];

   } VECTOR3D, *LPVECTOR3D;

   typedef VECTOR3D NORMAL_VECTOR_RESPONSE, *LPNORMAL_VECTOR_RESPONSE;