.. _manual_set_on_monitoring_ctrl_io_ex2:

set_on_monitoring_ctrl_io_ex2 (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`set_on_monitoring_ctrl_io_ex2 <set_on_monitoring_ctrl_io_ex>` during **Manual (Teach)** operations  
to **register an advanced I/O monitoring callback** that supports extended I/O mapping  
and additional signal channels introduced in **DRCF_VERSION == 3**.

Compared to :ref:`set_on_monitoring_ctrl_io_ex(Manual Mode) <manual_set_on_monitoring_ctrl_io_ex>`,  
this version delivers **enhanced data**, including **flange I/O states**, **high-speed input data**,  
and **user-defined I/O expansion fields**.

**Typical usage**

- Monitor both **control box and flange I/O** simultaneously in real time.  
- Capture extended analog and digital feedback for advanced tool integration.  
- Log detailed I/O events in a background process during manual testing.

.. Note::

    - The callback is triggered after calling ``setup_monitoring_version(1)`` to enable v3 data format.  
    - Contains extended fields for flange I/O and additional analog channels.  

**Example: Register extended I/O monitoring callback (DRCF v3)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   // 1) Define the callback function for extended monitoring
   void OnMonitoringCtrlIOEx2(const LPROBOT_MONITORING_CTRLIO_EX2 pData) {
       std::printf("[I/O Monitor v3] DIN_1: %d, DOUT_1: %d | FLANGE_DI_1: %d, FLANGE_DO_1: %d | ANIN1: %.2f V\n",
                   pData->_digitalInput[0],
                   pData->_digitalOutput[0],
                   pData->_flangeDI[0],
                   pData->_flangeDO[0],
                   pData->_analogInput[0]);
   }

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - setup_monitoring_version(1) called to enable extended data

       // 2) Register extended callback
       drfl.set_on_monitoring_ctrl_io_ex2(OnMonitoringCtrlIOEx2);

       // 3) Maintain loop to receive monitoring updates
       while (true) { std::this_thread::sleep_for(std::chrono::seconds(1)); }

       return 0;
   }

**Tips**

- Always call ``setup_monitoring_version(1)`` **before** registering this callback.  
- Suitable for real-time monitoring dashboards or logging systems.  
- Avoid heavy computations inside callback — use event queues for processing.  