.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING:

CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING
===========================================

This structure defines the **digital I/O mapping for real-time welding monitoring signals**.  
It connects digital channels to various process feedback values,  
such as voltage, current, wire feed, and error diagnostics.  
Each entry utilizes :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`  
to specify mapping, bit offset, and value range.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tWeldingVoltage``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Real-time voltage feedback mapping
   * - 15
     - ``_tWeldingCurrent``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Real-time current feedback mapping
   * - 30
     - ``_tWireFeedSpeed``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Wire feed speed monitoring channel
   * - 45
     - ``_tWireStick``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Detects wire stick events or blockages
   * - 60
     - ``_tError``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Error status monitoring (binary fault indicator)
   * - 75
     - ``_tErrorNumber``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Detailed error code mapping for diagnostics

Total size: 90 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING
   {
       /* Real-time voltage monitoring */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWeldingVoltage;

       /* Real-time current monitoring */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWeldingCurrent;

       /* Wire feed speed feedback */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWireFeedSpeed;

       /* Wire stick or jam detection */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWireStick;

       /* Error status flag */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tError;

       /* Error code mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tErrorNumber;

   } CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING, *LPCONFIG_DIGITAL_WELDING_INTERFACE_MONITORING;

.. note::
   - Provides **real-time process monitoring** over digital interfaces.  
   - ``_tError`` and ``_tErrorNumber`` allow both binary and numeric fault reporting.  
   - Ideal for **digital welding controllers** supporting feedback through fieldbus or GPIO mapping.