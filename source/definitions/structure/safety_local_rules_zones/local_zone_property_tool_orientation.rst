.. _struct_LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION:

LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION
====================================

This structure defines a **local override for the tool orientation limit**  
within a safety zone. It constrains the **tool’s allowed direction** and **maximum rotation angle**,  
ensuring safe tool posture during operation.

.. list-table::
   :widths: 10 26 20 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iOverride``
     - ``unsigned char``
     - 0 or 1
     - **Override flag** |br|
       0: Use global orientation limit |br| 
       1: Apply local orientation limit
   * - 1
     - ``_fDirection``
     - ``float[3]``
     - -
     - Normalized direction vector (X, Y, Z) |br|  
       defining the allowed tool direction
   * - 13
     - ``_fAngle``
     - ``float``
     - degrees
     - Maximum allowable deviation angle (°)  
       from the defined tool direction

Total size: 17 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Tool direction vector (X, Y, Z) */
       float _fDirection[3];

       /* Maximum deviation angle (degrees) */
       float _fAngle;
   } LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION, *LPLOCAL_ZONE_PROPERTY_TOOL_ORIENTATION;

.. note::
   - Used for maintaining a **safe tool posture** in zones requiring  
     constrained approach angles (e.g., welding, inspection, or assembly).  
   - The robot limits tool orientation to remain within `_fAngle`  
     of the vector `_fDirection`.  
   - Prevents accidental contact or misalignment during close-proximity operations.