.. _set_on_monitoring_robot_system:

set_on_monitoring_robot_system
------------------------------------------
This function registers a callback that automatically detects changes  
in the **robot system type** (e.g., real or virtual) of the controller.  
It is useful for automatically handling events when the robot switches its operational environment.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 658)

.. code-block:: cpp

    void set_on_monitoring_robot_system(TOnMonitoringRobotSystemCB pCallbackFunc) { 
        _set_on_monitoring_robot_system(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringRobotSystemCB <cb_tonmonitoringrobotsystemcb>`
     - -
     - Callback function pointer triggered when the robot system changes

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringRobotSystemCB(ROBOT_STATE eRobotState)
   {
       // Triggered when the robot operation system changes
   }

   int main()
   {
       drfl.set_on_monitoring_robot_system(OnMonitoringRobotSystemCB);
   }

This example registers a **robot system monitoring callback**  
that automatically runs whenever the controller switches between the **virtual** and **real robot** environments.  
Developers can use this to synchronize environment-specific settings or handle safety logic dynamically.
