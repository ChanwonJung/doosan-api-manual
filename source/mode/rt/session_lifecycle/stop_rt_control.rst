.. _stop_rt_control:

stop_rt_control
------------------------------------------
This function stops the **Real-time (RT)** input/output streaming that was previously started  
by :ref:`start_rt_control <start_rt_control>`.  
It safely terminates the real-time data exchange between the PC and the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 590)

.. code-block:: cpp

   bool stop_rt_control() { 
       return _stop_rt_control(_rbtCtrlUDP); 
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
     - Successfully stopped real-time communication.
   * - 0
     - Failed to stop (e.g., stream not active or invalid handle).

**Note**

- Stops both input and output streams that were configured via  
  :ref:`set_rt_control_input <set_rt_control_input>` and :ref:`set_rt_control_output <set_rt_control_output>`.  
- Should always be called before :ref:`disconnect_rt_control <disconnect_rt_control>`.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect and configure
       drfl.connect_rt_control("192.168.137.100", 12347);
       std::string version = "v1.0";
       float period = 0.001f;  // 1 msec = 1 kHz
       int lossCount = 4;

       drfl.set_rt_control_output(version, period, lossCount);
       drfl.start_rt_control();

       // Perform RT operations
       // ...

       // Stop real-time communication
       drfl.stop_rt_control();

       // Finally disconnect
       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function stops the ongoing RT data exchange  
so that resources can be safely released or reconfigured before disconnection.

**Tips**

- Always stop RT streaming before disconnecting the UDP channel.  
- Recommended when changing RT version, period, or communication direction.  
- Prevents residual data packets and ensures clean session closure.
