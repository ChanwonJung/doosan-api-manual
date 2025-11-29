.. _set_on_monitoring_data:

set_on_monitoring_data
------------------------------------------
This is a function for registering a callback that automatically monitors  
the robot’s operation data such as joint positions, task coordinates, and system status.  
It is useful when certain tasks must execute automatically upon data updates.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 613)

.. code-block:: cpp

    void set_on_monitoring_data(TOnMonitoringDataCB pCallbackFunc) { 
        _set_on_monitoring_data(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringDataCB <cb_tonmonitoringdatacb>`
     - -
     - Callback function pointer to handle real-time monitoring data updates

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringDataCB(const LPMONITORING_DATA pData)
   {
       // Displays the current joint position data
       cout << "joint data "
            << pData->_tCtrl._tJoint._fActualPos[0] << ", "
            << pData->_tCtrl._tJoint._fActualPos[1] << ", "
            << pData->_tCtrl._tJoint._fActualPos[2] << ", "
            << pData->_tCtrl._tJoint._fActualPos[3] << ", "
            << pData->_tCtrl._tJoint._fActualPos[4] << ", "
            << pData->_tCtrl._tJoint._fActualPos[5] << endl;
   }

   int main()
   {
       drfl.set_on_monitoring_data(OnMonitoringDataCB);
   }


This example registers a **data monitoring callback**  
that continuously prints the robot’s **joint positions** in real time as they are updated by the controller.
