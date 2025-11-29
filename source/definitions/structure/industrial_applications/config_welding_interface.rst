.. _struct_CONFIG_WELDING_INTERFACE:

CONFIG_WELDING_INTERFACE
=========================

This structure defines the **configuration for analog welding interfaces**,  
including analog channel mappings (input/output) and digital I/O assignments for arc, gas, and wire feed control.  
It enables communication and control between the robot and external welding equipment.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bEnable``
     - ``unsigned char``
     - 0 or 1
     - Enable flag for the welding interface |br|
       (0: Disabled, 1: Enabled)
   * - 1
     - ``_tChOut[2]``
     - :ref:`WELDING_CHANNEL <struct_WELDING_CHANNEL>`
     - -
     - Output welding channels |br|
       (0: Voltage channel, 1: Current channel)
   * - 37
     - ``_tChIn[2]``
     - :ref:`WELDING_CHANNEL <struct_WELDING_CHANNEL>`
     - -
     - Input welding channels |br|
       (0: Voltage channel, 1: Current channel)
   * - 73
     - ``_iArcOnDO``
     - ``unsigned char``
     - 0~15
     - Digital output channel for **Arc On** signal
   * - 74
     - ``_iGasOnDO``
     - ``unsigned char``
     - 0~15
     - Digital output channel for **Gas On** signal
   * - 75
     - ``_iInchPDO``
     - ``unsigned char``
     - 0~15
     - Digital output channel for **Inching +** signal
   * - 76
     - ``_iInchNDO``
     - ``unsigned char``
     - 0~15
     - Digital output channel for **Inching -** signal

Total size: 77 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_WELDING_INTERFACE
   {
       /* Interface enable flag */
       unsigned char _bEnable;

       /* Output welding channels (0: Voltage, 1: Current) */
       WELDING_CHANNEL _tChOut[2];

       /* Input welding channels (0: Voltage, 1: Current) */
       WELDING_CHANNEL _tChIn[2];

       /* Digital output assignments */
       unsigned char _iArcOnDO;
       unsigned char _iGasOnDO;
       unsigned char _iInchPDO;
       unsigned char _iInchNDO;

   } CONFIG_WELDING_INTERFACE, *LPCONFIG_WELDING_INTERFACE;

.. note::
   - ``WELDING_CHANNEL`` defines the analog I/O configuration for individual channels.  
   - ``CONFIG_WELDING_INTERFACE`` groups all analog and digital parameters for full welding control.  
   - Typical wiring: |br|
     - Arc On / Gas On → Digital outputs |br|
     - Voltage / Current feedback → Analog inputs |br| 
     - Voltage / Current control → Analog outputs |br| 
   - Used for MIG/TIG welding integration in Doosan robot systems.