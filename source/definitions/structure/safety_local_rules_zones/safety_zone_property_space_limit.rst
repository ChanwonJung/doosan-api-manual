.. _struct_SAFETY_ZONE_PROPERTY_SPACE_LIMIT:

SAFETY_ZONE_PROPERTY_SPACE_LIMIT
================================

This structure defines the **spatial limitation properties** for a safety zone.  
It configures how robot motion is inspected and constrained (body or TCP-based),  
and specifies optional **joint range overrides** and **dynamic zone activation inputs**.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iInspectionType``
     - ``unsigned char``
     - 0~1
     - **Type of inspection target** |br|  
       0: Robot body-based |br|
       1: TCP (Tool Center Point)-based
   * - 1
     - ``_tJointRangeOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_JOINT_RANGE <struct_LOCAL_ZONE_PROPERTY_JOINT_RANGE>`
     - -
     - Local override of joint motion limits |br| 
       (applied only if the override flag is active for each joint).
   * - 55
     - ``_iDynamicZoneEnable``
     - ``unsigned char``
     - 0~8
     - **Dynamic zone activation input channel** |br| 
       0: Not used, 1~8: Safety input channel number
   * - 56
     - ``_iInsideZoneDectection``
     - ``unsigned char``
     - 0~8
     - **Inside-zone detection input channel** |br| 
       0: Not used, 1~8: Safety input channel number

Total size: 57 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_PROPERTY_SPACE_LIMIT
   {
       /* Inspection Type: 0(body), 1(tcp) */
       unsigned char _iInspectionType;

       /* Valid Space (deprecated field)
       unsigned char _iValidSpace;
       */

       /* Override Joint Range configuration */
       LOCAL_ZONE_PROPERTY_JOINT_RANGE _tJointRangeOverride;

       /* Dynamic Zone Enable Option:
          0(Not used), 1~8(Safety input channel) */
       unsigned char _iDynamicZoneEnable;

       /* Inside Zone Detection Option:
          0(Not used), 1~8(Safety input channel) */
       unsigned char _iInsideZoneDectection;
   } SAFETY_ZONE_PROPERTY_SPACE_LIMIT, *LPSAFETY_ZONE_PROPERTY_SPACE_LIMIT;

.. note::
   - ``_iInspectionType`` determines whether motion safety is monitored based on  
     the **robot body** or the **TCP (Tool Center Point)** position.
   - ``_tJointRangeOverride`` provides **joint-level customization** for this zone only.
   - ``_iDynamicZoneEnable`` and ``_iInsideZoneDectection`` can be mapped  
     to **specific safety input channels** for runtime activation or detection.
   - The commented ``_iValidSpace`` field existed in older versions  
     to indicate inside/outside validity, but is now replaced by zone-type logic.
