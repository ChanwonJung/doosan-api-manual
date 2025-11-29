.. _read_data_rt:

read_data_rt
------------------------------------------
This function reads the **real-time output data** from the robot controller.  
It retrieves the latest output structure containing motion, torque, and system states  
configured by :ref:`set_rt_control_output <set_rt_control_output>`.

Typically used inside a **real-time loop** after :ref:`start_rt_control <start_rt_control>`  
to continuously monitor joint positions, velocities, or external torques.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 597)

.. code-block:: cpp

   LPRT_OUTPUT_DATA_LIST read_data_rt() {
       return _read_data_rt(_rbtCtrlUDP);
   };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - LPRT_OUTPUT_DATA_LIST
     - Pointer to the structure containing all RT output data fields |br| 
       defined by :ref:`get_rt_control_output_data_list <get_rt_control_output_data_list>`.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <cstring>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       std::string version = "v1.0";
       float period = 0.001f;  // 1 msec
       int lossCount = 4;

       // Configure input/output streaming
       drfl.set_rt_control_input(version, period, lossCount);
       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       // Real-time reading loop
       while (true) {
           auto data = drfl.read_data_rt();
           if (!data) continue;

           // Read key fields
           float jointPos[6];
           float jointVel[6];
           float jointTorque[6];

           memcpy(jointPos, data->actual_joint_position, sizeof(float) * 6);
           memcpy(jointVel, data->actual_joint_velocity, sizeof(float) * 6);
           memcpy(jointTorque, data->actual_joint_torque, sizeof(float) * 6);

           std::cout << "Joint 1 Pos: " << jointPos[0]
                     << "  Vel: " << jointVel[0]
                     << "  Torque: " << jointTorque[0] << std::endl;

           // Custom condition to break the loop
           if (jointPos[0] > 30.0f)
               break;

           // Sleep for the RT period
           std::this_thread::sleep_for(std::chrono::milliseconds(1));
       }

       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function continuously retrieves and prints  
the current joint position, velocity, and torque from the real-time stream.

**Tips**

- Always call this function **after** RT streaming is started using :ref:`start_rt_control`.  
- The returned structure pointer updates every RT cycle — avoid holding it persistently.  
- Use ``memcpy`` or direct indexing to copy data safely inside the loop.  
- For visualization, store data into arrays or send to a logger in real time.
