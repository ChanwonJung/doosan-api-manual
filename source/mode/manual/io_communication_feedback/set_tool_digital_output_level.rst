.. _manual_set_tool_digital_output_level:

set_tool_digital_output_level (Manual Mode)
--------------------------------------------------------
This section explains how to use :ref:`set_tool_digital_output_level <set_tool_digital_output_level>` during **Manual (Teach)** operations  
to configure the voltage level of the **tool (flange) digital output lines**.

**Typical usage**

- Select the output power level (e.g., **12 V** or **24 V**) supplied to the tool connector.  
- Match the voltage level with the connected **gripper, valve, or external tool** specifications.  
- Prevent damage caused by voltage mismatch during manual operation.

.. Note::

    - Changing this setting affects **all tool digital outputs (TOOL_DO_1, TOOL_DO_2)** simultaneously.  
    - The output level must match the **power specification** of the connected end-effector.

**Example: Set tool output voltage level**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Tool connected to flange port

       // 1) Set tool output voltage to 24 V
       bool ok = drfl.set_tool_digital_output_level(24);
       std::printf("[Tool Output Level] Set to 24V: %s\n", ok ? "OK" : "FAILED");

       return 0;
   }

**Tips**

- Verify the **gripper or sensor voltage rating** before applying 24 V output.  
- Power level applies globally to all tool outputs — configure before enabling any signal.  
- If setting fails, ensure the controller firmware and tool interface support output voltage selection.
