.. _cb_tonmonitoringctrliioex2cb:

TOnMonitoringCtrlIOEx2CB
------------------------------------------
This is the **latest extended** controller I/O monitoring callback for **DRCF version 3**.  
Compared to :ref:`TOnMonitoringCtrlIOCB <cb_tonmonitoringctrliocb>` and
:ref:`TOnMonitoringCtrlIOExCB <cb_tonmonitoringctrliioexcb>`, it delivers the v3-format
I/O payload (:ref:`MONITORING_CTRLIO_EX2 <struct_MONITORING_CTRLIO_EX2>`) and is invoked only after enabling the
new monitoring format.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringCtrlIOEx2CB)(const LPMONITORING_CTRLIO_EX2);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_monitoring_ctrl_io_ex2(LPROBOTCONTROL pCtrl, TOnMonitoringCtrlIOEx2CB pCallbackFunc);

   #elif DRCF_VERSION == 3
       /* Latest version. callbacks invoked after setup_monitoring_version(1) */
       void set_on_monitoring_ctrl_io_ex(TOnMonitoringCtrlIOEx2CB pCallbackFunc)
       {
           _set_on_monitoring_ctrl_io_ex2(_rbtCtrl, pCallbackFunc);
       };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - pCtrlIOEx2
     - :ref:`MONITORING_CTRLIO_EX2 <struct_MONITORING_CTRLIO_EX2>`
     - -
     - Pointer to v3 extended I/O structure (digital/analog I/O plus v3 metadata).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <chrono>

   using namespace DRAFramework;

   // EX2 I/O monitoring callback (DRCF v3)
   void OnMonitoringCtrlIOEx2CB(const LPMONITORING_CTRLIO_EX2 pEx2)
   {
       // Print first few digital inputs/outputs as an example
       std::cout << "[I/O EX2] DI0..3: "
                 << (int)pEx2->_tInput._iActualDI[0] << ", "
                 << (int)pEx2->_tInput._iActualDI[1] << ", "
                 << (int)pEx2->_tInput._iActualDI[2] << ", "
                 << (int)pEx2->_tInput._iActualDI[3] << std::endl;

       std::cout << "[I/O EX2] DO0..3: "
                 << (int)pEx2->_tOutput._iActualDO[0] << ", "
                 << (int)pEx2->_tOutput._iActualDO[1] << ", "
                 << (int)pEx2->_tOutput._iActualDO[2] << ", "
                 << (int)pEx2->_tOutput._iActualDO[3] << std::endl;

       // Keep logic lightweight (<50 ms)
   }

   int main()
   {
   #if DRCF_VERSION == 3
       CDRFLEx drfl;

       if (!drfl.open_connection("192.168.137.100")) {
           std::cout << "Failed to connect.\n";
           return -1;
       }

       // Enable v3 monitoring payloads; EX2 callbacks will fire after this
       drfl.setup_monitoring_version(1);

       // Register the EX2 callback
       drfl.set_on_monitoring_ctrl_io_ex(OnMonitoringCtrlIOEx2CB);

       // Alive loop
       while (true) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
   #else
       std::cout << "TOnMonitoringCtrlIOEx2CB requires DRCF_VERSION == 3.\n";
   #endif
       return 0;
   }

**Notes**

- Use this when targeting **v3 controllers** needing richer I/O telemetry.  
- Provide a fallback to :ref:`TOnMonitoringCtrlIOExCB <cb_tonmonitoringctrliioexcb>` (v2) or
  :ref:`TOnMonitoringCtrlIOCB <cb_tonmonitoringctrliocb>` (legacy) for broader compatibility.  
- Avoid heavy computation or blocking calls inside the callback (execution < 50 ms).
