.. _struct_DIGITAL_WELDING_COMM_STATE:

DIGITAL_WELDING_COMM_STATE
==========================

Welding communication link state between robot and digital welding machine (e.g., over EtherNet/IP).

.. list-table::
   :widths: 10 34 18 8 30
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_cWeldingMachineOnline``
     - ``unsigned char``
     - 0~1
     - Welding machine online status (0: Offline, 1: Online)
   * - 1
     - ``_cWeldingEipSlaveState``
     - ``unsigned char``
     - 0~3
     - **EIP/comm state** |br|
       (0: EIP slave offline, 1: Master online |br|
       2: RobotData online, 3: WeldingMachine online)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _DIGITAL_WELDING_COMM_STATE
   {
       unsigned char _cWeldingMachineOnline;   // 0: Offline, 1: Online
       unsigned char _cWeldingEipSlaveState;  // 0: EIP Slave Offline, 1: Master Online, 2: RobotData Online, 3: WeldingMachine Online
   } DIGITAL_WELDING_COMM_STATE, *LPDIGITAL_WELDING_COMM_STATE;