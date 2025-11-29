.. _cb_tonmonitoringspeedmodecb:

TOnMonitoringSpeedModeCB
------------------------------------------
This is a callback function for checking the **current velocity (speed) mode** of the robot controller.  
As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnMonitoringSpeedModeCB)(const MONITORING_SPEED);

   // registration API (internal + wrapper)
   DRFL_API void _SetOnMonitoringSpeedMode(LPROBOTCONTROL pCtrl, TOnMonitoringSpeedModeCB pCallbackFunc);
   void SetOnMonitoringSpeedMode(TOnMonitoringSpeedModeCB pCallbackFunc)
   {
       _SetOnMonitoringSpeedMode(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - eSpeedMode
     - :ref:`MONITORING_SPEED <enum_MONITORING_SPEED>`
     - -
     - Current speed mode reported by the controller (e.g., **Low**, **Normal**, **High**).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when the robot’s speed mode changes
   void OnMonitoringSpeedModeCB(const MONITORING_SPEED eSpdMode)
   {
       switch (eSpdMode)
       {
       case MONITORING_SPEED_LOW:
           cout << "[SPEED MODE] Low-speed mode active." << endl;
           break;

       case MONITORING_SPEED_NORMAL:
           cout << "[SPEED MODE] Normal-speed mode active." << endl;
           break;

       case MONITORING_SPEED_HIGH:
           cout << "[SPEED MODE] High-speed mode active." << endl;
           break;

       default:
           cout << "[SPEED MODE] Unknown speed mode: " << static_cast<int>(eSpdMode) << endl;
           break;
       }
   }

   int main()
   {
       CDRFL drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register speed mode monitoring callback
       drfl.set_on_monitoring_speed_mode(OnMonitoringSpeedModeCB);

       // Keep process alive to monitor speed mode events
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback is invoked whenever the robot’s **speed mode** changes.  
- Use this callback to update **UI indicators**, **safety overlays**, or **motion speed profiles**.  
- Avoid time-consuming operations or blocking calls inside the callback (execution < 50 ms).
