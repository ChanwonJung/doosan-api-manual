.. _cb_tonmonitoringdatacb:

TOnMonitoringDataCB
------------------------------------------
This is a callback function for checking **robot operation data** that represents the current location,  
joint positions, and task-space pose of the robot controller. |br|
As the callback function is executed automatically upon specific monitoring events,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnMonitoringDataCB)(const LPMONITORING_DATA);

   // registration API (internal + wrapper)
   DRFL_API void _SetOnMonitoringData(LPROBOTCONTROL pCtrl, TOnMonitoringDataCB pCallbackFunc);
   void SetOnMonitoringData(TOnMonitoringDataCB pCallbackFunc)
   {
       _SetOnMonitoringData(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pData
     - :ref:`MONITORING_DATA <struct_MONITORING_DATA>`
     - -
     - Pointer to structure containing current robot joint and task-space information.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback function triggered periodically to provide robot monitoring data
   void OnMonitoringDataCB(const LPMONITORING_DATA pData)
   {
       cout << "[MONITOR] Joint positions (deg): ";
       for (int i = 0; i < 6; ++i)
       {
           cout << pData->_tCtrl._tJoint._fActualPos[i];
           if (i < 5) cout << ", ";
       }
       cout << endl;

       // Display TCP position (mm, deg)
       cout << "[MONITOR] TCP position: X=" << pData->_tCtrl._tTask._fActualPos[0]
            << " Y=" << pData->_tCtrl._tTask._fActualPos[1]
            << " Z=" << pData->_tCtrl._tTask._fActualPos[2] << endl;
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register real-time monitoring callback
       drfl.set_on_monitoring_data(OnMonitoringDataCB);

       // Keep program alive to continuously receive monitoring updates
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback delivers the **same data** as the controller’s current operation state (joint & task position).  
- Used for **real-time visualization**, **data logging**, or **telemetry updates** in applications.  
- Avoid performing long or blocking computations inside the callback (execution < 50 ms).
