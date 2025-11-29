.. _manual_set_tool_digital_output_type:

set_tool_digital_output_type (Manual Mode)
--------------------------------------------------------
This section explains how to use :ref:`set_tool_digital_output_type <set_tool_digital_output_type>` during **Manual (Teach)** operations  
to **define the electrical output type** (PNP or NPN) for a specific **tool (flange) digital output port**.

**Typical usage**

- Configure tool outputs to match the **input logic type** of the connected end-effector or device.  
- Prevent wiring or signal polarity errors during tool integration.  
- Adjust output type for compatibility with different sensor or actuator configurations.

.. Note::

    - The setting affects only the specified port; other tool outputs remain unchanged.

**Example: Set tool digital output type**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Tool or gripper connected to flange port

       // 1) Configure TOOL_DO_1 as PNP (sourcing)
       drfl.set_tool_digital_output_type(1, OUTPUT_TYPE_PNP);
       std::printf("[TOOL_DO_1] Set to PNP mode\n");

       // 2) Configure TOOL_DO_2 as NPN (sinking)
       drfl.set_tool_digital_output_type(2, OUTPUT_TYPE_NPN);
       std::printf("[TOOL_DO_2] Set to NPN mode\n");

       return 0;
   }

**Tips**

- Match the output type (PNP/NPN) with the **input logic** of the connected tool or sensor.  
- Incorrect polarity configuration can prevent signal recognition or cause hardware damage.  
- Set output type before activating signals with :ref:`set_tool_digital_output <set_tool_digital_output>`.  
- Check the controller’s hardware manual for supported output types per flange model.
