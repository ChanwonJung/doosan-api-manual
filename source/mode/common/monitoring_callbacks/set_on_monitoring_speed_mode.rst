.. _set_on_monitoring_speed_mode:

set_on_monitoring_speed_mode
------------------------------------------
This function registers a callback that automatically monitors  
the current **speed mode** (normal or reduced) of the robot controller.  
It is useful when actions must be triggered in response to speed mode changes.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 633)

.. code-block:: cpp

    void set_on_monitoring_speed_mode(TOnMonitoringSpeedModeCB pCallbackFunc) { 
        _set_on_monitoring_speed_mode(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringSpeedModeCB <cb_tonmonitoringspeedmodecb>`
     - -
     - Callback function pointer for monitoring robot speed mode

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringSpeedModeCB(const MONITORING_SPEED eSpdMode)
   {
       // Displays the current velocity mode
       cout << "speed mode: " << (int)eSpdMode << endl;
   }

   int main()
   {
       drfl.set_on_monitoring_speed_mode(OnMonitoringSpeedModeCB);
   }

This example registers a **speed mode monitoring callback** that prints the robot’s  
current velocity mode (e.g., normal or reduced) whenever it changes in the controller.
