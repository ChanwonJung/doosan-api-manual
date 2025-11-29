.. _cb_tonmonitoringstatecb:

TOnMonitoringStateCB
------------------------------------------
This is a callback function for checking changes in operation state information in the robot controller.  
As the callback function is executed automatically in the case of a specific event,  
a code that requires an excessive execution time (within **50 msec**) within the callback function should not be made.

**Defined in:** ``DRFL.h``  

.. code-block:: cpp

   typedef void (*TOnMonitoringStateCB)(const ROBOT_STATE);

   void SetOnMonitoringState(TOnMonitoringStateCB pCallbackFunc)
   {
       _SetOnMonitoringState(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - eState
     - :ref:`ROBOT_STATE <enum_robot_state>`
     - -
     - Refer to the Definition of Enumeration Type.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   using namespace DRAFramework;

   // Callback function: triggered whenever the robot’s operational state changes
   void OnMonitoringStateCB(const ROBOT_STATE eState)
   {
       switch ((unsigned char)eState)
       {
           case STATE_SAFE_OFF:
               printf("[STATE] SAFE OFF detected. Resetting safety and enabling servo...\n");
               drfl.set_robot_control(CONTROL_RESET_SAFET_OFF);
               break;

           case STATE_IDLE:
               printf("[STATE] Robot is now idle and ready.\n");
               break;

           case STATE_MOVING:
               printf("[STATE] Robot is executing motion.\n");
               break;

           case STATE_STOPPED:
               printf("[STATE] Robot motion stopped.\n");
               break;

           default:
               printf("[STATE] Unknown or transitional state: %d\n", eState);
               break;
       }
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the robot controller
       drfl.open_connection("192.168.137.100");

       // Register callback for robot state monitoring
       drfl.set_on_monitoring_state(OnMonitoringStateCB);

       // Keep program alive to observe state transitions
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Note**

- This callback is automatically invoked by the controller whenever a robot state transition occurs.  
- Avoid heavy computation, blocking calls, or file I/O within the callback (execution time < 50 ms).  
- Typical usage includes servo enabling after `STATE_SAFE_OFF`, logging state changes, or updating GUI indicators.
