.. _write_data_rt:

write_data_rt
------------------------------------------
This function writes **real-time input data** from the external controller to the robot controller.  
It is used for transmitting external signals such as force/torque feedback,  
digital I/O, and analog I/O in real-time external control mode.

Although currently limited in public applications,  
it is designed for future **collaborative control** integration with external systems.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 598)

.. code-block:: cpp

   bool write_data_rt(float fExternalForceTorque[NUM_JOINT],
                      int iExternalDI,
                      int iExternalDO,
                      float fExternalAnalogInput[6],
                      float fExternalAnalogOutput[6]) {
       return _write_data_rt(_rbtCtrlUDP,
                             fExternalForceTorque,
                             iExternalDI,
                             iExternalDO,
                             fExternalAnalogInput,
                             fExternalAnalogOutput);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fExternalForceTorque
     - float[6]
     - -
     - External force/torque input for each joint.  |br|
       Used when applying external sensor feedback.
   * - iExternalDI
     - unsigned short
     - -
     - External digital input data (16 channels).
   * - iExternalDO
     - unsigned short
     - -
     - External digital output data (16 channels).
   * - fExternalAnalogInput
     - float[6]
     - -
     - External analog input values (up to 6 channels).
   * - fExternalAnalogOutput
     - float[6]
     - -
     - External analog output values (up to 6 channels).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Successfully transmitted real-time input data.
   * - 0
     - Failed to transmit (communication error or not in RT mode).

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect and start RT communication
       drfl.connect_rt_control("192.168.137.100", 12347);
       drfl.set_rt_control_input("v1.0", 0.001f, 4);
       drfl.set_rt_control_output("v1.0", 0.001f, 4);
       drfl.start_rt_control();

       // Define external data arrays
       float fExternalForceTorque[6] = {100.f, 100.f, 100.f, 100.f, 100.f, 100.f};
       int iExternalDI = 1;
       int iExternalDO = 2;
       float fExternalAnalogInput[6]  = {0.f, 0.f, 100.f, 100.f, 100.f, 100.f};
       float fExternalAnalogOutput[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};

       // Send external control data
       if (drfl.write_data_rt(fExternalForceTorque, iExternalDI, iExternalDO,
                              fExternalAnalogInput, fExternalAnalogOutput))
           std::cout << "External RT data written successfully." << std::endl;
       else
           std::cout << "Failed to write RT data." << std::endl;

       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function transmits simulated external I/O and force data  
to the robot controller through the real-time UDP interface.

**Tips**

- Call write_data_rt **after** RT streaming has started using :ref:`start_rt_control`.  
- Values in ``fExternalForceTorque`` or I/O arrays should be updated continuously within the control loop.  
- In most use cases, this API will be utilized for **future sensor fusion** or **external cooperative control**.
