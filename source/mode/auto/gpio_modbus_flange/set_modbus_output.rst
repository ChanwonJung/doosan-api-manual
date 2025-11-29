.. _auto_set_modbus_output:

set_modbus_output (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_modbus_output <set_modbus_output>`  
during **Auto (Run)** operations to write data to a Modbus slave device.  
This function is used to control external industrial equipment such as  
PLC modules, motor drivers, pneumatic controllers, and process automation devices  
that communicate over the Modbus TCP/RTU protocol.

**Typical usage**

- Control external actuators through Modbus registers.  
- Send commands to PLC coils or holding registers.  
- Adjust parameters of sensors or industrial controllers.  
- Synchronize robot actions with Modbus-based equipment.

.. Note::

    - ``strSymbol`` must refer to a Modbus signal registered via ``add_modbus_signal``.  
    - Ensure the Modbus slave connection parameters are correct (IP, port, ID).  
    - Modbus operations should be used carefully inside cycles to avoid latency spikes.

**Example: Writing to a Modbus Register to Start a Conveyor**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Write value '1' to start a conveyor motor via Modbus
       if (!drfl.set_modbus_output("CONVEYOR_START", 1)) {
           printf("Failed to write Modbus output.\n");
           return -1;
       }

       // Perform Auto Mode motion after triggering the conveyor
       float pos[6] = {400.f, 150.f, 300.f, 180.f, 0.f, 0.f};
       drfl.movej(pos, 60.f, 30.f);

       return 0;
   }

In this example, the robot sends a Modbus start signal  
and immediately continues its Auto Mode sequence.

**Tips**

- Use Modbus for industrial automation tasks requiring PLC-like communication.  
- Ensure stable network conditions for Modbus TCP devices.  
- For repeated write operations, ensure timing does not exceed cycle constraints.  
- Use descriptive symbols when registering Modbus signals for clarity.
