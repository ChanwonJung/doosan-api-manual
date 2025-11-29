.. _struct_CONFIG_COLLISION_MUTE_ZONE_PROPERTY:

CONFIG_COLLISION_MUTE_ZONE_PROPERTY
===================================

This structure defines the property information for **collision monitoring mute zones**,  
which are spaces where collision detection is temporarily disabled.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szIdentifier[32]``
     - ``char[32]``
     - -
     - Unique ID string identifying the mute zone.
   * - 32
     - ``_iOnOff``
     - ``unsigned char``
     - -
     - Enable flag |br|
       (0: Disabled, 1: Enabled)
   * - 33
     - ``_fSensitivity``
     - ``float``
     - -
     - Collision sensitivity (0-100%)
   * - 37
     - ``_tZone``
     - :ref:`SAFETY_OBJECT <struct_SAFETY_OBJECT>`
     - -
     - Definition of the mute zone geometry and boundaries.

Total size: 139 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_COLLISION_MUTE_ZONE_PROPERTY
   {
       char            _szIdentifier[32];  // ID
       unsigned char   _iOnOff;            // enable flag
   #ifdef INFRACORE_PATCH
       unsigned char   _iSafetyIO;         // optional: safety I/O config (patch only)
   #endif
       float           _fSensitivity;      // collision sensitivity (0–100%)
       SAFETY_OBJECT   _tZone;             // geometry definition of mute zone
   } CONFIG_COLLISION_MUTE_ZONE_PROPERTY, *LPCONFIG_COLLISION_MUTE_ZONE_PROPERTY;