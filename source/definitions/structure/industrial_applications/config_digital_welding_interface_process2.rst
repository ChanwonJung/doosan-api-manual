.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2:

CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2
=========================================

This structure defines the **secondary process status and monitoring mapping**  
for digital welding interfaces.  
It focuses on real-time signal exchange between the welding robot and power source,  
tracking process flow, machine readiness, and current feedback.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tCurrentFlow``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Mapping for **Current Flow Detection**
   * - 15
     - ``_tProcessActive``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Prcoess activation settings
   * - 30
     - ``_tMainCurrent``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital feedback for **main current** settings
   * - 45
     - ``_tMachineReady``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Signal indicating **machine ready state** settings
   * - 60
     - ``_tCommReady``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Communication readiness flag between robot and welder

Total size: 75 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2
   {
       /* Welding current flow detection */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tCurrentFlow;

       /* Process active status mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tProcessActive;

       /* Main welding current feedback mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tMainCurrent;

       /* Machine ready signal mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tMachineReady;

       /* Communication readiness signal mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tCommReady;

   } CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2, *LPCONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2;

.. note::
   - This structure complements :ref:`CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS <struct_CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS>`  
     by providing **extended process monitoring** signals.  
   - ``_tMachineReady`` ensures proper startup synchronization.  
   - ``_tCommReady`` confirms communication between the welding controller and robot system.  
   - Commonly used in **digital fieldbus-controlled welding machines** (e.g., EtherCAT, ProfiNet).