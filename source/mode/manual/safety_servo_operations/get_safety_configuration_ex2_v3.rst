.. _manual_get_safety_configuration_ex2_v3:

get_safety_configuration_ex2_v3 (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_safety_configuration_ex2_v3 <get_safety_configuration_ex_v3>` during **Manual (Teach)** operations  
to retrieve the **extended safety configuration** of the robot controller when using **DRCF_VERSION == 3**.  
Compared to the v2 structure, this version provides **additional safety fields** such as user-defined safety zones,  
enhanced IO mapping, and collaborative operation parameters.

**Typical usage**

- Inspect and log **comprehensive safety parameters** including newly added safety attributes in DRCF v3.  
- Verify updated configuration of **safe torque off, protective limits, and emergency stop hierarchy**.  
- Confirm system-level integration with external safety devices under the new configuration model.

.. Note::

  - The data is **read-only** and reflects the currently active configuration applied by the controller.  

**Example: Retrieve and display extended safety configuration (DRCF v3)**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 1) Retrieve safety configuration (DRCF v3)
       LPSAFETY_CONFIGURATION_EX2_V3 pSafetyCfgV3 = drfl.get_safety_configuration();
       if (!pSafetyCfgV3) {
           std::printf("[Safety Config v3] Failed to retrieve configuration.\n");
           return -1;
       }

       // 2) Display key configuration fields
       std::printf("[Safety Config v3]\n");
       std::printf("Active Safety Mode        : %d\n", pSafetyCfgV3->_iSafetyMode);
       std::printf("Protective Stop Reset Type: %d\n", pSafetyCfgV3->_iSafeStopResetType);
       std::printf("Reduced Speed Mode Active : %d\n", pSafetyCfgV3->_iReducedModeActive);
       std::printf("Number of Safety Zones    : %d\n", pSafetyCfgV3->_iNumSafetyZones);

       return 0;
   }

**Tips**

- ``get_safety_configuration_ex2_v3()`` provides **richer diagnostic data** for advanced safety environments.  
- Ideal for **validation, commissioning, or system integration** with third-party safety controllers.  
- Recommended to log retrieved configurations before modifying safety parameters with :ref:`set_safety_mode <manual_set_safety_mode>` or related functions.
