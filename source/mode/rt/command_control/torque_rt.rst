.. _torque_rt:

torque_rt
------------------------------------------
This function performs **real-time motor torque control** from an external controller.  
It allows direct torque streaming to each joint motor through UDP-based real-time communication.  
This mode is typically used for advanced control algorithms such as **impedance**, **admittance**,  
or **gravity-compensated** torque feedback.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 604)

.. code-block:: cpp

   bool torque_rt(float fMotorTor[NUM_JOINT],
                  float fTargetTime) {
       return _torque_rt(_rbtCtrlUDP, fMotorTor, fTargetTime);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fMotorTor
     - float[6]
     - -
     - Target motor torque [Nm].
   * - fTargetTime
     - float
     - -
     - Target interpolation duration [s].

**Note**

- **Asynchronous command.**  
- The internal controller interpolates the torque profile to reach ``fMotorTor`` over ``fTargetTime``.  
- If ``fTargetTime`` ≤ controller cycle (~1 ms), the command is executed immediately without interpolation.  
- If the next command is not received before reaching the target torque, |br|
  the last torque input is maintained.  
- If no command is received for **0.1 s**, a timeout error occurs and motion stops automatically.

**Caution**

- In **H-series robots**, the **second joint** has a built-in **gravity compensator**.  |br|
  The commanded torque and the compensator’s torque are **summed** internally to generate motion.  |br|
  Therefore, when sending external torque commands,  |br|
  users should compensate using the relationship:  |br|

  :math:`gravity\_torque = (link\_gravity\_torque - gravity\_compensator\_torque)`

- Excessive or unstable torque commands may cause unexpected motion.  
- It is recommended to use **soft torque feedback or compliance control** to ensure safe response.  

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — torque command applied.
   * - 0
     - Error — invalid argument or communication failure.

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
       float period = 0.001f;  // 1 ms
       int lossCount = 4;

       // Configure real-time streaming
       drfl.set_rt_control_input(version, period, lossCount);
       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       float fMotorTor[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       float fTargetTime = 0.01f; // 10 ms

       float q[6] = {0.f};
       float q_dot[6] = {0.f};
       float q_ddot[6] = {0.f};
       float trg_q[6] = {0.f};
       float trg_q_dot[6] = {0.f};
       float kp[6] = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
       float kd[6] = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};

       while (true) {
           // Simulated time increment
           float time = 0.0f;

           // Get current state from real-time data
           memcpy(q, drfl.read_data_rt()->actual_joint_position, sizeof(float) * 6);
           memcpy(q_dot, drfl.read_data_rt()->actual_joint_velocity, sizeof(float) * 6);
           memcpy(q_ddot, drfl.read_data_rt()->gravity_torque, sizeof(float) * 6);

           // Simple gravity + PD torque controller
           for (int i = 0; i < 6; i++) {
               fMotorTor[i] = q_ddot[i] + kp[i] * (trg_q[i] - q[i]) + kd[i] * (trg_q_dot[i] - q_dot[i]);
           }

           drfl.torque_rt(fMotorTor, fTargetTime);

           // Condition to exit
           if (time > 5.0f) {
               drfl.stop_rt_control();
               break;
           }

           std::this_thread::sleep_for(std::chrono::milliseconds(1)); // 1 ms RT loop
       }

       drfl.disconnect_rt_control();
       return 0;
   }

This example demonstrates a **joint-space torque control loop**  
using proportional-derivative (PD) feedback combined with **gravity compensation**.

**Tips**

- Use ``torque_rt`` for **advanced torque-level control** or **compliance-based applications**.  
- Always monitor current joint torque using :ref:`read_data_rt <read_data_rt>` for feedback verification.  
- Apply smooth torque transitions to avoid abrupt mechanical stress.
