.. _speedl_rt:

speedl_rt
------------------------------------------
This function performs **real-time task-space (TCP) velocity control**  
from an external controller. |br|
It commands the robot’s end-effector velocity and acceleration in Cartesian space  
and is typically used for smooth linear streaming control.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 603)

.. code-block:: cpp

   bool speedl_rt(float fTargetVel[NUM_TASK],
                  float fTargetAcc[NUM_TASK],
                  float fTargetTime) {
       return _speedl_rt(_rbtCtrlUDP, fTargetVel, fTargetAcc, fTargetTime);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetVel
     - float[6]
     - -
     - Target TCP velocity [mm/s, deg/s].
   * - fTargetAcc
     - float[6]
     - -
     - Target TCP acceleration [mm/s², deg/s²]. |br|
       If set to **-10000**, acceleration is automatically computed from the target velocity.
   * - fTargetTime
     - float
     - -
     - Target interpolation duration [s].

**Note**

- **Asynchronous command.**  
- The internal motion profile interpolates to reach *(fTargetVel, fTargetAcc)* over ``fTargetTime``.  
- If ``fTargetTime`` ≤ controller’s cycle (~1 ms), control is performed directly without interpolation.  
- If the next command is not received before ``fTargetTime`` expires, the previous velocity is maintained.  
- If no new command is received for **0.1 s**, a timeout error is raised and motion stops.  
- When exceeding the **global acceleration limit**, the robot halts and an Info message is generated.

**Caution**

- In the current version, this function is **not linked** with Operation Speed [%].  
- Not compatible with **force/compliance control mode**.  
- Not compatible with **DR_VAR_VEL** option near singularities;  |br|
  automatically switches to **DR_AVOID** behavior when detected.  
- For consistent motion, send commands at **1 ms intervals** and  |br|
  ensure ``fTargetTime`` is slightly larger than the communication cycle.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — real-time task velocity command executed.
   * - 0
     - Error — invalid input or RT communication failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect and configure RT streaming
       drfl.connect_rt_control("192.168.137.100", 12347);

       std::string version = "v1.0";
       float period = 0.001f; // 1 ms cycle
       int lossCount = 4;

       drfl.set_rt_control_input(version, period, lossCount);
       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       // Define velocity and acceleration targets
       float fTargetVel[6] = {150.0f, 0.0f, 100.0f, 0.0f, 0.0f, 0.0f};
       float fTargetAcc[6] = {800.0f, 800.0f, 800.0f, 100.0f, 100.0f, 100.0f};
       float fTargetTime = 0.06f; // 60 ms

       // Send real-time TCP velocity command
       if (drfl.speedl_rt(fTargetVel, fTargetAcc, fTargetTime))
           std::cout << "TCP velocity command successful." << std::endl;
       else
           std::cout << "TCP velocity command failed." << std::endl;

       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

This example demonstrates continuous task-space velocity control  
where the TCP moves in a straight-line direction with real-time updates.

**Tips**

- Use ``speedl_rt`` for **Cartesian velocity streaming** with low latency.  
- Combine with feedback from :ref:`read_data_rt <read_data_rt>` to implement closed-loop control.  
- For position-based real-time control, use :ref:`servol_rt <servol_rt>`.
