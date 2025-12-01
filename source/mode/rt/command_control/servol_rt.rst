.. _servol_rt:

servol_rt
------------------------------------------
This function performs **real-time task-space (TCP) position control** from an external controller.  
It commands the robot’s tool center point (TCP) position and orientation at each real-time control cycle,  
based on the target pose, velocity, acceleration, and interpolation time.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 601)

.. code-block:: cpp

   bool servol_rt(float fTargetPos[NUM_TASK],
                  float fTargetVel[NUM_TASK],
                  float fTargetAcc[NUM_TASK],
                  float fTargetTime) {
       return _servol_rt(_rbtCtrlUDP, fTargetPos, fTargetVel, fTargetAcc, fTargetTime);
   };

**Caution**

- The current ``servol_rt`` command is **preliminary**, and jerky motion may occur 
  depending on communication latency or network jitter.  
- It is recommended to **tune the target time (fTargetTime)** and use a **slow response speed**,
  or alternatively use :ref:`speedl_rt <speedl_rt>` for smoother motion.  
- When running at high frequency (1 kHz), ensure that ``fTargetTime`` is slightly **greater**
  than the control cycle time for stable interpolation.

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Target TCP position and orientation [x, y, z, Rx, Ry, Rz] |br| 
       (position in **mm**, rotation in **deg**, using Euler ZYX convention)
   * - fTargetVel
     - float[6]
     - -
     - Target TCP velocity [mm/s, deg/s] |br|
       If set to **-10000**, velocity is automatically calculated from ``fTargetPos``
   * - fTargetAcc
     - float[6]
     - -
     - Target TCP acceleration [mm/s², deg/s²] |br|
       If set to **-10000**, acceleration is automatically computed
   * - fTargetTime
     - float
     - -
     - Target interpolation duration [s]

**Note**

- **Asynchronous command.**  
- The internal motion profile interpolates between current and target states |br| 
  *(fTargetPos, fTargetVel, fTargetAcc)* over ``fTargetTime``.  
- If ``fTargetTime`` ≤ controller’s cycle (~1 ms), interpolation is skipped.  
- If the next command is not received before completion, the motion decelerates |br|  
  using the system’s global acceleration setting.

**Caution**

- The current implementation is **not linked** with Operation Speed [%].  
- Jerky motion may occur if the command interval exceeds 1 ms.  
- Recommended to set ``fTargetTime ≥ 20 × communication_period`` or use ``speedl_rt`` instead.  
- Not compatible with **force/compliance control** or **DR_VAR_VEL** near singularities;  |br|
  the system automatically reverts to **DR_AVOID** mode in such cases.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — command accepted and executed.
   * - 0
     - Error — invalid parameter or RT communication failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       std::string version = "v1.0";
       float period = 0.001f; // 1 ms
       int lossCount = 4;

       // Configure real-time streaming
       drfl.set_rt_control_input(version, period, lossCount);
       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       // Define target TCP pose
       float fTargetPos[6] = {150.f, 0.f, 100.f, 0.f, 0.f, 0.f};
       float fTargetVel[6] = {200.f, 100.f, 100.f, 20.f, 20.f, 20.f};
       float fTargetAcc[6] = {1000.f, 800.f, 800.f, 100.f, 100.f, 100.f};
       float fTargetTime = 0.06f; // 60 ms (recommended ≥ 20 ms)

       // Send real-time task-space motion command
       if (drfl.servol_rt(fTargetPos, fTargetVel, fTargetAcc, fTargetTime))
           std::cout << "Task-space motion command successful." << std::endl;
       else
           std::cout << "Task-space motion failed." << std::endl;

       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

This example shows how to control TCP motion in real time  
by sending continuous task-space commands at 1 ms intervals.

**Tips**

- Use ``servol_rt`` for **precise Cartesian interpolation control** in external systems.  
- Always ensure consistent timing between cycles for smooth motion.  
- For joint-level streaming, refer to :ref:`servoj_rt <servoj_rt>`.
