.. _set_on_rt_monitoring_data:

set_on_rt_monitoring_data
------------------------------------------
This function registers a **callback function** that is triggered whenever  
the robot controller sends **real-time output data** to the external controller.

The callback allows continuous monitoring of robot status (e.g., joint positions, torques)  
during real-time operations, typically used with :ref:`read_data_rt <read_data_rt>`  
and :ref:`start_rt_control <start_rt_control>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 662)

.. code-block:: cpp

   void set_on_rt_monitoring_data(TOnRTMonitoringDataCB pCallbackFunc) {
       _set_on_rt_monitoring_data(_rbtCtrlUDP, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnRTMonitoringDataCB <cb_tonrtmonitoringdatacb>` 
     - Function pointer (callback) to be executed whenever new RT data is received.

**Note**

- The callback function is invoked automatically at the controller’s real-time update rate.  
- Avoid using **non-real-time functions** such as ``printf()`` or file I/O  
  faster than **30 Hz** inside the callback.  
- This callback is primarily used to monitor joint states, motor torque, or task-space feedback  
  during real-time control sessions.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — callback registered successfully.
   * - 0
     - Error — invalid function pointer or UDP connection not established.

**Example**

.. code-block:: cpp

   // Define callback function
   void OnRTMonitoringData(LPRT_OUTPUT_DATA_LIST data) {
       static int count = 0;
       if (++count % 60 == 0) { // Print every 60 cycles (~0.06s at 1kHz)
           printf("Timestamp: %.3lf\n", data->_time_stamp);
           printf("Actual Joint Position: %.3f %.3f %.3f %.3f %.3f %.3f\n",
                  data->_actual_joint_position[0], data->_actual_joint_position[1],
                  data->_actual_joint_position[2], data->_actual_joint_position[3],
                  data->_actual_joint_position[4], data->_actual_joint_position[5]);
           printf("Actual Motor Torque: %.3f %.3f %.3f %.3f %.3f %.3f\n",
                  data->_actual_motor_torque[0], data->_actual_motor_torque[1],
                  data->_actual_motor_torque[2], data->_actual_motor_torque[3],
                  data->_actual_motor_torque[4], data->_actual_motor_torque[5]);
           printf("----------------------------------------\n");
       }
   }

   // Main program
   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       string version = "v1.0";
       float period = 0.001f; // 1 ms
       int losscount = 4;

       // Register callback for RT monitoring
       drfl.set_on_rt_monitoring_data(OnRTMonitoringData);

       // Configure real-time input/output channels
       drfl.set_rt_control_input(version, period, losscount);
       drfl.set_rt_control_output(version, period, losscount);

       // Start real-time control
       drfl.start_rt_control();

       while (true) {
           // Application logic or motion control loop
       }

       drfl.disconnect_rt_control();
       return 0;
   }

This example registers ``OnRTMonitoringData()`` as a callback function  
to monitor joint position and torque in real time while the robot is in RT control mode.

**Tips**

- Recommended for applications that need **continuous state feedback** (e.g., torque control, diagnostics).  
- Keep the callback function **lightweight** and avoid blocking operations.  
- For logging or visualization, offload data processing to a separate thread or process.
