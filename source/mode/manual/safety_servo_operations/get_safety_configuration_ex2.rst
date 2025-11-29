.. _manual_get_safety_configuration_ex2:

get_safety_configuration_ex2 (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_safety_configuration_ex_v2 <get_safety_configuration_ex_v2>` during **Manual (Teach)** operations  
to retrieve the **robot controller’s active safety configuration parameters** when using **DRCF_VERSION == 2**.  
This function allows users to verify and log current safety settings such as safety zones, emergency stop behavior, and protective limits.

**Typical usage**

- Review and record the **current safety configuration** before performing manual operations.  
- Confirm proper configuration of **safety-rated speed, stop types, or IO-linked safety signals**.  
- Diagnose unexpected protective stops or configuration mismatches.

**Example: Retrieve and print safety configuration**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 1) Retrieve safety configuration (DRCF v2)
       LPSAFETY_CONFIGURATION_EX2 pSafetyCfg = drfl.get_safety_configuration();
       if (!pSafetyCfg) {
           std::printf("[Safety Config] Failed to retrieve configuration.\n");
           return -1;
       }

       // 2) Print basic safety info
       std::printf("[Safety Config v2]\n");
       std::printf("Active Safety Mode : %d\n", pSafetyCfg->_iSafetyMode);
       std::printf("Protective Stop Reset Type : %d\n", pSafetyCfg->_iSafeStopResetType);
       std::printf("Reduced Speed Mode : %d\n", pSafetyCfg->_iReducedModeActive);

       return 0;
   }

**Tips**

- Use this function to **log safety configurations** during system audits or teaching verification.  
- Always confirm consistency between configuration data and real controller settings.  
- Combine with :ref:`set_safety_mode <manual_set_safety_mode>` or :ref:`set_safe_stop_reset_type <manual_set_safe_stop_reset_type>` for complete safety control workflow.  
- For controllers running **DRCF v3**, refer to :ref:`get_safety_configuration_ex2_v3 <manual_get_safety_configuration_ex2_v3>` for updated structure fields.
