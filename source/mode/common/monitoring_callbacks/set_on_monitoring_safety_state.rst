.. _set_on_monitoring_safety_state:

set_on_monitoring_safety_state
------------------------------------------
This function registers a callback that automatically detects and responds  
when the **safety state** of the robot controller changes.  
It is especially useful when implementing logic that should react to safety events or module updates.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 657)

.. code-block:: cpp

    void set_on_monitoring_safety_state(TOnMonitoringSafetyStateCB pCallbackFunc) { 
        _set_on_monitoring_safety_state(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringSafetyStateCB <cb_tonmonitoringsafetystatecb>`
     - -
     - Callback function pointer triggered when the controller’s safety state is updated 

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringSafetyStateCB(SafetyState iState)
   {
       // Triggered when the safety module state is updated
   }

   int main()
   {
       drfl.set_on_monitoring_safety_state(OnMonitoringSafetyStateCB);
   }

This example registers a **safety monitoring callback**  
that is invoked automatically whenever the controller’s safety module state changes.  
It allows developers to define safety-related responses, such as logging, alerts, or mode changes.
