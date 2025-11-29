.. _struct_SAFETY_OBJECT_OBB:

SAFETY_OBJECT_OBB
=================

This structure defines an **Oriented Bounding Box (OBB)** safety object,  
which represents a 3D cuboid that can be **rotated** relative to the base frame.  
Unlike :ref:`SAFETY_OBJECT_CUBE <struct_SAFETY_OBJECT_CUBE>`,  
this version uses four reference points to specify the box orientation in 3D space.

.. list-table::
   :widths: 10 28 22 8 45
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tTargetPos[4]``
     - :ref:`POINT_3D <struct_POINT_3D>` ``[4]``
     - -
     - **Box vertices defining orientation** |br|
       ``_tTargetPos[0]``: Standard origin  |br|
       ``_tTargetPos[1]``: X-axis endpoint  |br|
       ``_tTargetPos[2]``: Y-axis endpoint  |br|
       ``_tTargetPos[3]``: Z-axis endpoint

Total size: 48 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_OBJECT_OBB
   {
       /* Vertices defining the oriented bounding box */
       /* std(0), x-end(1), y-end(2), z-end(3) */
       POINT_3D _tTargetPos[4];
   } SAFETY_OBJECT_OBB, *LPSAFETY_OBJECT_OBB;
