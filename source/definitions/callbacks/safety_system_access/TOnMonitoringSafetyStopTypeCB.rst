.. _cb_tonmonitoringsafetystoptypecb:

TOnMonitoringSafetyStopTypeCB
------------------------------------------
This is a callback function that is triggered when the **safety stop type** of the robot controller changes.  
It allows the user to detect and handle different safety stop conditions, such as **E-Stop**, **Protective Stop**,  
or **Auto Safety Stop** triggered by the safety system or external devices.

As this function is executed automatically on a safety event,  
it must not include any code that requires excessive execution time (within **50 msec**).

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringSafetyStopTypeCB)(const unsigned char);

   // internal definition
   DRFL_API void _set_on_monitoring_safety_stop_type(LPROBOTCONTROL pCtrl, TOnMonitoringSafetyStopTypeCB pCallbackFunc);

   // user-callable wrapper
   void set_on_monitoring_safety_stop_type(TOnMonitoringSafetyStopTypeCB pCallbackFunc)
   {
       _set_on_monitoring_safety_stop_type(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - iSafetyStopType
     - ``unsigned char``  
     - -
     - Indicates the **type of safety stop** detected by the robot controller.  
       Possible values include Emergency Stop, Protective Stop, and Auto Safety Stop.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback invoked when safety stop type is updated
   void OnMonitoringSafetyStopTypeCB(const unsigned char iStopType)
   {
       cout << "[SAFETY STOP TYPE UPDATED]" << endl;

       switch (iStopType)
       {
           case SAFETY_STOP_TYPE_NONE:
               cout << "Stop Type: NONE — No active safety stop." << endl;
               break;

           case SAFETY_STOP_TYPE_PROTECTIVE:
               cout << "Stop Type: PROTECTIVE STOP — Triggered by protective device or safety fence." << endl;
               break;

           case SAFETY_STOP_TYPE_EMERGENCY:
               cout << "Stop Type: EMERGENCY STOP — Emergency stop activated!" << endl;
               break;

           case SAFETY_STOP_TYPE_AUTO:
               cout << "Stop Type: AUTO SAFETY STOP — Automatically stopped by system conditions." << endl;
               break;

           default:
               cout << "Stop Type: UNKNOWN (" << (int)iStopType << ")" << endl;
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

       // Register callback for safety stop type monitoring
       drfl.set_on_monitoring_safety_stop_type(OnMonitoringSafetyStopTypeCB);

       // Keep monitoring loop alive
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback is triggered whenever the **safety stop classification** changes.  
- This includes: |br|
  - **Emergency Stop (E-Stop)** |br|
  - **Protective Stop** |br|
  - **Auto Safety Stop** |br|
- Typical use cases: |br|
  - Displaying current safety stop cause in a user interface |br|
  - Logging stop events for diagnostics |br|
  - Initiating recovery or alarm reset sequences |br|
- Keep callback logic minimal (execution < 50 ms) to avoid real-time performance degradation.
