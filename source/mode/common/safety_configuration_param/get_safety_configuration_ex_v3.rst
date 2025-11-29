.. _get_safety_configuration_ex_v3:

get_safety_configuration_ex_v3 (DRCF v3)
------------------------------------------
This function retrieves the **current safety configuration** from the controller  
for **DRCF version 3** firmware.

It returns a pointer to ``SAFETY_CONFIGURATION_EX2_V3``, an extended layout that keeps  
v2 fields and adds v3-specific items (e.g., expanded zone/property models and additional options).

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 924)

.. code-block:: cpp

    // DRCF v3
    LPSAFETY_CONFIGURATION_EX2_V3 get_safety_configuration_ex_v3()
    {
        return _get_safety_configuration_ex_v3(_rbtCtrl);
    }

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Type
     - Description
   * - :ref:`LPSAFETY_CONFIGURATION_EX2_V3 <struct_SAFETY_CONFIGURATION_EX2_V3>`
     - Pointer to the current safety configuration (DRCF v3 extended layout).

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx drfl;

        LPSAFETY_CONFIGURATION_EX2_V3 cfg = drfl.get_safety_configuration_ex_v3();
        if (!cfg) {
            std::cerr << "Failed to read safety configuration (DRCF v3)\n";
            return -1;
        }

        // Example: read a few representative fields (names may vary by header version)
        std::cout << "Collision sensitivity: " << cfg->_fCollisionSensitivity << "\n";
        std::cout << "Active Tool Shape: " << cfg->_szActiveToolShape << "\n";
        std::cout << "Safety zone count: " << cfg->_iSafetyZoneCount << "\n";
        return 0;
    }