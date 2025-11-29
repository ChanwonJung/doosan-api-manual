.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_OPTION:

CONFIG_DIGITAL_WELDING_INTERFACE_OPTION
=======================================

This structure defines the **extended digital I/O mapping for optional welding functions**.  
It provides up to **15 configurable digital parameters**, allowing flexible integration  
with diverse welding machine options such as special mode toggles, protection features,  
and user-defined process controls.  
Each field uses :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`  
to define the digital interface details.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tOption1`` ~ ``_tOption15``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - User-defined digital welding options. |br|
       Each entry corresponds to one optional welding control signal, such as: |br|
       - Arc start/end delay setting |br|
       - Crater start/end delay setting

Total size: 225 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_OPTION
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
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption11;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption12;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption13;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption14;
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tOption15;

   } CONFIG_DIGITAL_WELDING_INTERFACE_OPTION, *LPCONFIG_DIGITAL_WELDING_INTERFACE_OPTION;

.. note::
   - This structure provides a **scalable mapping system** for custom digital welding functions.  
   - Each option slot (`_tOption1`~`_tOption15`) can represent **a specific control or status signal**.  
   - Commonly used in **multi-process or programmable welding controllers**.  
   - Compatible with both analog and digital interface setups.
