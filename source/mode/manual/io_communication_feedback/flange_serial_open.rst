.. _manual_flange_serial_open:

flange_serial_open (Manual Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_open <flange_serial_open>` during **Manual (Teach)** operations  
to **establish serial communication** between the robot’s flange port and an external device such as a **gripper, sensor, or tool controller**.

**Typical usage**

- Manually send/receive data to verify tool communication during setup.  
- Check device response and signal integrity before automatic program execution.

.. Note::

    - After opening, you can use :ref:`flange_serial_write <flange_serial_write>` and :ref:`flange_serial_read <manual_flange_serial_read>` for data exchange.

**Example: Open flange serial port and verify communication**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - External serial device connected to flange COM1

       // 1) Open the flange serial port
       bool opened = drfl.flange_serial_open(
           FLANGE_COM1,          // Port number
           115200,               // Baud rate
           BYTE_SIZE_EIGHTBITS,  // Data bits
           PARITY_CHECK_NONE,    // Parity
           STOPBITS_ONE          // Stop bits
       );

       if (!opened) {
           std::printf("[Flange] Failed to open COM1.\n");
           return -1;
       }
       std::printf("[Flange] COM1 opened successfully.\n");

       // 2) (Optional) Write / read test data
       // const char cmd[] = "STATUS?";
       // drfl.flange_serial_write(FLANGE_COM1, cmd, sizeof(cmd));
       // char buf[64] = {0};
       // drfl.flange_serial_read(FLANGE_COM1, buf, sizeof(buf));
       // std::printf("Response: %s\n", buf);

       // 3) Close after test
       drfl.flange_serial_close(FLANGE_COM1);
       std::printf("[Flange] COM1 closed.\n");

       return 0;
   }

**Tips**

- Match **baudrate, parity, and stop bits** exactly with the device’s serial configuration.  
- Use short test messages (e.g., 8–32 bytes) to confirm stable communication.  
- If open fails, check cable wiring (TX/RX swap) or ensure the port is not already active.  
- Always close the port using :ref:`flange_serial_close <flange_serial_close>` before reopening or switching devices.
