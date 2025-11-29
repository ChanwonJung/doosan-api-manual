.. _manual_flange_serial_write:

flange_serial_write (Manual Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_write <flange_serial_write>` during **Manual (Teach)** operations  
to **transmit data** from the robot’s flange serial port to an external device (e.g., gripper, force sensor, or tool controller).

**Typical usage**

- Send control commands or queries to a connected serial device.  
- Test manual command transmission before automatic DRL integration.  
- Verify that the connected device correctly receives and responds to data.

.. Note::

    - Ensure the port is opened beforehand via :ref:`flange_serial_open <flange_serial_open>`.

**Example: Send simple command to flange device**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <cstring>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Device connected to flange COM1

       // 1) Open port
       if (!drfl.flange_serial_open(FLANGE_COM1, 115200))
           return -1;

       // 2) Prepare and send message
       const char cmd[] = "STATUS?\r\n";
       bool sent = drfl.flange_serial_write(strlen(cmd), (char*)cmd, FLANGE_COM1);
       if (sent)
           std::printf("[Flange] Sent: %s\n", cmd);
       else
           std::printf("[Flange] Transmission failed.\n");

       // 3) Close port
       drfl.flange_serial_close(FLANGE_COM1);
       return 0;
   }

**Tips**

- Append termination characters (e.g., ``\r`` or ``\n``) if the device expects ASCII-based commands.  
- Avoid sending large data blocks continuously in manual mode.  
- Use :ref:`flange_serial_read <flange_serial_read>` afterward to confirm the device’s response.
