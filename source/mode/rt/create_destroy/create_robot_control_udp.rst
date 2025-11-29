.. _create_robot_control_udp:

create_robot_control_udp
------------------------------------------
This function creates a **UDP-based RT (Real-Time) control instance** for high-frequency robot control.  
It allocates a separate handle dedicated to the RT communication channel, independent from the main TCP handle.  
This instance is later used by functions such as :ref:`connect_rt_control <connect_rt_control>` and :ref:`start_rt_control <start_rt_control>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (constructor)

.. code-block:: cpp

   CDRFLEx() { 
       _rbtCtrlUDP = _create_robot_control_udp(); 
   }

**Parameter** |br|
None 

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - LPROBOTCONTROL (Pointer)
     - Returns a handle to the newly created UDP control instance used for RT communication.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       // Constructor automatically creates a UDP RT control instance
       CDRFLEx drfl;

       // The instance can now be used for real-time control operations
       drfl.connect_rt_control("192.168.137.100", 12347);
       drfl.start_rt_control();
   }

In this example, the constructor of `CDRFLEx` automatically initializes the RT UDP instance.  
This instance is then used to establish and operate a real-time control channel.