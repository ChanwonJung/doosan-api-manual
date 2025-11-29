.. _cb_tonmonitoringdigitalweldingdatacb:

TOnMonitoringDigitalWeldingDataCB
------------------------------------------
This is a callback function for monitoring **digital welding signals** (e.g., welding status, error flags, etc.) from the robot controller during welding operations.  
The callback allows users to track digital feedback, such as welding operation status or safety events.  

The function is triggered automatically when the digital welding data is updated, and since it's called in real-time, it must execute quickly (within **50 msec**).

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringDigitalWeldingDataCB)(const LPMONITORING_DIGITAL_WELDING);

   // internal function definition (real-time)
   DRFL_API void _set_on_monitoring_digital_welding_data(LPROBOTCONTROL pCtrl,
                                                           TOnMonitoringDigitalWeldingDataCB pCallbackFunc);

   // user-facing function
   void set_on_monitoring_digital_welding_data(TOnMonitoringDigitalWeldingDataCB pCallbackFunc)
   {
       _set_on_monitoring_digital_welding_data(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pDigitalWeld
     - :ref:`MONITORING_DIGITAL_WELDING <struct_MONITORING_DIGITAL_WELDING>`
     - -
     - Structure that contains digital welding feedback such as status flags, errors, or binary signal states.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Digital welding data callback
   void OnMonitoringDigitalWeldingDataCB(const LPMONITORING_DIGITAL_WELDING pDigitalWeld)
   {
       if (!pDigitalWeld) return;

       cout << "[DIGITAL WELDING DATA UPDATED]" << endl;

       // Display digital status
       cout << "Welding Status: " << (pDigitalWeld->_iWeldingStatus ? "Active" : "Inactive") << endl;

       // Example: Checking if any errors are reported
       cout << "Error flag: " << (pDigitalWeld->_iErrorFlag ? "Error present" : "No error") << endl;
   }

   int main()
   {
   #if DRCF_VERSION == 2
       CDRFLEx drfl;

       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register the callback for digital welding monitoring
       drfl.set_on_monitoring_digital_welding_data(OnMonitoringDigitalWeldingDataCB);

       // Keep running to monitor updates
       while (true) std::this_thread::sleep_for(std::chrono::milliseconds(100));

       drfl.close_connection();
   #else
       cout << "TOnMonitoringDigitalWeldingDataCB requires DRCF_VERSION == 2." << endl;
   #endif
       return 0;
   }

**Notes**

- This callback provides real-time **digital welding signals**: |br|
  - **Welding status** (active or inactive) |br|
  - **Error flags** or alerts during welding |br|
  - **Status of other digital signals** related to welding process |br|
- Keep callback operations **fast** and **non-blocking** to avoid real-time interruptions.
- **Only available when DRCF_VERSION == 2**.
- Common use cases include: |br|
  - Monitoring welding progress and errors. |br|
  - Triggering alarms or corrective actions if errors are detected. |br|
  - Logging digital states for diagnostics and troubleshooting. |br|
