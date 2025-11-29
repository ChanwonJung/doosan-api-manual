.. _cb_tonmasteringneedcb:

TOnMasteringNeedCB
------------------------------------------
This is a callback function for checking if the **robot’s axes have been twisted or misaligned**  
due to external force in the robot controller.  
When this event occurs, the robot requires **re-mastering (axis alignment)** through homing.  
The alignment completion can then be verified using the :ref:`TOnHommingCompletedCB <cb_tonhommingcompletedcb>` callback.  

As the callback function is executed automatically in the case of a specific event,  
a code that requires an excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnMasteringNeedCB)();

   // registration API (internal + wrapper)
   DRFL_API void _SetOnMasteringNeed(LPROBOTCONTROL pCtrl, TOnMasteringNeedCB pCallbackFunc);
   void SetOnMasteringNeed(TOnMasteringNeedCB pCallbackFunc)
   {
       _SetOnMasteringNeed(_rbtCtrl, pCallbackFunc);
   };

**Parameter** |br|
None

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when robot mastering (axis alignment) is required
   void OnMasteringNeedCB()
   {
       cout << "[MASTERING] Axis misalignment detected. Starting homing sequence..." << endl;

       // Initiate homing mode for re-alignment of robot axes
       drfl.move_home(true);
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register mastering-needed callback
       drfl.set_on_mastering_need(OnMasteringNeedCB);

       // Keep program alive to monitor events
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback is invoked when the controller detects **axis offset** that requires re-mastering.  
- Use this event to trigger an **automatic homing or alignment process**.  
- Avoid heavy computation or blocking calls inside the callback (execution < 50 ms).  
- Use :ref:`TOnHommingCompletedCB <cb_tonhommingcompletedcb>` to confirm when re-alignment finishes.
