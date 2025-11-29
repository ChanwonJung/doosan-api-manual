.. _system_shut_down:

system_shut_down
------------------------------------------
This function shuts down the connected robot controller system.  
It is typically used to safely power down the controller after all robot operations  
and background tasks have been completed.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 991)

.. code-block:: cpp

    bool system_shut_down() { return _system_shut_down(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to shut down the robot controller system.
   * - 1
     - int
     - Success — the robot controller has been successfully shut down.

**Example**

.. code-block:: cpp

   // Ensure robot motion is stopped before shutdown
   drfl.stop();

   // Shutdown the controller system
   bool bShutdown = drfl.system_shut_down();
   if (bShutdown) {
       // Successfully shut down the robot system
       // Proceed with application termination
   } else {
       // Handle shutdown failure
   }

This example safely stops robot motion before calling **system_shut_down()**,  
then proceeds with controller shutdown and application termination.
