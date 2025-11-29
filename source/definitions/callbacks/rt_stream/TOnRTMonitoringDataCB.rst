.. _cb_tonrtmonitoringdatacb:

TOnRTMonitoringDataCB
------------------------------------------
This is a **real-time callback function** that provides robot operation data in high-frequency intervals  
through the **UDP-based real-time communication interface**. |br|
It allows continuous monitoring of key robot states (joint position, torque, external force, etc.)  
in applications requiring low-latency feedback.

Because this function runs inside a real-time loop,  
you **must not include blocking or heavy operations** (e.g., file I/O, printing, or long computations).  
Execution time should remain within **50 msec**.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnRTMonitoringDataCB)(const LPRT_OUTPUT_DATA_LIST);

   // internal definition
   DRFL_API void _set_on_rt_monitoring_data(LPROBOTCONTROL pCtrl, TOnRTMonitoringDataCB pCallbackFunc);

   // user-callable wrapper (UDP real-time control interface)
   void set_on_rt_monitoring_data(TOnRTMonitoringDataCB pCallbackFunc)
   {
       _set_on_rt_monitoring_data(_rbtCtrlUDP, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pRTData
     - :ref:`RT_OUTPUT_DATA_LIST <struct_RT_OUTPUT_DATA_LIST>`
     - -
     - Pointer to a structure containing **real-time monitoring data** such as joint position, torque, velocity, and status flags.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <iomanip>
   using namespace DRAFramework;
   using namespace std;

   // Real-time data callback (UDP)
   void OnRTMonitoringDataCB(const LPRT_OUTPUT_DATA_LIST pRTData)
   {
       if (!pRTData) return;

       cout << fixed << setprecision(3);
       cout << "[REAL-TIME MONITORING DATA]" << endl;

       // Display joint positions
       cout << "Joint positions [rad]: ";
       for (int i = 0; i < NUM_JOINT; i++)
           cout << setw(8) << pRTData->_tCtrl._fJointPosition[i] << " ";
       cout << endl;

       // Display external torques
       cout << "External torque [Nm]: ";
       for (int i = 0; i < NUM_JOINT; i++)
           cout << setw(8) << pRTData->_tCtrl._fExternalTorque[i] << " ";
       cout << endl;

       // Display tool force
       cout << "Tool force [N]: ";
       for (int i = 0; i < 3; i++)
           cout << setw(8) << pRTData->_tCtrl._fTcpForce[i] << " ";
       cout << endl;

       cout << "------------------------------------" << endl;
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to controller in real-time mode (UDP)
       if (!drfl.open_connection_rt("192.168.137.100")) {
           cout << "Failed to connect to controller (RT mode)." << endl;
           return -1;
       }

       // Register callback for RT monitoring
       drfl.set_on_rt_monitoring_data(OnRTMonitoringDataCB);

       // Keep running (real-time loop)
       while (true)
           std::this_thread::sleep_for(std::chrono::milliseconds(100));

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback provides **high-frequency feedback (≈4 ms cycle)** from the robot controller.
- Typical fields accessible in :ref:`RT_OUTPUT_DATA_LIST <struct_RT_OUTPUT_DATA_LIST>` include: |br|
  - Joint positions, velocities, and torques |br|
  - External TCP force and moment |br|
  - Digital/analog input states |br|
  - System and motion flags |br|
- Recommended use cases: |br|
  - Real-time visualization of robot motion |br|
  - Force-based control or adaptive compliance monitoring |br|
  - Research or control experiments using low-latency feedback |br|
- Keep callback operations **lightweight (< 50 ms)** to maintain UDP stability.
- Use this callback **only when DRCF_VERSION ≥ 2** and **UDP interface** is properly initialized.
