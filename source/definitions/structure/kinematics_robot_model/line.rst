.. _struct_LINE:
.. _struct_LINE_2D:  

LINE
====

This structure defines a **2D line segment** represented by a start point and an end point.  
Each point is defined using the :ref:`POINT_2D <struct_POINT_2D>` structure.  
It is typically used for planar geometry calculations such as  
boundary definitions, region drawing, or graphical path representation.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tFromPoint``
     - :ref:`POINT_2D <struct_POINT_2D>`
     - [mm]
     - Start point of the line segment
   * - 8
     - ``_tToPoint``
     - :ref:`POINT_2D <struct_POINT_2D>`
     - [mm]
     - End point of the line segment

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LINE
   {
       POINT_2D _tFromPoint;   /* Start point (X1, Y1) */
       POINT_2D _tToPoint;     /* End point (X2, Y2) */
   } LINE, *LPLINE;

   typedef LINE LINE_2D;

Both ``LINE`` and ``LINE_2D`` refer to the same structure.