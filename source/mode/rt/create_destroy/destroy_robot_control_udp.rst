.. _destroy_robot_control_udp:

destroy_robot_control_udp
------------------------------------------
This function releases and destroys the **UDP RT control instance** previously created by  
:ref:`create_robot_control_udp <create_robot_control_udp>`.  
It ensures all allocated resources and sockets associated with the RT instance are properly closed.

This method is automatically invoked by the **destructor** of the CDRFLEx class,  
so manual invocation is generally unnecessary unless explicitly managing memory.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (destructor)

.. code-block:: cpp

   virtual ~CDRFLEx() { 
       _destroy_robot_control_udp(_rbtCtrlUDP);   
   }

**Parameter**

.. list-table::
   :widths: 24 24 52
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Description**
   * - _rbtCtrlUDP
     - ``LPROBOTCONTROL``
     - Handle of the UDP RT control instance to be destroyed.

**Return** |br|
None

**Example**

.. code-block:: cpp

   {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);
       drfl.start_rt_control();

       // RT session automatically cleaned up at scope end
   } // Destructor automatically calls _destroy_robot_control_udp()

In this example, when the `CDRFLEx` object goes out of scope,  
the destructor automatically invokes `_destroy_robot_control_udp()` to clean up the RT instance and release memory safely.

**Tips**

- No need to manually call this in typical use — it is **automatically handled** by the class destructor.  
- Always ensure all RT operations (e.g., `stop_rt_control`, `disconnect_rt_control`) are completed before object destruction.  
- Recommended to use **RAII pattern** (automatic cleanup by object lifecycle).
