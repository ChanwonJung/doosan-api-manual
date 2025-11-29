.. _set_on_monitoring_data_ex:

set_on_monitoring_data_ex
------------------------------------------
This is a function for registering an extended callback that monitors the robot’s operation data,  
such as joint positions and user coordinates, in real time.  
It is available only in **M2.5 version or higher** and is activated  
when the monitoring data version is set to 1 using the `set_up_monitoring_version()` function.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 615)

.. code-block:: cpp

    void set_on_monitoring_data_ex(TOnMonitoringDataExCB pCallbackFunc) { 
        _set_on_monitoring_data_ex(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringDataExCB <cb_tonmonitoringdataexcb>`
     - -
     - Extended data callback function pointer to handle real-time monitoring updates

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringDataExCB(const LPMONITORING_DATA_EX pData)
   {
       cout << "joint data "
            << pData->_tCtrl._tUser._fActualPos[0] << ", "
            << pData->_tCtrl._tUser._fActualPos[1] << ", "
            << pData->_tCtrl._tUser._fActualPos[2] << ", "
            << pData->_tCtrl._tUser._fActualPos[3] << ", "
            << pData->_tCtrl._tUser._fActualPos[4] << ", "
            << pData->_tCtrl._tUser._fActualPos[5] << endl;
   }

   int main()
   {
       drfl.set_on_monitoring_data_ex(OnMonitoringDataExCB);
   }

This example registers an **extended monitoring callback**  
that continuously prints the robot’s **user-frame joint position data** in real time.  
It requires the monitoring version to be set to **1** for activation.
