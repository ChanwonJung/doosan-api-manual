.. _auto_flange_serial_open:

flange_serial_open (Auto Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_open <flange_serial_open>`  
during **Auto (Run)** operations to open a **serial communication channel**  
on the robot’s flange-mounted serial port.

The flange serial interface allows communication with end-effector devices  
such as smart grippers, torque drivers, barcode scanners, sensors,  
and other serial-based peripherals.

**Typical usage**

- Establish communication with a serial-based smart gripper.  
- Connect to end-effector measurement sensors or barcode readers.  
- Initialize a tool-mounted device before starting Auto Mode cycles.  
- Perform serial I/O exchanges during automated tasks.

.. Note::

    - ``nBaudRate`` must match the device settings (e.g., 9600, 115200).  
    - Serial mode typically uses **8N1** (8 data bits, no parity, 1 stop bit).  
    - Ensure the cable and wiring match the robot's flange serial pinout.  
    - Must be called before ``flange_serial_write`` or ``flange_serial_read``.

**Example: Opening Serial Communication with a Smart Gripper**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Open flange serial port at 115200 baud
       if (!drfl.flange_serial_open(115200)) {
           printf("Failed to open flange serial port.\n");
           return -1;
       }

       printf("Flange serial port opened successfully.\n");
       return 0;
   }

In this example, the flange serial port is opened  
to prepare communication with a tool-mounted peripheral.

**Tips**

- Always open the serial port before attempting read/write operations.  
- Match baud rate and wiring with the connected device’s specifications.  
- Close the port after use to avoid locking the communication channel.  
- Use ``flange_serial_write`` and ``flange_serial_read`` for data exchange.
