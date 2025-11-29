.. _struct_CONFIG_COLLISION_MUTE_ZONE:

CONFIG_COLLISION_MUTE_ZONE
==========================

This is a structure information to set the **collision monitoring mute (invalid) space**,
composed of enable flags and an array of mute-zone properties.

.. toctree::
   :maxdepth: 1
   :caption: Substructures
   :hidden:

   config_collision_mute_zone_property

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iValidity[10]``
     - ``unsigned char[10]``
     - -
     - Per-entry validity flag for each mute zone |br|
       (0: invalid, 1: valid)
   * - 10
     - ``_tProperty[10]``
     - :ref:`CONFIG_COLLISION_MUTE_ZONE_PROPERTY <struct_CONFIG_COLLISION_MUTE_ZONE_PROPERTY>`\[10]
     - -
     - Mute zone property array (ID, enable, sensitivity, and geometry)

Total size : 1,400 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_COLLISION_MUTE_ZONE
   {
       /* validity of safety object: 0(invalid), 1(valid) */
       unsigned char                         _iValidity[10];
       /* mute zone property list */
       CONFIG_COLLISION_MUTE_ZONE_PROPERTY   _tProperty[10];
   } CONFIG_COLLISION_MUTE_ZONE, *LPCONFIG_COLLISION_MUTE_ZONE;