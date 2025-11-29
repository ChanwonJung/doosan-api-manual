.. _union_VIRTUAL_FENCE_OBJECT:

VIRTUAL_FENCE_OBJECT
====================

This union defines the **geometry data** used for configuring a *Virtual Fence* zone.  
It supports multiple shape types (**cube**, **polygon**, and **cylinder**) sharing the same memory region.  
Each substructure provides spatial limits or boundaries along X, Y, and Z axes.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tCube``
     - ``struct``
     - -
     - Contains X/Y/Z upper and lower limits defining a rectangular prism region. |br|
       - ``_fXLoLimit, _fXUpLimit`` |br|  
       - ``_fYLoLimit, _fYUpLimit`` |br|  
       - ``_fZLoLimit, _fZUpLimit`` |br|
   * - 20
     - ``_tPolygon``
     - ``struct``
     - -
     - Defines a polygonal boundary using 2D line segments (:ref:`LINE <struct_LINE>`)  
       and vertical limits (``_fZLoLimit``, ``_fZUpLimit``). |br|
       - ``_iLineCount`` : number of polygon edges (max 6) |br|
       - ``_tLine[6]`` : line segments connecting each vertex |br| 
   * - 125
     - ``_tCylinder``
     - ``struct``
     - -
     - Represents a circular boundary with height limits. |br| 
       - ``_fRadius`` : cylinder radius |br| 
       - ``_fZLoLimit, _fZUpLimit`` : vertical limits |br| 
   * - 137
     - ``_iBuffer``
     - ``unsigned char[110]``
     - -
     - Reserved Space 10 bytes

Total size: 147 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef union _VIRTUAL_FENCE_OBJECT
   {
       struct _CUBE {
           float _fXLoLimit;
           float _fXUpLimit;
           float _fYLoLimit;
           float _fYUpLimit;
           float _fZLoLimit;
           float _fZUpLimit;
       } _tCube;

       struct _POLYGON {
           unsigned char _iLineCount;
           LINE          _tLine[6];
           float         _fZLoLimit;
           float         _fZUpLimit;
       } _tPolygon;

       struct _CYLINDER {
           float _fRadius;
           float _fZLoLimit;
           float _fZUpLimit;
       } _tCylinder;

       unsigned char _iBuffer[110];

   } VIRTUAL_FENCE_OBJECT, *LPVIRTUAL_FENCE_OBJECT;
