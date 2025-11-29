.. _close_connection:

close_connection
------------------------------------------
This function disconnects the robot controller from the external PC.  
It safely terminates the established TCP/IP communication session.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 573)

.. code-block:: cpp

    bool close_connection() { return _close_connection(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 1
     - int
     - Success — robot controller disconnected successfully.

**Example**

.. code-block:: cpp

   CDRFLEx drfl;
   drfl.close_connection();

This example safely closes the TCP/IP connection with the robot controller,  
ensuring all communication sessions are properly terminated.