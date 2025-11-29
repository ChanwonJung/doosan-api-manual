.. _set_on_monitoring_safety_stop_type:

set_on_monitoring_safety_stop_type
------------------------------------------
This function registers a callback that automatically detects and responds  
when the **safety stop type** of the robot controller changes.  
It is typically used to handle different safety stop events such as *protective stop*, *emergency stop*, or *recovery stop*.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 660)

.. code-block:: cpp

    void set_on_monitoring_safety_stop_type(TOnMonitoringSafetyStopTypeCB pCallbackFunc) { 
        _set_on_monitoring_safety_stop_type(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringSafetyStopTypeCB <cb_tonmonitoringsafetystoptypecb>`
     - -
     - Callback function pointer triggered when the safety stop type of the controller is updated

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringSafetyStopTypeCB(SafetyStopType eStopType)
   {
       // Triggered when the robot safety stop type changes
       // Example: Emergency stop, protective stop, or recovery stop
   }

   int main()
   {
       drfl.set_on_monitoring_safety_stop_type(OnMonitoringSafetyStopTypeCB);
   }

This example registers a **safety stop type monitoring callback**  
that executes automatically when the controller’s safety stop type changes.  
It enables real-time responses to various safety stop events for safe and predictable robot behavior.
