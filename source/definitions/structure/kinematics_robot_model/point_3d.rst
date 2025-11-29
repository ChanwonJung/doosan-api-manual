.. _struct_POINT_3D:

POINT_3D
========

This structure represents a **3D point** defined by X, Y, and Z coordinates.  
It is commonly used for position representation in Cartesian space,  
such as robot TCP position, object location, or safety zone vertices.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fXPos``
     - ``float``
     - [mm]
     - X coordinate
   * - 4
     - ``_fYPos``
     - ``float``
     - [mm]
     - Y coordinate
   * - 8
     - ``_fZPos``
     - ``float``
     - [mm]
     - Z coordinate

Total size: 12 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _POINT_3D
   {
       float _fXPos;   /* X position [mm] */
       float _fYPos;   /* Y position [mm] */
       float _fZPos;   /* Z position [mm] */
   } POINT_3D, *LPPOINT_3D;
