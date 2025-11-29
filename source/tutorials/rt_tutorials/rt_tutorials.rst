.. _tutorials_rt:

6.5 RT Tutorials
===================================

The **Real-Time Tutorials** section introduces the Doosan Robot API’s  
real-time control (RT) and monitoring features.  
This mode allows users to stream joint or task-space commands and receive real-time data  
through a dedicated UDP-based communication channel.

These examples demonstrate how to establish an RT connection,  
configure the transmission parameters, start and stop RT control,  
and process real-time feedback data.

**Tutorial Flow**

1. **RT Connection Setup**: Establish the real-time control link.  
2. **RT Output Configuration**: Define control frequency and packet loss tolerance.  
3. **Start / Stop RT Control**: Enable and disable real-time command streaming.  
4. **RT Data Monitoring**: Retrieve and log real-time output data (position, velocity, torque).  
5. **Speed / Torque Commands (Extension)**: Apply real-time speed or torque commands for each joint.  
6. **Unified Safety Handling**: Combine RT loop with safety stop and disconnection recovery.

---------------------------------------
RT Connection Setup
---------------------------------------

**Purpose** |br|
Establish a dedicated UDP communication channel for real-time data exchange  
between the robot controller and an external PC.

.. code-block:: cpp

   // Connect using default IP and port
   Drfl.connect_rt_control();

   // Alternatively, specify a custom host and port
   // Drfl.connect_rt_control("192.168.137.100", 12348);

**Check** |br|
The connection establishes successfully without timeout,  
and the controller responds with RT connection acknowledgment.

---------------------------------------
RT Output Configuration
---------------------------------------

**Purpose** |br| 
Define the update period and packet loss tolerance for RT communication.

.. code-block:: cpp

   std::string version = "v1.0";
   float period = 0.001f;   // 1 ms update period
   int loss_count = 4;      // allowed packet loss count

   Drfl.set_rt_control_output(version, period, loss_count);

**Check**  |br|
The robot accepts the configuration and prepares for RT command streaming.

---------------------------------------
Start / Stop RT Control
---------------------------------------

**Purpose** |br| 
Start and stop the real-time control loop for command transmission.

.. code-block:: cpp

   // Start streaming
   Drfl.start_rt_control();

   // Stop streaming after use
   Drfl.stop_rt_control();

**Check** |br| 
RT control starts successfully, and robot transitions into real-time operation mode.  
Upon stop, the controller safely exits RT mode.

---------------------------------------
RT Data Monitoring
---------------------------------------

**Purpose**  |br|
Access and log real-time joint position, velocity, and torque data.

.. code-block:: cpp

   void OnRTMonitoringData(LPRT_OUTPUT_DATA_LIST tData) {
       static int count = 0;
       if (++count % 500 == 0) {
           printf("timestamp: %.3f\\n", tData->time_stamp);
           printf("q = %.4f %.4f %.4f %.4f %.4f %.4f\\n",
               tData->actual_joint_position[0], tData->actual_joint_position[1],
               tData->actual_joint_position[2], tData->actual_joint_position[3],
               tData->actual_joint_position[4], tData->actual_joint_position[5]);
           printf("q_dot = %.4f %.4f %.4f %.4f %.4f %.4f\\n",
               tData->actual_joint_velocity[0], tData->actual_joint_velocity[1],
               tData->actual_joint_velocity[2], tData->actual_joint_velocity[3],
               tData->actual_joint_velocity[4], tData->actual_joint_velocity[5]);
       }
   }

   // Callback registration
   Drfl.set_on_rt_monitoring_data(OnRTMonitoringData);

**Check** |br| 
RT callback outputs continuous joint position, velocity, and torque data at 1 ms intervals.

---------------------------------------
Speed / Torque Commands (Extension)
---------------------------------------

**Purpose** |br| 
Send real-time speed or torque commands to each joint during RT mode.

.. code-block:: cpp

   float vel[6] = {0.2, 0.0, 0.0, 0.0, 0.0, 0.0};
   float acc[6] = {0.5, 0.5, 0.5, 0.5, 0.5, 0.5};

   // Set joint velocity and acceleration in real-time
   Drfl.set_velj_rt(vel);
   Drfl.set_accj_rt(acc);

   // Optional: Cartesian space velocity control
   Drfl.set_velx_rt(0.2f, 0.2f);
   Drfl.set_accx_rt(0.5f, 0.5f);

**Check** |br| 
The robot follows the specified joint or Cartesian velocity profile  
under real-time control without latency.

---------------------------------------
Unified Safety Handling
---------------------------------------

**Purpose**  |br|
Integrate RT control with safety stop and reconnection logic for stable long-term operation.

.. code-block:: cpp

   void OnDisconnected() {
       printf("[RT] Disconnected from controller. Retrying...\\n");
       while (!Drfl.open_connection("192.168.137.100")) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }
       Drfl.connect_rt_control();
   }

   void OnMonitoringStateCB(const ROBOT_STATE eState) {
       if (eState == STATE_SAFE_STOP || eState == STATE_SAFE_OFF) {
           Drfl.stop_rt_control();
           Drfl.SetRobotControl(CONTROL_SERVO_ON);
           Drfl.start_rt_control();
       }
   }

**Check** |br| 
When a connection or safety stop occurs,  
the RT control automatically resets and resumes without system restart.

.. note::
   - Real-time control requires stable network conditions  
     and a controller version that supports UDP-based RT API.  
   - Always verify connection using :ref:`6.2 Basic Tutorials <tutorials_basic>`  
     and recovery logic from :ref:`6.3 Advanced Tutorials <tutorials_advanced>`  
     before running RT mode.


   