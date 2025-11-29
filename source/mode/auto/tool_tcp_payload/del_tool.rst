.. _auto_del_tool:

del_tool (Auto Mode)
------------------------------------------
This section explains how to use :ref:`del_tool <del_tool>`  
during **Auto (Run)** operations or maintenance procedures  
to remove a previously registered **tool configuration** from the controller.

This function is mainly used during system setup or when cleaning up  
unused tool entries, rather than during normal automated production.

**Typical usage**

- Delete outdated or unused end-effector configurations.  
- Remove incorrect tool definitions during commissioning.  
- Clean up tool symbols before deploying a new recipe.  
- Maintain consistency across multi-robot workcells.

.. Note::

    - Do **not** delete a tool that is currently active or used by a running DRL program.  
    - Symbol must exactly match a tool registered using ``add_tool``.  
    - Best used during system initialization or maintenance, not mid-cycle.

**Example: Removing an Unused Tool**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Remove a registered tool
       if (!drfl.del_tool("OLD_END_EFFECTOR")) {
           printf("Failed to delete tool: OLD_END_EFFECTOR\n");
           return -1;
       }

       printf("Tool successfully removed.\n");
       return 0;
   }

In this example, an unused tool configuration is removed  
to keep the system clean and prevent symbol conflicts.

**Tips**

- Avoid deleting tools during motion or active Auto Mode execution.  
- Only remove tools that are no longer required for recipes or operations.  
- Keep tool naming consistent to avoid accidental deletion.
