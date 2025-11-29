.. _auto_get_tool:

get_tool (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_tool <get_tool>`  
during **Auto (Run)** operations to check the **currently active tool**.  
The active tool determines the robot’s payload, CoG, and dynamics,  
so verifying this value is useful in automated workflows.

This function returns the symbol name of the tool  
that was previously activated using :ref:`set_tool <set_tool>`.

**Typical usage**

- Verify correct tool selection before starting an Auto Mode sequence.  
- Log tool information for production traceability.  
- Ensure recipe-based applications activate the intended tool.  
- Debug unexpected force-control or payload behavior.

.. Note::

    - If no tool has been explicitly set, the controller’s default tool is used.  
    - Combine with ``set_tool()`` in multi-tool automation environments.

**Example: Checking Active Tool Before Auto Operation**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Query the active tool symbol
       std::string activeTool = drfl.get_tool();
       printf("Active Tool: %s\n", activeTool.c_str());

       // Validate expected tool for recipe
       if (activeTool != "RG2_GRIPPER") {
           printf("Warning: Unexpected tool selected.\n");
       }

       return 0;
   }

In this example, the currently active tool symbol is printed  
and validated before executing a recipe-specific Auto task.

**Tips**

- Print the tool name during startup for easier debugging.  
- Use with ``get_tcp()`` to confirm complete end-effector configuration.  
- Useful in systems where tools change depending on recipe or product type.
