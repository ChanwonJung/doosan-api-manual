.. _struct_NORMAL_VECTOR:

NORMAL_VECTOR
==============

This structure defines the **normal vector calculation data** used for  
computing surface or orientation normals based on multiple reference poses.  
It stores three vector components, each containing six floating-point elements  
representing positions or directions in 3D space.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[3][NUMBER_OF_JOINT]``
     - -
     - Three vectors (X, Y, Z), each defined by six float elements

Total size: 72 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _NORMAL_VECTOR
   {
       /* Task position set for normal vector calculation */
       float _fTargetPos[3][NUMBER_OF_JOINT];

   } NORMAL_VECTOR, *LPNORMAL_VECTOR;
