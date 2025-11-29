.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS:

CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS
========================================

This structure defines the **digital welding process interface mapping**,  
linking core process-related signals such as welding start, robot readiness,  
and error reset to specific digital I/O communication channels.  
Each signal is defined using :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tWeldingStart``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Welding Start** signal
   * - 15
     - ``_tRobotReady``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Robot Ready** handshake signal
   * - 30
     - ``_tErrorReset``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Error Reset** command

Total size: 45 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS
   {
       /* Welding Start signal mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tWeldingStart;

       /* Robot Ready signal mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tRobotReady;

       /* Error Reset signal mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tErrorReset;

   } CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS, *LPCONFIG_DIGITAL_WELDING_INTERFACE_PROCESS;

.. note::
   - This structure enables synchronization between the **robot controller** and the **welding machine**.  
   - ``_tRobotReady`` ensures readiness confirmation before initiating a welding sequence.  
   - ``_tErrorReset`` supports digital recovery from welding faults or interlocks.
