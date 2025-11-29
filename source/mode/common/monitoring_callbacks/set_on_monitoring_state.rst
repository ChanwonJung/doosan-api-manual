.. _set_on_monitoring_state:

set_on_monitoring_state
------------------------------------------
This is a function for registering a callback that automatically detects changes  
in the operation state of the robot controller.  
It is useful for executing specific actions automatically when the robot’s state changes.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 611)

.. code-block:: cpp

    void set_on_monitoring_state(TOnMonitoringStateCB pCallbackFunc) { 
        _set_on_monitoring_state(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringStateCB <cb_tonmonitoringstatecb>`
     - -
     - Callback function pointer to be registered for robot state monitoring

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringStateCB(const ROBOT_STATE eState)
   {
       switch ((unsigned char)eState)
       {
           case STATE_SAFE_OFF:
               // Robot controller servo ON
               drfl.set_robot_control(CONTROL_RESET_SAFET_OFF);
               break;

           default:
               break;
       }
   }

   int main()
   {
       drfl.set_on_monitoring_state(OnMonitoringStateCB);
   }

This example registers a **state monitoring callback**  
that automatically turns on the robot servo when the controller enters the **SAFE OFF** state.
