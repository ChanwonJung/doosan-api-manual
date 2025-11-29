.. _cb_tonmonitoringdataexcb:

TOnMonitoringDataExCB
------------------------------------------
This is an extended version of the monitoring callback that provides **enhanced operation data**  
from the robot controller, including detailed information about **joint**, **task**, and **I/O state**. |br|
It functions similarly to :ref:`TOnMonitoringDataCB <cb_tonmonitoringdatacb>` but contains additional fields  
within the :ref:`MONITORING_DATA_EX <struct_MONITORING_DATA_EX>` structure for advanced monitoring or diagnostic applications.  

As the callback function is executed automatically upon a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringDataExCB)(const LPMONITORING_DATA_EX);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_monitoring_data_ex(LPROBOTCONTROL pCtrl, TOnMonitoringDataExCB pCallbackFunc);
   void set_on_monitoring_data_ex(TOnMonitoringDataExCB pCallbackFunc)
   {
       _set_on_monitoring_data_ex(_rbtCtrl, pCallbackFunc);
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
     - :ref:`MONITORING_DATA_EX <struct_MONITORING_DATA_EX>`
     - -
     - Pointer to the extended monitoring data structure containing joint, TCP, torque, and I/O information.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Extended monitoring callback for real-time robot data
   void OnMonitoringDataExCB(const LPMONITORING_DATA_EX pData)
   {
       cout << "[MONITOR-EX] Joint position (deg): ";
       for (int i = 0; i < 6; ++i)
       {
           cout << pData->_tCtrl._tJoint._fActualPos[i];
           if (i < 5) cout << ", ";
       }
       cout << endl;

       // TCP pose (X, Y, Z, Rx, Ry, Rz)
       cout << "[MONITOR-EX] TCP pose: ";
       for (int i = 0; i < 6; ++i)
       {
           cout << pData->_tCtrl._tTask._fActualPos[i];
           if (i < 5) cout << ", ";
       }
       cout << endl;

       // Display I/O state if available
       cout << "[MONITOR-EX] Digital input[0]: "
            << static_cast<int>(pData->_tCtrl._tIo._bDigitalInput[0]) << endl;
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register extended monitoring callback
       drfl.set_on_monitoring_data_ex(OnMonitoringDataExCB);

       // Keep running to receive continuous updates
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- Provides **extended monitoring data** including joint torque, TCP pose, I/O states, and additional sensor feedback.  
- Recommended for advanced applications such as **data logging**, **digital twin visualization**, or **robot diagnostics**.  
- Avoid blocking or heavy computations within the callback (execution < 50 ms).
