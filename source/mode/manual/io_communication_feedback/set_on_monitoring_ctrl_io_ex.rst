.. _manual_set_on_monitoring_ctrl_io_ex:

set_on_monitoring_ctrl_io_ex (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`set_on_monitoring_ctrl_io_ex <set_on_monitoring_ctrl_io_ex>` during **Manual (Teach)** operations  
to **register a callback function** that receives **real-time I/O monitoring data** from the robot’s control box  
when using API version **DRCF_VERSION == 2**.

**Typical usage**

- Monitor **digital and analog I/O state changes** in real time during manual operation.  
- Debug I/O wiring or verify signal transitions without polling functions repeatedly.  
- Log or visualize I/O changes in a user-defined callback for testing.

.. Note::

    - The callback is triggered whenever any I/O input/output state changes.  
    - Must be registered after establishing a connection with the robot controller.  
    - For newer monitoring API, see :ref:`set_on_monitoring_ctrl_io_ex2(Manual Mode) <manual_set_on_monitoring_ctrl_io_ex2>`.

**Example: Register I/O monitoring callback (DRCF v2)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   // 1) Define the callback function
   void OnMonitoringCtrlIOEx(const LPROBOT_MONITORING_CTRLIO_EX pData) {
       std::printf("[I/O Monitor v2] DIN_1: %d, DOUT_1: %d, ANIN1: %.2f V\n",
                   pData->_digitalInput[0],
                   pData->_digitalOutput[0],
                   pData->_analogInput[0]);
   }

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 2) Register callback
       drfl.set_on_monitoring_ctrl_io_ex(OnMonitoringCtrlIOEx);

       // 3) Keep program alive to receive events
       while (true) { std::this_thread::sleep_for(std::chrono::seconds(1)); }

       return 0;
   }

**Tips**

- The callback executes in a separate monitoring thread — avoid blocking operations.  
- Use lightweight logging or data buffering inside the callback.  
- Unregister or stop monitoring before closing the connection to prevent dangling callbacks.  