.. _struct_LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE:

LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE
===================================

This structure defines a **local override for the TCP self-collision stop mode**,  
which specifies how the robot stops when a **self-collision** or TCP safety event occurs.  
It functions similarly to :ref:`LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE <struct_LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE>`,  
but applies specifically to **TCP or self-limit events**.

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
       0: Use global TCP/SLF stop mode |br|
       1: Apply local stop mode
   * - 1
     - ``_iStopMode``
     - ``unsigned char``
     - 0, 2, 3, 4
     - **Stop behavior mode** |br|  
       (0: STO, 2: SS1, 3: SS2, 4: RS1)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Stop behavior mode (0: STO, 2: SS1, 3: SS2, 4: RS1) */
       unsigned char _iStopMode;
   } LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE, *LPLOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE;

.. note::
   - Used to define specific stop actions for **TCP overtravel or self-collision** detection.  
   - Ensures consistent safety response depending on the zone or motion type.  
   - Often used in **tool-limited or workspace-limited safety configurations**.