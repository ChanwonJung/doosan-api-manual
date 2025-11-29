.. _struct_LOCAL_ZONE_PROPERTY_TCP_POWER:

LOCAL_ZONE_PROPERTY_TCP_POWER
=============================

This structure defines a **local override for the TCP (Tool Center Point) power limit**  
within a specific safety zone. It allows defining a lower maximum allowable TCP power  
for collision prevention or compliance with safety standards.

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
       0: Use global TCP power limit |br| 
       1: Apply local TCP power limit
   * - 1
     - ``_fPower``
     - ``float``
     - -
     - Local TCP power limit (W)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_TCP_POWER
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Optional reduced override (deprecated) */
       /* unsigned char _iOverrideReduce; */

       /* Local TCP power limit (W) */
       float _fPower;
   } LOCAL_ZONE_PROPERTY_TCP_POWER, *LPLOCAL_ZONE_PROPERTY_TCP_POWER;
