.. _connect_rt_control:

connect_rt_control
------------------------------------------
This function establishes a **UDP/IP connection** between the external PC and the robot controller  
to enable **Real-time External Control (RT)** communication. |br|
This channel is independent from the original tcp/ip api. It doesn’t care control authority. |br|
For the integrated controller (v3), versions v3.3 or below can be connected to 192.168.137.50. 

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 575)

.. code-block:: cpp

   bool connect_rt_control(string strIpAddr = "192.168.137.100", 
                           unsigned int usPort = 12347) {
       return _connect_rt_control(_rbtCtrlUDP, strIpAddr.c_str(), usPort);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strIpAddr
     - string
     - ``"192.168.137.100"``
     - Target controller IP address for the UDP connection.
   * - usPort
     - unsigned int
     - ``12347``
     - Port number for RT communication (default UDP port).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - The connection is successfully established.
   * - 0
     - The connection attempt failed (e.g., wrong IP/port or controller already in use).

**Typical usage**

- Connect before configuring RT control input/output schema and period.  
- Used as the first step of any **real-time joint or task control loop**.  
- Automatically reconnects to the controller if the UDP instance is newly created.

**Note**

- Real-time external control uses **UDP/IP** communication, not TCP/IP.  
- This channel operates **independently** from the main API connection and cannot control authority or safety locks.  
- For integrated controllers (v3.x), versions **v3.3 or below** may require connecting to **192.168.137.50** instead.  
- Default configuration supports **1-to-1** UDP communication between controller and external PC.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect to the robot controller via UDP for RT control
       if (drfl.connect_rt_control("192.168.137.100", 12347)) {
           std::cout << "RT connection established successfully." << std::endl;

           // Ready to configure input/output schema and start RT streaming
           drfl.start_rt_control();
       } 
       else {
           std::cout << "RT connection failed." << std::endl;
       }

       return 0;
   }

In this example, the function establishes a UDP connection with the controller  
to prepare for real-time motion control or high-frequency data exchange.  
Once connected, users can call :ref:`start_rt_control <start_rt_control>` to begin RT streaming.

**Tips**

- Ensure the robot is powered and reachable on the specified IP before calling this function.  
- Close the RT channel gracefully using :ref:`disconnect_rt_control <disconnect_rt_control>` after operations.  
- When using **Virtual Robot mode**, use the same IP and port to simulate RT data exchange.  
- In real-time applications, this step should be followed by setting the **input/output version and period**  
  using :ref:`set_rt_control_input <set_rt_control_input>` and :ref:`set_rt_control_output <set_rt_control_output>`.
