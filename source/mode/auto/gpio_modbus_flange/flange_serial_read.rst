.. _auto_flange_serial_read:

flange_serial_read (Auto Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_read <flange_serial_read>`  
during **Auto (Run)** operations to receive data from a device connected to the  
robot’s flange-mounted serial port.

This function reads a specified number of bytes into a buffer, allowing  
the robot to process responses or sensor readings from the tool.

**Typical usage**

- Receive status feedback from a smart gripper.  
- Read barcode/QR scan data from a serial scanner.  
- Acquire sensor data from tool-mounted measurement devices.  
- Implement handshake/acknowledgment logic with external peripherals.

.. Note::

    - The serial port must be opened beforehand with ``flange_serial_open``.  
    - Many devices require request–response timing considerations.

**Example: Reading a Response From a Tool Device**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <cstring>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Open serial port
       drfl.flange_serial_open(115200);

       // Receive buffer
       unsigned char buff[128];
       memset(buff, 0, sizeof(buff));

       // Read up to 128 bytes
       int readSize = drfl.flange_serial_read(buff, 128);

       if (readSize <= 0) {
           printf("No data received.\n");
           return -1;
       }

       printf("Received (%d bytes): %s\n", readSize, buff);
       return 0;
   }

In this example, data is read from the tool after a previous write operation,  
allowing the robot to receive device responses in Auto Mode.

**Tips**

- Allocate sufficient buffer size for expected messages.  
- Some devices require a delay after write before attempting to read.  
- Use polling or loop-based reads for larger or streaming data.  
- Combine with serial-write to implement command–response or handshake protocols.
