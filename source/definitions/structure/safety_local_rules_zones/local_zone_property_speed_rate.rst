.. _struct_LOCAL_ZONE_PROPERTY_SPEED_RATE:

LOCAL_ZONE_PROPERTY_SPEED_RATE
==============================

This structure defines a **local override for the overall robot speed scaling factor**  
within a designated safety zone. It adjusts the **robot’s global motion speed rate**  
to ensure safe operation when the robot enters or operates inside a restricted zone.

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
       0: Use global speed rate  |br|
       1: Apply local speed rate
   * - 1
     - ``_fSpeedRate``
     - ``float``
     - 0.0 ~ 1.0
     - Local motion speed rate multiplier |br|
       (e.g., 0.5 → 50% of global speed)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_SPEED_RATE
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Local motion speed rate (0.0 ~ 1.0) */
       float _fSpeedRate;
   } LOCAL_ZONE_PROPERTY_SPEED_RATE, *LPLOCAL_ZONE_PROPERTY_SPEED_RATE;

.. note::
   - This structure allows dynamically scaling robot motion speed in a **local zone**.  
   - Commonly used for **collaborative mode** or **restricted operation areas**.  
   - Setting `_fSpeedRate` to `0.5` limits all motion commands to 50% of normal speed.
