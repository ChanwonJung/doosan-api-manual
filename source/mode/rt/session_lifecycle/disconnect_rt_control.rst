.. _disconnect_rt_control:

disconnect_rt_control
------------------------------------------
This function terminates the active **UDP real-time control session** established with the robot controller.  
It safely closes the RT communication channel and resets all internal RT configurations.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 576)

.. code-block:: cpp

   bool disconnect_rt_control() { 
       return _disconnect_rt_control(_rbtCtrlUDP); 
   };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Disconnection successful.
   * - 0
     - Disconnection failed (e.g., already disconnected or invalid handle).

**Note**

- Disconnecting automatically resets all RT configurations and internal handles.  
- Recommended after calling :ref:`stop_rt_control <stop_rt_control>` to ensure a clean shutdown.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       drfl.connect_rt_control("192.168.137.100", 12347);
       drfl.start_rt_control();

       // Stop streaming and close the UDP channel
       drfl.stop_rt_control();
       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function safely closes the active UDP RT control session  
and resets internal configurations used for real-time streaming.

**Tips**

- Always stop RT streaming before disconnecting.  
- Use only once per session; the destructor will also release the handle if still active.  
- Reconnect via :ref:`connect_rt_control <connect_rt_control>` to start a new RT session.
