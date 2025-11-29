.. _struct_LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE:

LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE
======================================

This structure defines a **local override for the robot’s collision stop mode**  
within a specific safety zone. It allows customizing how the robot reacts  
when a collision is detected, depending on the operational context.

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
       0: Use global stop mode |br|  
       1: Apply local stop mode
   * - 1
     - ``_iStopMode``
     - ``unsigned char``
     - 0, 2, 3, 4
     - **Stop behavior mode** |br|
       0: STO (Safe Torque Off), 2: SS1 (Safe Stop 1) |br| 
       3: SS2 (Safe Stop 2), 4: RS1 (Reduced Speed 1)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Stop behavior mode (0: STO, 2: SS1, 3: SS2, 4: RS1) */
       unsigned char _iStopMode;
   } LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE, *LPLOCAL_ZONE_PROPERTY_COLLISION_STOPMODE;

.. note::
   - Enables zone-specific stop behavior upon **collision detection**.  
   - Helps balance **safety and mechanical integrity** in multi-zone workspaces.
