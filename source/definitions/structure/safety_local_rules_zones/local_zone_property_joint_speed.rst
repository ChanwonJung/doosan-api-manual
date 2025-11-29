.. _struct_LOCAL_ZONE_PROPERTY_JOINT_SPEED:

LOCAL_ZONE_PROPERTY_JOINT_SPEED
===============================

This structure defines **local joint speed limits** for a specific safety zone.  
It allows selective overriding of the global joint speed configuration  
to restrict motion speed within designated zones for safety purposes.

Each joint can independently override the global setting using the `_iOverride` flag array.

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
     - ``unsigned char[6]``
     - 0 or 1
     - **Override flag for each joint** |br|
       0: Use global joint speed limit |br| 
       1: Override with local value |br|
   * - 6
     - ``_fSpeed``
     - ``float[6]``
     - -
     - Local joint speed limits (°/s or rad/s). |br|  
       Applied only if `_iOverride[i] = 1` for the corresponding joint.

Total size: 30 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_JOINT_SPEED
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride[6];

       /* Optional reduced override (deprecated) */
       /* unsigned char _iOverrideReduce[6]; */

       /* Local joint speed limits (°/s or rad/s) */
       float _fSpeed[6];
   } LOCAL_ZONE_PROPERTY_JOINT_SPEED, *LPLOCAL_ZONE_PROPERTY_JOINT_SPEED;

.. note::
   - ``_iOverride`` enables per-joint selective activation of local limits.  
   - Used for safety-critical applications to slow robot motion  
     when entering specific workspace zones (e.g., collaborative or restricted areas).
