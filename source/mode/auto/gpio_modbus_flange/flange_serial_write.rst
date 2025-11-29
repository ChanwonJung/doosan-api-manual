.. _auto_flange_serial_write:

flange_serial_write (Auto Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_write <flange_serial_write>`  
during **Auto (Run)** operations to send data through the robot’s  
**flange-mounted serial communication port**.

This function transmits a byte buffer to a serial-based tool device, enabling  
communication with smart grippers, scanners, torque drivers, and various  
end-effector peripherals.

**Typical usage**

- Send control commands to a smart gripper or driver.  
- Transmit messages to barcode/QR scanners.  
- Send configuration packets to sensor modules.  
- Communicate with serial-based measurement or inspection tools.

.. Note::
 
    - The serial port must be opened first using ``flange_serial_open``.  
    - Data format (ASCII, binary, protocol) must match the device specification.

**Example: Sending a Command to a Smart Gripper**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Ensure serial port is open
       drfl.flange_serial_open(115200);

       // Example command (ASCII): "GRIP_OPEN\n"
       const char cmd[] = "GRIP_OPEN\n";

       if (!drfl.flange_serial_write((unsigned char*)cmd, sizeof(cmd))) {
           printf("Failed to write to serial port.\n");
           return -1;
       }

       printf("Command sent to tool.\n");
       return 0;
   }

In this example, a command string is sent through the flange serial interface  
to control a tool-mounted smart gripper.

**Tips**

- Use correct command packet format according to device protocol.  
- For binary protocols, ensure proper byte ordering and checksum handling.  
- Avoid excessive write frequency to prevent buffer overrun.  
- Combine with ``flange_serial_read`` to implement request–response protocols.
