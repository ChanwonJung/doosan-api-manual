.. _cb_tonmonitoringrobotsystemcb:

TOnMonitoringRobotSystemCB
------------------------------------------
This is a callback function that is executed when the **robot operation system** changes in the robot controller.  
It allows you to monitor transitions between system modes such as **Real Robot**, **Virtual Robot**, or **Simulation**.  

Since this callback is automatically executed by the controller on a system change event,  
you should avoid performing long or blocking operations (execution time should be within **50 msec**).

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnMonitoringRobotSystemCB)(const ROBOT_SYSTEM);

   // internal definition
   DRFL_API void _set_on_monitoring_robot_system(LPROBOTCONTROL pCtrl, TOnMonitoringRobotSystemCB pCallbackFunc);

   // user-callable wrapper
   void set_on_monitoring_robot_system(TOnMonitoringRobotSystemCB pCallbackFunc)
   {
       _set_on_monitoring_robot_system(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - eRobotSystem
     - :ref:`ROBOT_SYSTEM <enum_robot_system>`
     - -
     - Indicates the current robot operation system (e.g., REAL_ROBOT, VIRTUAL_ROBOT, SIMULATION).

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback executed when robot operation system changes
   void OnMonitoringRobotSystemCB(const ROBOT_SYSTEM eSystem)
   {
       cout << "[ROBOT SYSTEM STATE UPDATED]" << endl;

       switch (eSystem)
       {
           case ROBOT_SYSTEM_REAL:
               cout << "Robot system: REAL ROBOT — connected to physical hardware." << endl;
               break;

           case ROBOT_SYSTEM_VIRTUAL:
               cout << "Robot system: VIRTUAL ROBOT — operating in virtual mode." << endl;
               break;

           case ROBOT_SYSTEM_SIMULATION:
               cout << "Robot system: SIMULATION — running simulation environment." << endl;
               break;

           default:
               cout << "Robot system: UNKNOWN (" << (int)eSystem << ")" << endl;
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

       // Register callback for robot system monitoring
       drfl.set_on_monitoring_robot_system(OnMonitoringRobotSystemCB);

       // Keep monitoring loop alive
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- Triggered when the controller changes between: |br|
  - **Real Robot (ROBOT_SYSTEM_REAL)** |br|
  - **Virtual Robot (ROBOT_SYSTEM_VIRTUAL)** |br|
  - **Simulation (ROBOT_SYSTEM_SIMULATION)** |br|
- Common uses: |br|
  - Displaying current system mode in UI |br|
  - Logging system transitions |br|
  - Automatically adapting control logic to match system type |br|
- Execution time inside the callback must be short (**< 50 ms**).
