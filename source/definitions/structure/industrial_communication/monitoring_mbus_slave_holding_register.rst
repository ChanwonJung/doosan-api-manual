.. _struct_MONITORING_MBUS_SLAVE_HOILDING_REGISTER:

MONITORING_MBUS_SLAVE_HOILDING_REGISTER
=======================================

This is a structure information to monitor **Modbus slave holding registers**,  
which include analog/digital I/O values, controller version, and robot state/joint information.  
It provides detailed Modbus-based data for both the robot controller and tool interface.

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
     - Controller digital input
   * - 2
     - ``_nCtrlDigitalOutput``
     - ``unsigned short``
     - -
     - Controller digital output
   * - 4
     - ``_nCtrlAnalogInput1``
     - ``unsigned short``
     - -
     - Analog input channel 1 value
   * - 6
     - ``_nCtrlAnalogInput1Type``
     - ``unsigned short``
     - -
     - Analog input 1 type (voltage/current)
   * - 8
     - ``_nCtrlAnalogInput2``
     - ``unsigned short``
     - -
     - Analog input channel 2 value
   * - 10
     - ``_nCtrlAnalogInput2Type``
     - ``unsigned short``
     - -
     - Analog input 2 type (voltage/current)
   * - 12
     - ``_nCtrlAnalogOutput1``
     - ``unsigned short``
     - -
     - Analog output channel 1 value
   * - 14
     - ``_nCtrlAnalogOutput1Type``
     - ``unsigned short``
     - -
     - Analog output 1 type (voltage/current)
   * - 16
     - ``_nCtrlAnalogOutput2``
     - ``unsigned short``
     - -
     - Analog output channel 2 value
   * - 18
     - ``_nCtrlAnalogOutput2Type``
     - ``unsigned short``
     - -
     - Analog output 2 type (voltage/current)
   * - 20
     - ``_nCtrlToolDigitalInput``
     - ``unsigned short``
     - -
     - Tool digital input
   * - 22
     - ``_nCtrlToolDigitalOutput``
     - ``unsigned short``
     - -
     - Tool digital output
   * - 24
     - ``_nGPR``
     - ``unsigned short[128]``
     - -
     - General purpose registers (GPR)
   * - 280
     - ``_nCtrlMajorVer``
     - ``unsigned short``
     - -
     - Controller major version
   * - 282
     - ``_nCtrlMinorVer``
     - ``unsigned short``
     - -
     - Controller minor version
   * - 284
     - ``_nCtrlPatchVer``
     - ``unsigned short``
     - -
     - Controller patch version
   * - 286
     - ``_nRobotState``
     - ``unsigned short``
     - -
     - Robot state code
   * - 288
     - ``_nServoOnRobot``
     - ``unsigned short``
     - -
     - Servo ON state
   * - 290
     - ``_nEmergencyStopped``
     - ``unsigned short``
     - -
     - Emergency stop flag
   * - 292
     - ``_nSafetyStopped``
     - ``unsigned short``
     - -
     - Safety stop flag
   * - 294
     - ``_nDirectTeachButtonPressed``
     - ``unsigned short``
     - -
     - Direct teaching button state
   * - 296
     - ``_nPowerButtonPressed``
     - ``unsigned short``
     - -
     - Power button pressed
   * - 298
     - ``_nJointPosition[6]``
     - ``unsigned short[6]``
     - -
     - Joint position values
   * - 310
     - ``_nJointVelocity[6]``
     - ``unsigned short[6]``
     - -
     - Joint velocity values
   * - 322
     - ``_nJointMotorCurrent[6]``
     - ``unsigned short[6]``
     - -
     - Motor current feedback
   * - 334
     - ``_nJointMotorTemp[6]``
     - ``unsigned short[6]``
     - -
     - Motor temperature
   * - 346
     - ``_nJointTorque[6]``
     - ``unsigned short[6]``
     - -
     - Joint torque feedback
   * - 358
     - ``_nTaskPosition[6]``
     - ``unsigned short[6]``
     - -
     - TCP position
   * - 370
     - ``_nTaskVelocity[6]``
     - ``unsigned short[6]``
     - -
     - TCP velocity
   * - 382
     - ``_nToolOffsetLength[6]``
     - ``unsigned short[6]``
     - -
     - Tool offset length
   * - 394
     - ``_nTaskExternalForce[6]``
     - ``unsigned short[6]``
     - -
     - External force values in task space

Total size: 406 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_MBUS_SLAVE_HOILDING_REGISTER
   {
       unsigned short  _nCtrlDigitalInput;
       unsigned short  _nCtrlDigitalOutput;
       unsigned short  _nCtrlAnalogInput1;
       unsigned short  _nCtrlAnalogInput1Type;
       unsigned short  _nCtrlAnalogInput2;
       unsigned short  _nCtrlAnalogInput2Type;
       unsigned short  _nCtrlAnalogOutput1;
       unsigned short  _nCtrlAnalogOutput1Type;
       unsigned short  _nCtrlAnalogOutput2;
       unsigned short  _nCtrlAnalogOutput2Type;
       unsigned short  _nCtrlToolDigitalInput;
       unsigned short  _nCtrlToolDigitalOutput;
       unsigned short  _nGPR[128];
       unsigned short  _nCtrlMajorVer;
       unsigned short  _nCtrlMinorVer;
       unsigned short  _nCtrlPatchVer;
       unsigned short  _nRobotState;
       unsigned short  _nServoOnRobot;
       unsigned short  _nEmergencyStopped;
       unsigned short  _nSafetyStopped;
       unsigned short  _nDirectTeachButtonPressed;
       unsigned short  _nPowerButtonPressed;
       unsigned short  _nJointPosition[6];
       unsigned short  _nJointVelocity[6];
       unsigned short  _nJointMotorCurrent[6];
       unsigned short  _nJointMotorTemp[6];
       unsigned short  _nJointTorque[6];
       unsigned short  _nTaskPosition[6];
       unsigned short  _nTaskVelocity[6];
       unsigned short  _nToolOffsetLength[6];
       unsigned short  _nTaskExternalForce[6];

   } MONITORING_MBUS_SLAVE_HOILDING_REGISTER;
