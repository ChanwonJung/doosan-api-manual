.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION:

CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION
==========================================

This structure defines the **digital interface mapping for welding condition parameters**,  
allowing configuration and monitoring of numeric welding values through digital I/O.  
It includes job selection, synergic ID, wire feed speed, and dynamic correction parameters.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tJobNumber``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Job Number Selection**
   * - 15
     - ``_tSynegicID``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Mapping for **Synergic ID**
   * - 30
     - ``_tWireFeedSpeed``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Wire Feed Speed Control**
   * - 45
     - ``_tArclengthCorrection``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Mapping for **Arc Length Correction**
   * - 60
     - ``_tDynamicCorrection``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Dynamic Correction**

Total size: 75 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION
   {
       /* Job number selection mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tJobNumber;

       /* Synergic ID mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tSynegicID;

       /* Wire feed speed mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWireFeedSpeed;

       /* Arc length correction mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tArclengthCorrection;

       /* Dynamic correction mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tDynamicCorrection;

   } CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION, *LPCONFIG_DIGITAL_WELDING_INTERFACE_CONDITION;

.. note::
   - Used for **synchronizing digital signals** with welding machine condition settings.  
   - ``_tJobNumber`` allows job-based parameter loading.  
   - ``_tDynamicCorrection`` helps dynamically stabilize the welding arc during process fluctuations.  
   - Enables **programmable control** of analog welding parameters over **digital communication buses**.