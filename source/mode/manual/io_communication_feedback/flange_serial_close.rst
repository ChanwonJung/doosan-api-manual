.. _manual_flange_serial_close:

flange_serial_close (Manual Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_close <flange_serial_close>` during **Manual (Teach)** operations  
to **terminate an active serial communication session** on a specific flange port after completing manual I/O or sensor communication tests.

**Typical usage**

- Close an open **flange serial port** used for tool, gripper, or sensor communication.  
- Ensure the port is properly released before switching to another device or reopening the port.  
- Prevent serial resource conflicts during repeated manual connection tests.

.. Note::

    - The function should be called after :ref:`flange_serial_open <flange_serial_open>` has successfully established a connection.  
    - Always close the port before powering off the robot or changing communication parameters.  


**Example: Open, communicate, and close flange serial port**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Tool or sensor connected to flange COM1

       // 1) Open the flange serial port (COM1, 115200 bps)
       bool opened = drfl.flange_serial_open(FLANGE_COM1, 115200, FLANGE_PARITY_NONE, 8, 1);
       if (!opened) {
           std::printf("[Flange] Failed to open serial port.\n");
           return -1;
       }
       std::printf("[Flange] Serial port opened successfully.\n");

       // 2) (Optional) Perform data transmission
       // drfl.flange_serial_write(FLANGE_COM1, tx_data, tx_length);
       // drfl.flange_serial_read(FLANGE_COM1, rx_buffer, rx_length);

       std::this_thread::sleep_for(std::chrono::seconds(1)); // simulation delay

       // 3) Close the serial port
       bool closed = drfl.flange_serial_close(FLANGE_COM1);
       if (closed)
           std::printf("[Flange] COM1 closed successfully.\n");
       else
           std::printf("[Flange] Failed to close COM1.\n");

       return 0;
   }

**Tips**

- Always call ``flange_serial_close()`` before reopening the same port to avoid **busy resource errors**.  
- If close fails, verify that all pending read/write operations are finished.  
- For multi-tool setups, manage ports **individually (COM1, COM2)** and close them in reverse order of use.
