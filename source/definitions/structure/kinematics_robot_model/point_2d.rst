.. _struct_POINT_2D:

POINT_2D
========

This structure defines a **2D point** representation consisting of X and Y coordinates.  
It is mainly used in functions or data structures that handle planar geometry,  
such as tool path definition, GUI layout mapping, or 2D safety zone shapes.

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

Total size: 8 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _POINT_2D
   {
       float _fXPos;   /* X position [mm] */
       float _fYPos;   /* Y position [mm] */
   } POINT_2D, *LPPOINT_2D;
