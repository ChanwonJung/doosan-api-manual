.. _speedj_rt:

speedj_rt
------------------------------------------
This function controls the **joint velocity** from an external controller in real-time.  
It allows smooth joint motion control by continuously streaming target velocity and acceleration values  
through the UDP-based real-time interface.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 602)

.. code-block:: cpp

   bool speedj_rt(float fTargetVel[NUM_JOINT],
                  float fTargetAcc[NUM_JOINT],
                  float fTargetTime) {
       return _speedj_rt(_rbtCtrlUDP, fTargetVel, fTargetAcc, fTargetTime);
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
     - Target joint velocity [deg/s] to be commanded.
   * - fTargetAcc
     - float[6]
     - -
     - Target joint acceleration [deg/s²].  |br|
       If set to **-10000**, acceleration is automatically calculated based on ``fTargetVel``.
   * - fTargetTime
     - float
     - -
     - Duration of target command [s].

**Note**

- **Asynchronous command**.  
- The motion profile is interpolated to reach *(fTargetVel, fTargetAcc)* over ``fTargetTime``.  
- If ``fTargetTime`` ≤ controller cycle (~1 ms), motion is executed without interpolation.  
- If the next command is not received before reaching ``fTargetVel``, the previous velocity is maintained.  
- If the next command is not received for more than **0.1 s**, the system triggers a **timeout stop**.  
- If the **global acceleration limit** is exceeded, motion stops and an Info message is generated.

**Caution**

- In the current version, this function is **not linked with Operation Speed [%]**.  
- Frequent use with too short intervals may cause communication delay or jerky response.  
- Ensure that ``fTargetTime`` > communication cycle for stable performance.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — real-time joint velocity command applied.
   * - 0
     - Error — invalid parameter or communication failure.

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

       // RT configuration
       drfl.set_rt_control_input(version, period, lossCount);
       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       float fTargetVel[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       float fTargetAcc[6] = {1000.f, 1000.f, 1000.f, 1000.f, 1000.f, 1000.f};
       float fTargetTime = 0.05f; // 50 ms

       float time = 0.f;
       int count = 0;

       while (count++ < 3000) {
           // Example: oscillate J1 between ±50 deg/s
           fTargetVel[0] = 50.f * sin(count * 0.01f);
           drfl.speedj_rt(fTargetVel, fTargetAcc, fTargetTime);
           std::this_thread::sleep_for(std::chrono::milliseconds(1));
       }

       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the joint velocity is continuously commanded  
in a sinusoidal profile using ``speedj_rt`` at 1 ms intervals.

**Tips**

- Use ``speedj_rt`` for **smooth and continuous velocity control** of joints.  
- Maintain a fixed update loop (typically 1 kHz) for deterministic motion.  
- For position-based streaming, use :ref:`servoj_rt <servoj_rt>` instead.
