.. _cb_tonmonitoringanalogweldingdatacb:

TOnMonitoringAnalogWeldingDataCB
------------------------------------------
This is a callback function for monitoring **analog welding signals** (e.g., current/voltage analog feedback) from the robot controller during welding operations.  
Because it is invoked automatically on each update, avoid heavy work in the handler and keep execution within **50 msec**.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringAnalogWeldingDataCB)(const LPMONITORING_ALALOG_WELDING);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_monitoring_analog_welding_data(LPROBOTCONTROL pCtrl,
                                                        TOnMonitoringAnalogWeldingDataCB pCallbackFunc);
   void set_on_monitoring_analog_welding_data(TOnMonitoringAnalogWeldingDataCB pCallbackFunc)
   {
       _set_on_monitoring_analog_welding_data(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pAnalogWeld
     - :ref:`MONITORING_ALALOG_WELDING <struct_ROBOT_ALALOG_WELDING_DATA>`
     - -
     - Pointer to structure holding analog welding feedback (e.g., current/voltage channels, status).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <iomanip>
   using namespace DRAFramework;
   using namespace std;

   // Analog welding feedback callback (DRCF v2)
   void OnMonitoringAnalogWeldingDataCB(const LPMONITORING_ALALOG_WELDING pAnalogWeld)
   {
       if (!pAnalogWeld) return;

       cout << fixed << setprecision(2);
       cout << "[WELD-ANALOG] updated" << endl;

       // Example access (field names may vary by firmware; adjust to your struct definition)
       // Current/Voltage analog readings
       cout << "Current(A): " << pAnalogWeld->_fCurrent << " | "
            << "Voltage(V): " << pAnalogWeld->_fVoltage << endl;

       // If multiple channels exist, print a few as an example
       // for (int ch = 0; ch < pAnalogWeld->_iNumChannels; ++ch)
       //     cout << "CH" << ch << ": " << pAnalogWeld->_fChannel[ch] << endl;
   }

   int main()
   {
   #if DRCF_VERSION == 2
       CDRFLEx drfl;

       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register analog welding monitoring callback
       drfl.set_on_monitoring_analog_welding_data(OnMonitoringAnalogWeldingDataCB);

       // Keep running to receive updates
       while (true) std::this_thread::sleep_for(std::chrono::milliseconds(100));

       drfl.close_connection();
   #else
       cout << "TOnMonitoringAnalogWeldingDataCB requires DRCF_VERSION == 2." << endl;
   #endif
       return 0;
   }

**Notes**

- Use for **quality monitoring**, **traceability logging**, or **adaptive control** based on analog welding feedback.  
- Keep handler code lightweight (no blocking I/O, minimal console prints) to maintain controller responsiveness.
