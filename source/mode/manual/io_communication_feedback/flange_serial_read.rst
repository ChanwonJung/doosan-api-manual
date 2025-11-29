.. _manual_flange_serial_read:

flange_serial_read (Manual Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_read <flange_serial_read>` during **Manual (Teach)** operations  
to **receive data** from an external serial device connected to the robot’s flange port.

**Typical usage**

- Read response messages from a **gripper**, **sensor**, or other serial tool.  
- Verify communication timing and response content after sending commands.  
- Perform real-time monitoring of tool feedback during manual diagnostics.

.. Note::

    - Must be used after successfully opening the port with :ref:`flange_serial_open <flange_serial_open>`.

**Example: Read response after sending command**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Device connected and port open
       drfl.flange_serial_open(FLANGE_COM1, 115200);

       // 1) Send request command
       const char cmd[] = "STATUS?\r\n";
       drfl.flange_serial_write(strlen(cmd), (char*)cmd, FLANGE_COM1);

       // 2) Read response with timeout (3 sec)
       LPFLANGE_SER_RXD_INFO_EX rx_info = drfl.flange_serial_read(3.0, FLANGE_COM1);
       if (rx_info && rx_info->_nRxdSize > 0) {
           std::printf("[Flange] Received (%d bytes): %s\n",
                       rx_info->_nRxdSize, rx_info->_chRxdData);
       } else {
           std::printf("[Flange] No response or timeout.\n");
       }

       // 3) Close port
       drfl.flange_serial_close(FLANGE_COM1);
       return 0;
   }

**Tips**

- Adjust timeout depending on device response time.  
- Always check ``_nRxdSize`` before accessing the received buffer.  
- If read returns null or empty, verify baud rate, parity, and wiring.  
- Combine with :ref:`flange_serial_write <flange_serial_write>` for full request–response testing.
