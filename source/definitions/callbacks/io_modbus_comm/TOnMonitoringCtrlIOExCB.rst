.. _cb_tonmonitoringctrliioexcb:

TOnMonitoringCtrlIOExCB
------------------------------------------
This is a callback function for checking **I/O state data** installed in the control box of the robot controller.  
It provides extended I/O information (digital and analog) for controllers that support **DRCF version 2**. |br|
Compared to :ref:`TOnMonitoringCtrlIOCB <cb_tonmonitoringctrliocb>`, this function includes additional I/O metadata.  

As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringCtrlIOExCB)(const LPMONITORING_CTRLIO_EX);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_monitoring_ctrl_io_ex(LPROBOTCONTROL pCtrl, TOnMonitoringCtrlIOExCB pCallbackFunc);
   void set_on_monitoring_ctrl_io_ex(TOnMonitoringCtrlIOExCB pCallbackFunc)
   {
       _set_on_monitoring_ctrl_io_ex(_rbtCtrl, pCallbackFunc);
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
     - :ref:`MONITORING_CTRLIO_EX <struct_MONITORING_CTRLIO_EX>`
     - -
     - Pointer to structure containing extended digital/analog I/O state data.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <chrono>

   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when extended I/O data is updated (requires DRCF_VERSION == 2)
   void OnMonitoringCtrlIOExCB(const LPMONITORING_CTRLIO_EX pCtrlIO)
   {
       cout << "[I/O EX] GPIO state data" << endl;

       // Digital Input
       for (int i = 0; i < NUM_DIGITAL; ++i)
           cout << "DI#" << i << " : " << static_cast<int>(pCtrlIO->_tInput._iActualDI[i]) << endl;

       // Digital Output
       for (int i = 0; i < NUM_DIGITAL; ++i)
           cout << "DO#" << i << " : " << static_cast<int>(pCtrlIO->_tOutput._iActualDO[i]) << endl;

       // Example: Analog I/O (if supported)
       cout << "AI[0]: " << pCtrlIO->_tInput._fActualAI[0]
            << " | AO[0]: " << pCtrlIO->_tOutput._fActualAO[0] << endl;
   }

   int main()
   {
   #if DRCF_VERSION == 2
       CDRFLEx drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register callback for extended I/O monitoring
       drfl.set_on_monitoring_ctrl_io_ex(OnMonitoringCtrlIOExCB);

       // Keep program alive to receive events
       while (true)
           this_thread::sleep_for(chrono::seconds(1));

       drfl.close_connection();
   #else
       cout << "[INFO] TOnMonitoringCtrlIOExCB requires DRCF_VERSION == 2" << endl;
   #endif

       return 0;
   }

**Notes**

- This callback is supported only for **controllers using DRCF version 2**.  
- Provides more detailed I/O information, including analog and status bits, for advanced diagnostics.  
- Ideal for **real-time I/O dashboards**, **diagnostic tools**, or **factory integration systems**.  
- Keep callback logic lightweight (execution time < 50 ms).
