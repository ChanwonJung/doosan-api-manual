.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_MODE:

CONFIG_DIGITAL_WELDING_INTERFACE_MODE
=====================================

This structure defines the **mode configuration mapping** for digital welding interfaces.  
It specifies the digital I/O assignments for various welding operation modes,  
such as 2T/4T toggle, pulse mode selection, and welding mode option settings.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tWeldingMode``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for Welding Mode Selection
   * - 15
     - ``_t2T2TSpecial``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Mapping for 2T/4T Mode or 2T Special signal
   * - 30
     - ``_tPulseMode``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for Pulse Mode Enable
   * - 45
     - ``_tWMopt1``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for Welding Mode Option 1

Total size: 60 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_MODE
   {
       /* Welding mode selection mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWeldingMode;

       /* 2T/4T mode or special toggle mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _t2T2TSpecial;

       /* Pulse mode activation mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tPulseMode;

       /* Welding mode option mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWMopt1;

   } CONFIG_DIGITAL_WELDING_INTERFACE_MODE, *LPCONFIG_DIGITAL_WELDING_INTERFACE_MODE;

.. note::
   - ``CONFIG_DIGITAL_WELDING_INTERFACE_MODE`` supports flexible mode selection via digital inputs.  
   - ``_t2T2TSpecial`` enables toggle between **momentary (2T)** and **latching (4T)** modes.  
   - ``_tPulseMode`` activates or deactivates **pulsed welding** functionality.  
   - Often used together with :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS <struct_CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS>`  
     for a complete digital welding interface configuration.