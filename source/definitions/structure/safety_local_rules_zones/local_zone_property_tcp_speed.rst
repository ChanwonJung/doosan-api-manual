.. _struct_LOCAL_ZONE_PROPERTY_TCP_SPEED:

LOCAL_ZONE_PROPERTY_TCP_SPEED
=============================

This structure defines a **local override for the TCP (Tool Center Point) speed limit**  
within a designated safety zone. It allows zone-specific restrictions on TCP velocity  
to enhance operator safety or precision during collaborative operations.

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
       0: Use global TCP speed limit |br|
       1: Apply local TCP speed limit
   * - 1
     - ``_fSpeed``
     - ``float``
     - -
     - Local TCP speed limit (m/s)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_TCP_SPEED
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Optional reduced override (deprecated) */
       /* unsigned char _iOverrideReduce; */

       /* Local TCP speed limit (m/s) */
       float _fSpeed;
   } LOCAL_ZONE_PROPERTY_TCP_SPEED, *LPLOCAL_ZONE_PROPERTY_TCP_SPEED;

.. note::
   - This structure is used to locally **reduce the maximum TCP speed**  
     in specific workspace zones.  
   - Typically applied when a robot operates near humans or precision fixtures.
