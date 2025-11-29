.. _cb_tonmonitoringctrliocb:

TOnMonitoringCtrlIOCB
------------------------------------------
This is a callback function for checking **I/O state data** installed in the control box of the robot controller.  
It provides access to digital and analog input/output values of the robot system in real time. |br|
As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnMonitoringCtrlIOCB)(const LPMONITORING_CTRLIO);

   // registration API (internal + wrapper)
   DRFL_API void _SetOnMonitoringCtrlIO(LPROBOTCONTROL pCtrl, TOnMonitoringCtrlIOCB pCallbackFunc);
   void SetOnMonitoringCtrlIO(TOnMonitoringCtrlIOCB pCallbackFunc)
   {
       _SetOnMonitoringCtrlIO(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pCtrlIO
     - :ref:`MONITORING_CTRLIO <struct_MONITORING_CTRLIO>`
     - -
     - Pointer to structure containing digital and analog I/O state data.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback function triggered when controller I/O state changes
   void OnMonitoringCtrlIOCB(const LPMONITORING_CTRLIO pCtrlIO)
   {
       cout << "[I/O MONITOR] Digital input state:" << endl;

       for (int i = 0; i < NUM_DIGITAL; ++i)
       {
           cout << "DI#" << i << " : " << static_cast<int>(pCtrlIO->_tInput._iActualDI[i]) << endl;
       }

       cout << "[I/O MONITOR] Digital output state:" << endl;
       for (int i = 0; i < NUM_DIGITAL; ++i)
       {
           cout << "DO#" << i << " : " << static_cast<int>(pCtrlIO->_tOutput._iActualDO[i]) << endl;
       }
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register callback for I/O monitoring
       drfl.set_on_monitoring_ctrlio(OnMonitoringCtrlIOCB);

       // Keep program alive to monitor I/O events
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback provides real-time **digital/analog I/O values** from the robot controller.  
- Commonly used to monitor **sensor inputs**, **signal feedback**, or **tool I/O state**.  
- Avoid heavy computation or blocking calls inside the callback (execution < 50 ms).  
- For extended versions with more detailed data, refer to :ref:`TOnMonitoringCtrlIOExCB <cb_tonmonitoringctrliioexcb>` and :ref:`TOnMonitoringCtrlIOEx2CB <cb_tonmonitoringctrliioex2cb>`.
