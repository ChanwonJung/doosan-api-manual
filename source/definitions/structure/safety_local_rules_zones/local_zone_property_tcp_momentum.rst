.. _struct_LOCAL_ZONE_PROPERTY_TCP_MOMENTUM:

LOCAL_ZONE_PROPERTY_TCP_MOMENTUM
================================

This structure defines a **local override for the TCP momentum limit**  
within a safety zone. It restricts the momentum (mass × velocity) of the TCP  
to reduce kinetic energy during collaborative or restricted operations.

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
       0: Use global TCP momentum limit |br|
       1: Apply local TCP momentum limit 
   * - 1
     - ``_fMomentum``
     - ``float``
     - -
     - Local TCP momentum limit (kg·m/s)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_TCP_MOMENTUM
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Optional reduced override (deprecated) */
       /* unsigned char _iOverrideReduce; */

       /* Local TCP momentum limit (kg·m/s) */
       float _fMomentum;
   } LOCAL_ZONE_PROPERTY_TCP_MOMENTUM, *LPLOCAL_ZONE_PROPERTY_TCP_MOMENTUM;

.. note::
   - Often used in conjunction with :ref:`LOCAL_ZONE_PROPERTY_TCP_POWER <struct_LOCAL_ZONE_PROPERTY_TCP_POWER>`.
