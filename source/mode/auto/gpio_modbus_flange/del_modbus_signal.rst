.. _auto_del_modbus_signal:

del_modbus_signal (Auto Mode)
------------------------------------------
This section explains how to use :ref:`del_modbus_signal <del_modbus_signal>`  
to remove a previously registered Modbus signal from the controller.

This function is used mainly during configuration or maintenance  
to clean up unused or incorrect Modbus mappings.

**Typical usage**

- Remove outdated Modbus addresses when devices are replaced.  
- Clean up development/testing signals before deployment.  
- Prevent symbol conflicts by deleting unused entries.  
- Maintain clean and consistent Modbus configuration.

.. Note::

    - ``strSymbol`` must match an existing registered Modbus signal.  
    - Do **not** delete a signal that is being used by an active Auto Mode sequence.  
    - Best used during setup or before production runs.

**Example: Removing an Unused Modbus Signal**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Delete an unused Modbus signal
       if (!drfl.del_modbus_signal("CONVEYOR_START")) {
           printf("Failed to delete Modbus signal.\n");
           return -1;
       }

       printf("Modbus signal removed successfully.\n");
       return 0;
   }

In this example, an old Modbus mapping is removed  
to prevent symbol duplication or configuration errors.

**Tips**

- Only delete signals that are confirmed to be unused.  
- Keep Modbus mapping tables organized when managing multiple devices.  
- Use ``get_modbus_input`` and ``set_modbus_output`` to verify active mappings.  
- Follow consistent naming conventions when adding or deleting signals.
