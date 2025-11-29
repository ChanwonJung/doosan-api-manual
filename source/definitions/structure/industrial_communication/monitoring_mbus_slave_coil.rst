.. _struct_MONITORING_MBUS_SLAVE_COIL:

MONITORING_MBUS_SLAVE_COIL
==========================

This is a structure information to monitor **Modbus slave coil states**.  
It provides real-time digital signal status such as controller I/O, tool I/O, and robot safety conditions.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_nCtrlDigitalInput``
     - ``unsigned short``
     - -
     - Controller digital input state (bitfield)
   * - 2
     - ``_nCtrlDigitalOutput``
     - ``unsigned short``
     - -
     - Controller digital output state (bitfield)
   * - 4
     - ``_nToolDigitalInput``
     - ``unsigned char``
     - -
     - Tool digital input state
   * - 5
     - ``_nToolDigitalOutput``
     - ``unsigned char``
     - -
     - Tool digital output state
   * - 6
     - ``_nServoOnRobot``
     - ``unsigned char``
     - 0 / 1
     - Servo ON status (1: Active)
   * - 7
     - ``_nEmergencyStopped``
     - ``unsigned char``
     - 0 / 1
     - Emergency stop state
   * - 8
     - ``_nSafetyStopped``
     - ``unsigned char``
     - 0 / 1
     - Safety stop active flag
   * - 9
     - ``_nDirectTeachButtonPress``
     - ``unsigned char``
     - 0 / 1
     - Direct teaching button pressed
   * - 10
     - ``_nPowerButtonPress``
     - ``unsigned char``
     - 0 / 1
     - Power button pressed
   * - 11
     - ``_nSafetyStoppedRequiredRecoveryMode``
     - ``unsigned char``
     - 0 / 1
     - Indicates if safety stop requires recovery mode

Total size: 12 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_MBUS_SLAVE_COIL
   {
       unsigned short  _nCtrlDigitalInput;
       unsigned short  _nCtrlDigitalOutput;
       unsigned char   _nToolDigitalInput;
       unsigned char   _nToolDigitalOutput;
       unsigned char   _nServoOnRobot;
       unsigned char   _nEmergencyStopped;
       unsigned char   _nSafetyStopped;
       unsigned char   _nDirectTeachButtonPress;
       unsigned char   _nPowerButtonPress;
       unsigned char   _nSafetyStoppedRequiredRecoveryMode;

   } MONITORING_MBUS_SLAVE_COIL;
