.. _start_rt_control:

start_rt_control
------------------------------------------
This function starts the **Real-time Control (RT)** data stream over UDP.  
After configuration of input/output schema and connection establishment,  
this function begins sending and receiving real-time data frames between the PC and the controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 589)

.. code-block:: cpp

   bool start_rt_control() { 
       return _start_rt_control(_rbtCtrlUDP); 
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
     - Successfully started real-time streaming.
   * - 0
     - Failed to start (e.g., not connected, version not set).

**Note**

- Starts both **input** and **output** streaming as configured by :ref:`set_rt_control_input <set_rt_control_input>`  
  and :ref:`set_rt_control_output <set_rt_control_output>`.  
- Must be called **after** successful :ref:`connect_rt_control <connect_rt_control>`.  
- Real-time streaming uses UDP and runs independently of TCP-based DRFL APIs.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       std::string version = "v1.0";
       float period = 0.001f;   // 1 msec = 1 kHz
       int lossCount = 4;

       // Configure RT output and start streaming
       drfl.set_rt_control_output(version, period, lossCount);

       if (drfl.start_rt_control())
           std::cout << "RT streaming started." << std::endl;
       else
           std::cout << "Failed to start RT streaming." << std::endl;

       return 0;
   }

In this example, the function activates real-time data exchange between the PC and the controller,  
allowing the application to read and write RT data frames at a 1 kHz update rate.

**Tips**

- Always configure RT input/output versions before starting the stream.  
- Stop streaming using :ref:`stop_rt_control <stop_rt_control>` before disconnecting.  
- High-frequency update (e.g., 0.001 s) may require elevated thread scheduling priority.
