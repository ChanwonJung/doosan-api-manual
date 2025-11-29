.. _manual_get_tool_digital_output:

get_tool_digital_output (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_tool_digital_output <get_tool_digital_output>` during **Manual (Teach)** operations  
to **check the current ON/OFF state** of digital output signals from the **tool (flange) connector**.

**Typical usage**

- Verify if output commands sent to the tool port are correctly activated.  
- Check gripper control signals or vacuum valve status during manual debugging.  
- Monitor tool output states before and after using :ref:`set_tool_digital_output <set_tool_digital_output>`.

.. Note::

    - Used mainly for **status verification** after manual or DRL-driven output operations.

**Example: Read digital outputs from tool port**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Tool outputs configured and powered

       // 1) Check tool output states
       bool tdo1 = drfl.get_tool_digital_output(TOOL_DO_1);
       bool tdo2 = drfl.get_tool_digital_output(TOOL_DO_2);

       std::printf("[TOOL_DO_1] = %s\n", tdo1 ? "ON" : "OFF");
       std::printf("[TOOL_DO_2] = %s\n", tdo2 ? "ON" : "OFF");

       return 0;
   }

**Tips**

- Confirm that the tool I/O configuration is set to **output mode**.  
- If outputs remain OFF, ensure external 24V supply and signal mapping are correct.  
- Use in combination with :ref:`set_tool_digital_output <set_tool_digital_output>` to toggle and verify signals.  
- Suitable for **manual gripper open/close** or **vacuum valve activation tests**.
