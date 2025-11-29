.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_OTHER:

CONFIG_DIGITAL_WELDING_INTERFACE_OTHER
======================================

This structure defines **user-assignable digital I/O options** for welding systems.  
It provides up to **10 flexible mapping slots** that can be configured for  
special or custom signals not covered by other interface structures.  
Each mapping slot follows :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`  
format for full configuration flexibility.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tOption1`` ~ ``_tOption10``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - User-defined digital welding options |br| 
       (e.g., synchronization triggers, external sensors, torch signals, machine interlocks)

Total size: 150 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_OTHER
   {
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption1;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption2;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption3;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption4;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption5;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption6;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption7;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption8;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption9;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption10;

   } CONFIG_DIGITAL_WELDING_INTERFACE_OTHER, *LPCONFIG_DIGITAL_WELDING_INTERFACE_OTHER;

.. note::
   - Allows **custom signal integration** into the welding communication interface.  
   - Useful for OEMs or integrators adding machine-specific digital inputs or outputs.  
   - Typical use cases include **external trigger**, **emergency logic**,  
     or **auxiliary status flags** during automated welding operations.