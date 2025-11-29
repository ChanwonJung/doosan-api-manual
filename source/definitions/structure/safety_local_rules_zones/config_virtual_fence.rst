.. _struct_CONFIG_VIRTUAL_FENCE:

CONFIG_VIRTUAL_FENCE
====================

This structure defines the configuration parameters for **Virtual Fence**,  
which limits the robot’s operational workspace using geometric boundaries such as cubes, polygons, or cylinders.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetRef``
     - ``unsigned char``
     - 0, 1, 101-200
     - Coordinate reference for the virtual fence. |br|
       BASE: 0, TOOL: 1, USER COORD: 101-200
   * - 1
     - ``_iFenceType``
     - ``unsigned char``
     - 0-2
     - **Fence shape type** |br|
       0: Cube, 1: Polygon, 2: Cylinder
   * - 2
     - ``_tFenceObject``
     - :ref:`VIRTUAL_FENCE_OBJECT <union_VIRTUAL_FENCE_OBJECT>`
     - -
     - Operation space geometry definition for the selected fence type.

Total size: 149 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_VIRTUAL_FENCE
   {
       unsigned char        _iTargetRef;     /* coordinate reference (base:0, tool:1, user:101~200) */
       unsigned char        _iFenceType;     /* fence type (cube:0, polygon:1, cylinder:2) */
       VIRTUAL_FENCE_OBJECT _tFenceObject;   /* virtual fence geometry definition */
   } CONFIG_VIRTUAL_FENCE, *LPCONFIG_VIRTUAL_FENCE;
