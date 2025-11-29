.. _struct_LOCAL_ZONE_PROPERTY_SPEED_REDUCTION:

LOCAL_ZONE_PROPERTY_SPEED_REDUCTION
===================================

This structure defines a **local override for the robot’s speed reduction factor**  
within a safety zone. Unlike the speed rate, this parameter directly specifies  
a reduction ratio applied to the robot’s motion for safety or precision operations.

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
       0: Use global reduction rate |br|
       1: Apply local reduction rate 
   * - 1
     - ``_fReductionRate``
     - ``float``
     - 0.0 ~ 1.0
     - Local reduction ratio |br|
       (e.g., 0.7 → reduce speed by 30%)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOCAL_ZONE_PROPERTY_SPEED_REDUCTION
   {
       /* Override flag (0: no override, 1: override global property) */
       unsigned char _iOverride;

       /* Local reduction rate (0.0 ~ 1.0) */
       float _fReductionRate;
   } LOCAL_ZONE_PROPERTY_SPEED_REDUCTION, *LPLOCAL_ZONE_PROPERTY_SPEED_REDUCTION;

.. note::
   - This parameter defines the **proportional decrease** in speed  
     relative to the global configuration.  
   - Useful for enforcing **gradual slow-downs** in entry zones  
     before full stop regions or sensitive workspaces.  
   - Typical values range between **0.3 ~ 0.8** depending on application safety levels.