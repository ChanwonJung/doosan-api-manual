.. _cb_tonmonitoringsafetystatecb:

TOnMonitoringSafetyStateCB
------------------------------------------
This is a callback function that is triggered whenever the **safety state** of the robot controller is updated.  
It allows applications to respond immediately to safety-related changes such as **E-Stop activation**,  
**protective stop**, or **safety fence detection**.

As this callback is executed automatically upon a safety event,  
do not include operations that take longer than **50 msec** inside the function.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringSafetyStateCB)(const SAFETY_STATE);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_monitoring_safety_state(LPROBOTCONTROL pCtrl, TOnMonitoringSafetyStateCB pCallbackFunc);

   // user-callable API
   void set_on_monitoring_safety_state(TOnMonitoringSafetyStateCB pCallbackFunc)
   {
       _set_on_monitoring_safety_state(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - eSafetyState
     - :ref:`SAFETY_STATE <enum_safety_state>`
     - -
     - Indicates the current safety state reported by the robot controller.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when the robot's safety state changes
   void OnMonitoringSafetyStateCB(SAFETY_STATE eState)
   {
       cout << "[SAFETY STATE UPDATED]" << endl;
       switch (eState)
       {
           case SAFETY_STATE_NORMAL:
               cout << "Safety State: NORMAL — Robot operating normally." << endl;
               break;
           case SAFETY_STATE_PROTECTIVE_STOP:
               cout << "Safety State: PROTECTIVE STOP — Protective stop activated." << endl;
               break;
           case SAFETY_STATE_EMERGENCY_STOP:
               cout << "Safety State: EMERGENCY STOP — Immediate stop triggered!" << endl;
               break;
           case SAFETY_STATE_SAFE_STOP:
               cout << "Safety State: SAFE STOP — Motion halted safely." << endl;
               break;
           default:
               cout << "Safety State: UNKNOWN (" << (int)eState << ")" << endl;
               break;
       }
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register callback for monitoring safety state
       drfl.set_on_monitoring_safety_state(OnMonitoringSafetyStateCB);

       // Keep monitoring continuously
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback is triggered whenever the **safety state** changes due to: |br|
  - Emergency stop (E-Stop) |br|
  - Protective stop |br|
  - Safety door/fence signal |br|
  - Safety mode transition (e.g., Manual ↔ Auto) |br|
- The :ref:`SAFETY_STATE <enum_safety_state>` enumeration defines the possible safety conditions.
- Recommended usage: |br|
  - Display real-time safety status |br|
  - Log or alert operators upon stop or hazard events |br|
  - Trigger robot recovery or safe-shutdown sequences |br|
- Ensure callback code executes quickly (**< 50 ms**) to prevent controller delay.
