.. _manual_set_on_monitoring_safety_stop_type:

set_on_monitoring_safety_stop_type (Manual Mode)
-------------------------------------------------------
This section explains how to use :ref:`set_on_monitoring_safety_stop_type <set_on_monitoring_safety_stop_type>` during **Manual (Teach)** operations.  
This function registers a **callback function** that is invoked whenever the robot’s **safety stop type** changes —  
for example, when the robot transitions into an **Emergency Stop (E-Stop)**, **Protective Stop**, or **Safe Stop** condition.

**Typical usage**

- Monitor and log **safety stop events** in real time during manual teaching or system testing.  
- Differentiate between **Protective Stop**, **Emergency Stop**, and **Safe Stop** to perform appropriate recovery actions.  
- Display stop type information on user interfaces for maintenance or safety inspection purposes.

.. Note::

    - The callback is triggered **whenever the safety stop type changes** on the robot controller.  
    - The callback continues to be active until replaced or the connection is closed.  
    - Callback execution should be **non-blocking** — avoid performing time-consuming tasks inside it.

**Example: Register a safety stop type monitoring callback**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   // 1) Define callback function
   void OnSafetyStopTypeChanged(const LPROBOT_MONITORING_SAFETY_STOP_TYPE pStopInfo) {
       std::printf("[Safety Stop Type Changed]\n");
       std::printf(" Stop Type: %d | Trigger Source: %d\n",
                   pStopInfo->_iStopType,
                   pStopInfo->_iTriggerSource);
   }

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 2) Register callback for safety stop type changes
       drfl.set_on_monitoring_safety_stop_type(OnSafetyStopTypeChanged);
       std::printf("[Safety Stop Monitor] Callback registered.\n");

       // 3) Keep the program alive to continuously receive updates
       while (true) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       return 0;
   }

**Tips**

- Typical stop types include: |br|
    - **E-Stop (Emergency Stop)** – immediate torque cutoff |br|
    - **Protective Stop** – triggered by safety sensor or zone violation |br|
    - **Safe Stop** – initiated by safety controller logic or external input  |br| 
- Use this callback for **diagnostic logging** or to trigger visual/auditory alerts in custom safety dashboards.  
- Combine with :ref:`set_on_monitoring_safety_state <manual_set_on_monitoring_safety_state>` for a full picture of real-time safety monitoring.  
- The stop type data can be cross-referenced with :ref:`get_safety_configuration_ex <manual_get_safety_configuration_ex2>`  
  or :ref:`get_safety_configuration_ex_v3 <manual_get_safety_configuration_ex2_v3>` for system-level analysis.  
- Ensure that any recovery procedure (like :ref:`release_protective_stop <release_protective_stop>`)  
  is executed only after verifying the **stop type** and confirming safe conditions.

