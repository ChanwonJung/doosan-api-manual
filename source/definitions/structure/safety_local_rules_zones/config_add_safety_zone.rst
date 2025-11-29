.. _struct_CONFIG_ADD_SAFETY_ZONE:
.. _struct_CONFIG_SAFETY_ZONE:

CONFIG_ADD_SAFETY_ZONE
======================

This structure defines the **configuration of a safety zone**,  
including its unique identifier, zone type, and corresponding property and shape definitions.  
It is also used as an alias type ``CONFIG_SAFETY_ZONE`` for general safety zone handling.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szIdentifier``
     - ``char[32]``
     - -
     - Unique zone identifier (UUID string)
   * - 32
     - ``_szAlias``
     - ``char[32]``
     - -
     - Zone alias or descriptive name (nullable)
   * - 64
     - ``_iZoneType``
     - ``unsigned char``
     - 0~1
     - Zone type flag |br|
       (0: Space Limit Zone, 1: Local Zone)
   * - 65
     - ``_tZoneProperty``
     - :ref:`SAFETY_ZONE_PROPERTY_DATA <union_SAFETY_ZONE_PROPERTY_DATA>`
     - -
     - Property configuration for the safety zone (limits, local zone overrides, etc.)
   * - 265
     - ``_tShape``
     - :ref:`SAFETY_ZONE_SHAPE <struct_SAFETY_ZONE_SHAPE>`
     - -
     - Geometric shape definition of the safety zone

Total size: 402 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_ADD_SAFETY_ZONE
   {
       /* Unique zone identifier (UUID) */
       char _szIdentifier[32];

       /* Zone alias (nullable string) */
       char _szAlias[32];

       /* Zone type: 0(space limit), 1(local zone) */
       unsigned char _iZoneType;

       /* Zone property data */
       SAFETY_ZONE_PROPERTY_DATA _tZoneProperty;

       /* Zone shape definition */
       SAFETY_ZONE_SHAPE _tShape;

   } CONFIG_ADD_SAFETY_ZONE, *LPCONFIG_ADD_SAFETY_ZONE;

   typedef CONFIG_ADD_SAFETY_ZONE CONFIG_SAFETY_ZONE;

.. note::
   - ``CONFIG_SAFETY_ZONE`` is defined as a **type alias** of ``CONFIG_ADD_SAFETY_ZONE``.  
   - This structure combines both **logical properties** and **spatial geometry** of a safety zone.  
   - The shape and behavior of each zone are controlled through  
     :ref:`SAFETY_ZONE_PROPERTY_DATA <union_SAFETY_ZONE_PROPERTY_DATA>` and  
     :ref:`SAFETY_ZONE_SHAPE <struct_SAFETY_ZONE_SHAPE>` respectively.
