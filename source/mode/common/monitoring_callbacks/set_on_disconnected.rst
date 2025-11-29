.. _set_on_disconnected:

set_on_disconnected
------------------------------------------
This is a function for registering the callback function that automatically checks  
if the connection with the robot controller has been terminated by external force or user.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 655)

.. code-block:: cpp

    void set_on_disconnected(TOnDisconnectedCB pCallbackFunc) { 
        _set_on_disconnected(_rbtCtrl, pCallbackFunc); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnDisconnectedCB <cb_tondisconnectedcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnDisconnectedCB()
   {
       // Needs the reconnection of the robot controller and error handling
   }

   int main()
   {
       drfl.set_on_disconnected(OnDisconnectedCB);
   }

When registered, this callback function executes automatically  
when the **connection between the robot controller and the client is lost**.  
It allows the user to implement **reconnection logic or error recovery procedures**  
for stable operation in external environments.
