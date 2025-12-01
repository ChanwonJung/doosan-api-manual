.. _cb_tonmonitoringaccesscontrolcb:

TOnMonitoringAccessControlCB
------------------------------------------
This is a callback function that monitors **control authority (access control)** changes in the robot controller.  
It is triggered when a control right event occurs, such as **request**, **permission**, or **rejection** of control ownership.

As this function is executed automatically by the controller,  
you should avoid writing code that takes longer than **50 msec** to execute.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnMonitoringAccessControlCB)(const MONITORING_ACCESS_CONTROL);

   // internal definition
   DRFL_API void _SetOnMonitoringAccessControl(LPROBOTCONTROL pCtrl, TOnMonitoringAccessControlCB pCallbackFunc);

   // user-callable API
   void SetOnMonitoringAccessControl(TOnMonitoringAccessControlCB pCallbackFunc)
   {
       _SetOnMonitoringAccessControl(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - eAccCtrl
     - :ref:`MONITORING_ACCESS_CONTROL <enum_monitoring_access_control>`
     - -
     - Represents the access control event state (e.g., REQUEST, PERMISSION, REJECTION).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback executed on access control event
   void OnMonitoringAccessControlCB(const MONITORING_ACCESS_CONTROL eAccCtrl)
   {
       cout << "[ACCESS CONTROL EVENT]" << endl;

       switch (eAccCtrl)
       {
           case MONITORING_ACCESS_CONTROL_REQUEST:
               cout << "Received control transfer request." << endl;

               // Example: reject control transfer request
               drfl.manage_access_control(MANAGE_ACCESS_CONTROL_RESPONSE_NO);
               break;

           case MONITORING_ACCESS_CONTROL_RESPONSE_YES:
               cout << "Control transfer has been permitted." << endl;
               break;

           case MONITORING_ACCESS_CONTROL_RESPONSE_NO:
               cout << "Control transfer has been rejected." << endl;
               break;

           default:
               cout << "Unknown access control state (" << (int)eAccCtrl << ")" << endl;
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

       // Register callback for access control events
       drfl.SetOnMonitoringAccessControl(OnMonitoringAccessControlCB);

       // Keep monitoring
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback is triggered by the robot controller when: |br|
  - Another device or user requests control transfer. |br|
  - The controller grants or denies control authority. |br|
- The parameter :ref:`MONITORING_ACCESS_CONTROL <enum_monitoring_access_control>` indicates the event type. |br|
- Common use cases: |br|
  - Automatically rejecting external control requests. |br|
  - Logging or alerting operators about control state changes. |br|
  - Handling cooperative robot operation environments. |br|
- Callback code should execute within **50 ms** to prevent blocking the controller.
