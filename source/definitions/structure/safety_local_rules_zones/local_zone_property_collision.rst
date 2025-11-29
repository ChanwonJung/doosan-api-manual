.. _struct_LOCAL_ZONE_PROPERTY_COLLISION:

LOCAL_ZONE_PROPERTY_COLLISION
=============================

This structure defines a **local override for collision detection sensitivity**  
in a specific safety zone. It allows fine-tuning of the robot’s force-based  
collision detection system to adapt to different operational conditions.

.. list-table::
   :widths: 10 26 20 8 45
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
       0: Use global collision sensitivity |br|
       1: Apply local collision sensitivity
   * - 1
     - ``_fSensitivity``
     - ``float``
     - -
     - Local collision sensitivity value |br| 
       (lower value → higher sensitivity)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_COLLISION
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Optional inspection mode (deprecated) */
       /* unsigned char _iCollisionInspection; */

       /* Local collision sensitivity */
       float _fSensitivity;
   } LOCAL_ZONE_PROPERTY_COLLISION, *LPLOCAL_ZONE_PROPERTY_COLLISION;

.. note::
   - ``_fSensitivity`` typically represents a **threshold value**  
     for detecting external collision forces.  
   - A **lower value** increases sensitivity, triggering stops sooner.  
   - Useful for zones requiring **delicate contact** or **human proximity** protection.