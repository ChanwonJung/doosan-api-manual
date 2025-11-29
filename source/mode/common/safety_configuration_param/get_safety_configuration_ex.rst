.. _get_safety_configuration_ex_v2:

get_safety_configuration_ex (DRCF v2)
------------------------------------------
This function retrieves the **current safety configuration** from the controller  
for **DRCF version 2** firmware.

It returns a pointer to ``SAFETY_CONFIGURATION_EX2``, which includes fields for  
joint/general ranges, collision sensitivity, safety functions, tool/TCP, install pose,  
safety I/O, virtual fence / safe zones, tool shape, cockpit/idle-off/nudge,  
TCP/Tool lists, Modbus list, world relation, speed ratios, safety zones, user coordinates,  
and configurable I/O, etc.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 921)

.. code-block:: cpp

    // DRCF v2
    LPSAFETY_CONFIGURATION_EX2 get_safety_configuration_ex()
    {
        return _get_safety_configuration_ex(_rbtCtrl);
    }

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - :ref:`LPSAFETY_CONFIGURATION_EX2 <struct_SAFETY_CONFIGURATION_EX2>`
     - Pointer to the current safety configuration (DRCF v2 layout).

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx drfl;

        LPSAFETY_CONFIGURATION_EX2 cfg = drfl.get_safety_configuration_ex();
        if (!cfg) {
            std::cerr << "Failed to read safety configuration (DRCF v2)\n";
            return -1;
        }

        // Example: read a few representative fields (names may vary by header version)
        std::cout << "Collision sensitivity: " << cfg->_fCollisionSensitivity << "\n";
        std::cout << "Active TCP: " << cfg->_szActiveTcp << "\n";
        std::cout << "UserCoord count: " << cfg->_iUserCoordCount << "\n";
        return 0;
    }