.. _struct_LOCAL_ZONE_PROPERTY_JOINT_RANGE:

LOCAL_ZONE_PROPERTY_JOINT_RANGE
===============================

This structure defines **local joint range limits** for a specific safety zone.  
It allows selective overriding of the global joint range configuration  
(:ref:`CONFIG_JOINT_RANGE <struct_CONFIG_JOINT_RANGE>`) for individual joints within a local zone.

Each joint can optionally override its global configuration using the `_iOverride` flag array.

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
       0: Use global joint range  |br|
       1: Override with local property |br|
   * - 6
     - ``_fMinRange``
     - ``float[6]``
     - -
     - Local minimum joint angle or position (° or rad). |br|
       Applied only if the corresponding `_iOverride[i] = 1`.
   * - 30
     - ``_fMaxRange``
     - ``float[6]``
     - -
     - Local maximum joint angle or position (° or rad). |br| 
       Applied only if the corresponding `_iOverride[i] = 1`.

Total size: 54 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_JOINT_RANGE
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride[6];

       /* Optional reduced override (deprecated) */
       /* unsigned char _iOverrideReduce[6]; */

       /* Minimum joint range (° or rad) */
       float _fMinRange[6];

       /* Maximum joint range (° or rad) */
       float _fMaxRange[6];
   } LOCAL_ZONE_PROPERTY_JOINT_RANGE, *LPLOCAL_ZONE_PROPERTY_JOINT_RANGE;

.. note::
   - This structure is typically nested within a **local safety zone configuration**  
     (see :ref:`SAFETY_ZONE_PROPERTY_LOCAL_ZONE <struct_SAFETY_ZONE_PROPERTY_LOCAL_ZONE>`).
   - The `_iOverride` array enables **joint-level selective overrides**,  
     making it useful for workspace-limited zones or restricted-motion tasks.
   - The commented `_iOverrideReduce` field indicates a previously supported  
     reduced mode override, reserved for backward compatibility.
