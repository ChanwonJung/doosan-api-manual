.. _servoj_rt:

servoj_rt
------------------------------------------
This function performs **real-time joint position control**  
from an external controller.  
It commands the robot joints to move toward the target position at each RT cycle  
based on the target position, velocity, acceleration, and interpolation time.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 600)

.. code-block:: cpp

   bool servoj_rt(float fTargetPos[NUM_JOINT],
                  float fTargetVel[NUM_JOINT],
                  float fTargetAcc[NUM_JOINT],
                  float fTargetTime) {
       return _servoj_rt(_rbtCtrlUDP, fTargetPos, fTargetVel, fTargetAcc, fTargetTime);
   };

**Caution**

- The current **servoj_rt** command is **still in early implementation**. |br|
  Jerky motion may occur depending on communication latency or jitter.  
- It is recommended to tune ``fTargetTime`` carefully and use a **slow response speed** |br|
  or use :ref:`speedj_rt <speedj_rt>` instead for smoother motion control.  
- When used in high-frequency loops (1 kHz), ensure that ``fTargetTime``  |br|
  is set slightly **greater than the communication cycle time**.

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
     - Target joint position [deg].
   * - fTargetVel
     - float[6]
     - -
     - Target joint velocity [deg/s]. |br|
       If set to **None (-10000)**, velocity is automatically computed from ``fTargetPos``.
   * - fTargetAcc
     - float[6]
     - -
     - Target joint acceleration [deg/s²]. |br|  
       If set to **None (-10000)**, acceleration is automatically computed.
   * - fTargetTime
     - float
     - -
     - Target motion duration [s].

**Note**

- This command is **asynchronous**.  
- The inner motion profile interpolates the path from current state to ``fTargetPos``
  at ``fTargetTime`` using ``fTargetVel`` and ``fTargetAcc``.  
- If ``fTargetTime`` ≤ controller cycle period (~1 ms),  |br|
  the robot moves directly to the target without interpolation.  
- If the next command is not received before reaching ``fTargetPos``,
  the system decelerates according to the global acceleration value.

**Caution**

- The current version is **not synchronized** with the system’s operation speed [%].  
- Jerky motion may occur if the interval between commands exceeds 1 ms.  
- Recommended to set ``fTargetTime ≥ 20×communication_period``  |br|
  or use :ref:`speedj_rt <speedj_rt>` for continuous position control.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success
   * - 0
     - Error (invalid parameter or RT communication issue)

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
       float period = 0.001f; // 1 ms
       int lossCount = 4;

       // Configure RT streaming
       drfl.set_rt_control_input(version, period, lossCount);
       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       float fTargetPos[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       float fTargetVel[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       float fTargetAcc[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       float fTargetTime = 0.008f;

       for (int i = 0; i < 5000; ++i) {
           // Example: oscillate Joint 1
           fTargetPos[0] = 10.f * sin(i * 0.01f);
           drfl.servoj_rt(fTargetPos, fTargetVel, fTargetAcc, fTargetTime);
           std::this_thread::sleep_for(std::chrono::milliseconds(1));
       }

       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

This example demonstrates how to perform continuous joint streaming control  
by repeatedly sending ``servoj_rt`` commands at 1 ms intervals.

**Tips**

- Always run ``servoj_rt`` in a **deterministic loop (1 kHz or lower)**.  
- Use smoothed joint trajectories or low-pass filtered signals to prevent jerk.  
- For Cartesian streaming, use :ref:`servol_rt <servol_rt>` instead.
