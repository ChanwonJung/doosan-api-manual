.. _struct_CONFIG_ANALOG_WELDING_INTERFACE:

CONFIG_ANALOG_WELDING_INTERFACE
===============================

This structure defines the configuration for an **analog welding interface**,  
linking detailed welding channels (voltage, current, and feeding speed)  
with corresponding digital outputs for welding control.  
It enables communication between the robot and analog welding equipment.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bMode``
     - ``unsigned char``
     - 0 or 1
     - Welding operation mode |br|
       (0: Stop, 1: Start)
   * - 1
     - ``_tTargetVoltage``
     - :ref:`CONFIG_WELDING_DETAIL_INFO <struct_CONFIG_WELDING_DETAIL_INFO>`
     - -
     - Target voltage configuration
   * - 19
     - ``_tFeedingSpeed``
     - :ref:`CONFIG_WELDING_DETAIL_INFO <struct_CONFIG_WELDING_DETAIL_INFO>`
     - -
     - Wire feeding speed configuration
   * - 37
     - ``_tWeldingVoltage``
     - :ref:`CONFIG_WELDING_DETAIL_INFO <struct_CONFIG_WELDING_DETAIL_INFO>`
     - -
     - Welding voltage control channel
   * - 55
     - ``_tWeldingCurrent``
     - :ref:`CONFIG_WELDING_DETAIL_INFO <struct_CONFIG_WELDING_DETAIL_INFO>`
     - -
     - Welding current control channel
   * - 73
     - ``_iArcOnDO``
     - ``unsigned char``
     - 0~16
     - Digital output channel for **Arc ON**
   * - 74
     - ``_iGasOnDO``
     - ``unsigned char``
     - 0~16
     - Digital output channel for **Gas ON**
   * - 75
     - ``_iInchPDO``
     - ``unsigned char``
     - 0~16
     - Digital output for **Inching + (forward)**
   * - 76
     - ``_iInchNDO``
     - ``unsigned char``
     - 0~16
     - Digital output for **Inching - (reverse)**
   * - 77
     - ``_iBlowOutValue``
     - ``unsigned char``
     - 0~16
     - Digital output for **Blow-out** control

Total size: 78 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_ANALOG_WELDING_INTERFACE
   {
       /* Welding mode: 0 = Stop, 1 = Start */
       unsigned char _bMode;

       /* Channel configuration: target and feedback parameters */
       CONFIG_WELDING_DETAIL_INFO _tTargetVoltage;
       CONFIG_WELDING_DETAIL_INFO _tFeedingSpeed;
       CONFIG_WELDING_DETAIL_INFO _tWeldingVoltage;
       CONFIG_WELDING_DETAIL_INFO _tWeldingCurrent;

       /* Digital outputs for welding control */
       unsigned char _iArcOnDO;
       unsigned char _iGasOnDO;
       unsigned char _iInchPDO;
       unsigned char _iInchNDO;
       unsigned char _iBlowOutValue;

   } CONFIG_ANALOG_WELDING_INTERFACE, *LPCONFIG_ANALOG_WELDING_INTERFACE;

.. note::
   - ``CONFIG_ANALOG_WELDING_INTERFACE`` integrates both **analog signal configuration** and **digital I/O control**.  
   - ``_tTargetVoltage`` and ``_tWeldingVoltage`` specify the **voltage control characteristics**,  
     while ``_tWeldingCurrent`` manages the **current output regulation**.  
   - ``_iArcOnDO`` and ``_iGasOnDO`` serve as digital triggers for welding start and gas activation.  
   - ``_iBlowOutValue`` can be used to purge the torch post-welding for cooling or cleaning.