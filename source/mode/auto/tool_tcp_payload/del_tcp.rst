.. _auto_del_tcp:

del_tcp (Auto Mode)
------------------------------------------
This section explains how to use :ref:`del_tcp <del_tcp>`  
to remove a previously registered **Tool Center Point (TCP)** from the robot controller.

This function is mainly used during system setup or maintenance to  
clean up unused TCP entries, rather than during normal Auto Mode task execution.

**Typical usage**

- Delete outdated or incorrect TCP definitions.  
- Clean up recipe libraries when tools or reference points change.  
- Remove temporary TCPs used for calibration or development.  
- Maintain a clean, consistent controller configuration.

.. Note::

    - Do **not** delete a TCP that is currently active.  
    - ``strSymbol`` must exactly match the registered TCP name.  
    - Typically used during commissioning or before production runs.

**Example: Removing an Unused TCP**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Delete a TCP named "TCP_TEST_POINT"
       if (!drfl.del_tcp("TCP_TEST_POINT")) {
           printf("Failed to delete TCP.\n");
           return -1;
       }

       printf("TCP successfully removed.\n");
       return 0;
   }

In this example, an unused TCP entry is removed  
to prevent naming conflicts and maintain a clean setup.

**Tips**

- Avoid deleting TCPs during motion or Auto Mode operations.  
- Remove outdated points when updating grippers or end-effector geometry.  
- Always check active TCP with ``get_tcp()`` before deletion.
