.. _auto_flange_serial_close:

flange_serial_close (Auto Mode)
------------------------------------------
This section explains how to use :ref:`flange_serial_close <flange_serial_close>`  
during **Auto (Run)** operations to **close** the previously opened  
flange serial communication channel.

Closing the port ensures that the communication interface is released properly  
and can be reopened later if needed.

**Typical usage**

- Safely close the serial port after data exchange is complete.  
- Reset the communication interface before switching devices.  
- Release the port during shutdown or error recovery routines.  
- Prevent conflicts when using multiple tool-mounted peripherals.

.. Note::

    - Should only be called after ``flange_serial_open`` was used.  
    - Further read/write calls will fail until the port is reopened.  
    - Good practice in long-running or multi-tool systems.

**Example: Closing the Flange Serial Port After Communication**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Example: Close the serial port at the end of a task
       if (!drfl.flange_serial_close()) {
           printf("Failed to close flange serial port.\n");
           return -1;
       }

       printf("Flange serial port closed.\n");
       return 0;
   }

In this example, the robot closes its flange serial port  
after completing end-effector communication.

**Tips**

- Always close ports during system shutdown or before switching tools.  
- Useful for recovering from serial errors or mismatched baud rates.  
- Combine with ``flange_serial_open`` for clean initialization cycles.  
- Helps prevent resource locking in tool-change scenarios.
