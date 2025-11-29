.. _struct_LOCAL_ZONE_PROPERTY_TCP_FORCE:

LOCAL_ZONE_PROPERTY_TCP_FORCE
=============================

This structure defines a **local override for the TCP (Tool Center Point) force limit**  
within a specific safety zone. It allows the user to restrict or relax the allowable  
TCP force independently from the global configuration.

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
       0: Use global TCP force limit |br| 
       1: Apply local TCP force limit
   * - 1
     - ``_fForce``
     - ``float``
     - -
     - Local TCP force limit (N)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_TCP_FORCE
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Optional reduced override (deprecated) */
       /* unsigned char _iOverrideReduce; */

       /* Local TCP force limit (N) */
       float _fForce;
   } LOCAL_ZONE_PROPERTY_TCP_FORCE, *LPLOCAL_ZONE_PROPERTY_TCP_FORCE;

.. note::
   - Used for restricting **TCP contact force** in sensitive zones  
     such as collaborative or human-interaction areas.  
   - If `_iOverride` is set to `1`, the robot applies the specified `_fForce`  
     as the maximum allowable TCP force in that local zone.



