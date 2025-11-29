.. _manage_access_control:

manage_access_control
------------------------------------------
This is a function for sending the **control right request message** to the robot controller,  
or for processing a user response when the control right request message is received.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 751)

.. code-block:: cpp

    bool manage_access_control(MANAGE_ACCESS_CONTROL eAccessControl = MANAGE_ACCESS_CONTROL_REQUEST) { 
        return _manage_access_control(_rbtCtrl, eAccessControl); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eAccessControl
     - :ref:`MANAGE_ACCESS_CONTROL <enum_manage_access_control>`
     - MANAGE_ACCESS_CONTROL_REQUEST
     - Specifies the type of control authority management command.
     
**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to send or process the control right message.
   * - 1
     - int
     - Success — successfully processed the control right request or response.

**Example**

.. code-block:: cpp

   void OnMonitoringAccessControlCB(const MONITORING_ACCESS_CONTROL eAccCtrl)
   {
       switch(eAccCtrl) {
           case MONITORING_ACCESS_CONTROL_DENY:
               // Deny the transfer of control right
               break;
           default:
               // Displays no control right message
               break;
       }
   }

   int main()
   {
       drfl.SetOnMonitoringAccessControl(OnMonitoringAccessControlCB);

       // Requests transfer of control right
       drfl.manage_access_control(MANAGE_ACCESS_CONTROL_REQUEST);
   }

This example registers a **callback function** to monitor control-right events  
and sends a **control right request** to the robot controller.  
When executed, it requests authority to control the robot and handles responses (granted or denied) accordingly.
