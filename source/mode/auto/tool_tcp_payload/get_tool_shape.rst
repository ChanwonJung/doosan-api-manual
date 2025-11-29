.. _auto_get_tool_shape:

get_tool_shape (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_tool_shape <get_tool_shape>`  
during **Auto (Run)** operations to retrieve the **currently active tool shape**  
used for monitoring, simulation, and motion planning.

This function returns the full ``TOOL_SHAPE`` structure associated  
with the active tool.

**Typical usage**

- Validate correct tool geometry before running an Auto Mode sequence.  
- Debug unexpected collision monitoring behavior.  
- Log shape information for process traceability.  
- Confirm which geometry is applied after switching tools.

.. Note::

    - Use after activating a tool via ``set_tool``.  
    - Useful for verifying configuration when multiple tool shapes exist.

**Example: Reading the Active Tool Shape**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       TOOL_SHAPE shape = drfl.get_tool_shape();

       printf("Active Tool Shape:\n");
       printf(" - Type: %d\n", shape.eShape);
       printf(" - Size: %.1f %.1f %.1f (mm)\n",
              shape.fSize[0], shape.fSize[1], shape.fSize[2]);

       return 0;
   }

In this example, the active tool shape is retrieved  
and printed for verification before automated movements.

**Tips**

- Use before Auto Mode motion when multiple tool shapes may be applied.  
- Compare returned values with expected geometry when debugging safety zones.  
- Combine with ``get_tcp()`` for complete end-effector configuration checks.
