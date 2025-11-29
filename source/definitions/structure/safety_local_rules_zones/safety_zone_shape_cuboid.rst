.. _struct_SAFETY_ZONE_SHAPE_CUBOID:

SAFETY_ZONE_SHAPE_CUBOID
========================

This structure defines the **cuboid-shaped safety zone**,  
used for representing rectangular 3D restricted regions in the robot workspace.  
It is described by minimum and maximum limits along each axis.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fXLoLimit``
     - ``float``
     - -
     - Minimum X-axis limit
   * - 4
     - ``_fYLoLimit``
     - ``float``
     - -
     - Minimum Y-axis limit
   * - 8
     - ``_fZLoLimit``
     - ``float``
     - -
     - Minimum Z-axis limit
   * - 12
     - ``_fXUpLimit``
     - ``float``
     - -
     - Maximum X-axis limit
   * - 16
     - ``_fYUpLimit``
     - ``float``
     - -
     - Maximum Y-axis limit
   * - 20
     - ``_fZUpLimit``
     - ``float``
     - -
     - Maximum Z-axis limit

Total size: 24 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_SHAPE_CUBOID
   {
       /* minimum limits (X, Y, Z) */
       float _fXLoLimit;
       float _fYLoLimit;
       float _fZLoLimit;

       /* maximum limits (X, Y, Z) */
       float _fXUpLimit;
       float _fYUpLimit;
       float _fZUpLimit;
   } SAFETY_ZONE_SHAPE_CUBOID, *LPSAFETY_ZONE_SHAPE_CUBOID;
