.. _struct_CONFIG_DIGITAL_WELDING_INTERFACE_TEST:

CONFIG_DIGITAL_WELDING_INTERFACE_TEST
=====================================

This structure defines the **digital I/O mapping for welding test and auxiliary operations**.  
It configures digital channels used for gas tests, inching control, torch blowout, simulation,  
and optional custom test signals.  
Each field is defined using :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tGasTest``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Gas Test** settings
   * - 15
     - ``_tInchingP``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Mapping for **Wire Inching (+)** settings
   * - 30
     - ``_tInchingM``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Mapping for **Wire Inching (−)** settings
   * - 45
     - ``_tBlowOutTorch``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Torch Blow-Out** settings
   * - 60
     - ``_tSimulation``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Digital mapping for **Welding Simulation Mode**
   * - 75
     - ``_tTSopt1``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Optional **Test Signal 1** settings
   * - 90
     - ``_tTSopt2``
     - :ref:`CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA <struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA>`
     - -
     - Optional **Test Signal 2** settings

Total size: 105 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_INTERFACE_TEST
   {
       /* Gas Test digital mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tGasTest;

       /* Inching positive direction (wire feed +) */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tInchingP;

       /* Inching negative direction (wire retract −) */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tInchingM;

       /* Torch blow-out operation */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tBlowOutTorch;

       /* Welding simulation mode mapping */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tSimulation;

       /* Optional Test Signal 1 */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tTSopt1;

       /* Optional Test Signal 2 */
       CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA _tTSopt2;

   } CONFIG_DIGITAL_WELDING_INTERFACE_TEST, *LPCONFIG_DIGITAL_WELDING_INTERFACE_TEST;

.. note::
   - This structure manages **manual testing and setup** features for digital welding systems.  
   - ``_tInchingP`` and ``_tInchingM`` are essential for manual wire control during setup.  
   - ``_tSimulation`` allows validation of I/O communication without actual arc ignition.  
   - Optional fields ``_tTSopt1`` and ``_tTSopt2`` can be repurposed for **custom digital test signals**.
