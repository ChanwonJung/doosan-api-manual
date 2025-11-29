.. _set_on_monitoring_access_control:

set_on_monitoring_access_control
------------------------------------------
This function registers a callback that monitors and reacts to **control right events**  
(such as request, permission, or rejection) in the robot controller.  
It is useful for managing multiple clients requesting robot control authority.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 635)

.. code-block:: cpp

    void set_on_monitoring_access_control(TOnMonitoringAccessControlCB pCallbackFunc) { 
        _set_on_monitoring_access_control(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringAccessControlCB <cb_tonmonitoringaccesscontrolcb>`
     - -
     - Callback function pointer triggered on access control events

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringAccessControlCB(const MONITORING_ACCESS_CONTROL eAccCtrl)
   {
       // Handles access control request messages
       switch (eAccCtrl)
       {
       case MONITORING_ACCESS_CONTROL_REQUEST:
           // Rejects the transfer of control right
           drfl.manage_access_control(MANAGE_ACCESS_CONTROL_RESPONSE_NO);
           break;
       default:
           break;
       }
   }

   int main()
   {
       drfl.set_on_monitoring_access_control(OnMonitoringAccessControlCB);
   }

This example registers an **access control monitoring callback**  
that listens for robot control right requests from external clients.  
When a control right request is received, the callback automatically responds with a rejection signal.
