.. _cb_tonmonitoringweldingdatacb:

TOnMonitoringWeldingDataCB
------------------------------------------
This is a callback function used for monitoring **welding data** in the robot controller.  
It is specifically triggered during the **welding operation** to track parameters such as welding current, voltage, and other relevant metrics in real-time.

Since this function operates in a real-time environment, it must not contain blocking or long-running operations,  
with execution time ideally kept below **50 msec**.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringWeldingDataCB)(const LPROBOT_WELDING_DATA);

   // internal definition
   DRFL_API void _set_on_monitoring_welding_data(LPROBOTCONTROL pCtrl, TOnMonitoringWeldingDataCB pCallbackFunc);

   // user-callable API (Welding Data Monitoring)
   void set_on_monitoring_welding_data(TOnMonitoringWeldingDataCB pCallbackFunc)
   {
       _set_on_monitoring_welding_data(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pWeldingData
     - :ref:`ROBOT_WELDING_DATA <struct_ROBOT_WELDING_DATA>`
     - -
     - Provides detailed information on the **welding parameters** including current, voltage, and status.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback for monitoring welding data
   void OnMonitoringWeldingDataCB(const LPROBOT_WELDING_DATA pWeldingData)
   {
       if (!pWeldingData) return;

       cout << "[WELDING DATA UPDATED]" << endl;
       cout << "Current: " << pWeldingData->_fWeldingCurrent << " A" << endl;
       cout << "Voltage: " << pWeldingData->_fWeldingVoltage << " V" << endl;
       cout << "Status: " << (pWeldingData->_iStatus == 1 ? "Welding in progress" : "Welding stopped") << endl;
       cout << "-----------------------------------" << endl;
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to robot controller in real-time mode (Welding Data)
       if (!drfl.open_connection_rt("192.168.137.100")) {
           cout << "Failed to connect to controller (RT mode)." << endl;
           return -1;
       }

       // Register callback for welding data monitoring
       drfl.set_on_monitoring_welding_data(OnMonitoringWeldingDataCB);

       // Keep running (real-time loop)
       while (true)
           std::this_thread::sleep_for(std::chrono::milliseconds(100));

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback provides **real-time welding data** such as: |br|
  - Welding **current** (in Amperes) |br|
  - Welding **voltage** (in Volts) |br|
  - Welding **status** (in progress or stopped) |br|
- This callback should only be used when the **controller supports welding operations**.
- **DRCF_VERSION == 2** is required for the callback to function correctly.
- Common applications: |br|
  - Monitoring welding quality in real-time. |br|
  - Logging welding parameters for quality control. |br|
  - Adaptive control based on welding performance (current/voltage feedback). |br|
- Ensure that callback functions complete quickly (within **50 ms**) to avoid performance issues in real-time communication.
