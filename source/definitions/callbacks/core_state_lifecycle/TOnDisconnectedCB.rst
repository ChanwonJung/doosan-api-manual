.. _cb_tondisconnectedcb:

TOnDisconnectedCB
------------------------------------------
This is a callback function for checking if the **connection with the robot controller**  
has been **terminated by an external cause or user intervention**. |br|
As the callback function is executed automatically upon a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnDisconnectedCB)();

   // registration API (internal + wrapper)
   DRFL_API void _SetOnDisconnected(LPROBOTCONTROL pCtrl, TOnDisconnectedCB pCallbackFunc);
   void SetOnDisconnected(TOnDisconnectedCB pCallbackFunc)
   {
       _SetOnDisconnected(_rbtCtrl, pCallbackFunc);
   };

**Parameter** |br|
None

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   #include <thread>
   #include <chrono>

   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when the robot controller connection is lost
   void OnDisconnectedCB()
   {
       cout << "[DISCONNECT] Lost connection with the robot controller." << endl;

       // Try reconnection or safely handle error state
       bool success = drfl.open_connection("192.168.137.100");
       if (success)
           cout << "[RECONNECT] Connection re-established successfully." << endl;
       else
           cout << "[ERROR] Failed to reconnect. Check network or controller power." << endl;
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register disconnection callback
       drfl.set_on_disconnected(OnDisconnectedCB);

       // Keep program alive to handle potential disconnects
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- This callback is invoked when the **network session or controller link** is terminated.  
- Use it to automatically attempt **reconnection**, log the event, or alert the user.  
- Avoid blocking or time-consuming code inside the callback (execution < 50 ms).
