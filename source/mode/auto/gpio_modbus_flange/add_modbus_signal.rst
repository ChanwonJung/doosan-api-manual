.. _auto_add_modbus_signal:

add_modbus_signal (Auto Mode)
------------------------------------------
This section explains how to use :ref:`add_modbus_signal <add_modbus_signal>`  
to register a **Modbus signal** on the robot controller for use in  
**Auto (Run)** operations.  

A Modbus signal defines the address, register type, and communication  
parameters for interacting with a Modbus TCP/RTU slave device.

Once registered, the signal can be accessed through  
``set_modbus_output`` or ``get_modbus_input``.

**Typical usage**

- Register PLC coil/register addresses for machine control.  
- Add mappings for industrial I/O modules (remote I/O blocks).  
- Configure communication with sensors, drives, or controllers.  
- Prepare Modbus symbols for use in automated production sequences.

.. Note::

    - ``strSymbol`` must be unique across all Modbus mappings.  
    - Incorrect register settings may cause communication failures.  
    - Use meaningful symbol names for clarity (e.g., “PLC_READY”, “VALVE1_CMD”).  
    - Signals should be registered before Auto Mode cycles begin.

**Example: Registering Modbus Signals for a PLC Module**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Register a coil output (write) signal
       if (!drfl.add_modbus_signal("CONVEYOR_START", 
                                   MODBUS_REG_COIL,  // coil output
                                   0,                // slave ID
                                   100))             // coil address
       {
           printf("Failed to add Modbus signal.\n");
           return -1;
       }

       // Register an input register (read) signal
       drfl.add_modbus_signal("PLC_READY", 
                              MODBUS_REG_INPUT_REGISTER, 
                              0, 
                              10);

       printf("Modbus signals registered.\n");
       return 0;
   }

In this example, two Modbus signals are created:  
one for controlling a conveyor, and another for receiving a PLC-ready signal.

**Tips**

- Register all Modbus signals during system startup or initialization.  
- Verify Modbus slave address, port, and register type before mapping.  
- Use logical symbol names that match your PLC or device documentation.  
- Avoid modifying signal definitions during active Auto Mode execution.
