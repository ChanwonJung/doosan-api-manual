.. _auto_get_tcp:

get_tcp (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_tcp <get_tcp>`  
during **Auto (Run)** operations to retrieve the symbol name  
of the **currently active Tool Center Point (TCP)**.

The active TCP determines the reference position/orientation used  
for linear moves, force control, and task-space calculations.  
Verifying this value is important in automated workflows to ensure  
the correct operation point is being used.

**Typical usage**

- Confirm the correct TCP is selected before Auto Mode motion.  
- Log TCP usage for traceability in production environments.  
- Debug misalignments caused by unexpected TCP activation.  
- Validate recipe settings for multi-tool applications.

.. Note::

    - If no TCP is explicitly set, the default TCP may be used.  
    - Combine with ``set_tcp`` in applications where multiple TCPs are needed.

**Example: Checking Active TCP Before Starting a Task**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Query currently active TCP
       std::string activeTcp = drfl.get_tcp();
       printf("Active TCP: %s\n", activeTcp.c_str());

       // Validate expected TCP for the upcoming recipe
       if (activeTcp != "TCP_GRIPPER_CENTER") {
           printf("Warning: Unexpected TCP is active.\n");
       }

       return 0;
   }

In this example, the active TCP is retrieved and compared  
against an expected value to prevent incorrect automated behavior.

**Tips**

- Print the active TCP at program start for easier debugging.  
- Useful for multi-TCP operations such as palletizing or assembly.  
- Combine with ``get_tool()`` to verify the complete end-effector configuration.
