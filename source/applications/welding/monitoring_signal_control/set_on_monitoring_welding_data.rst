.. _set_on_monitoring_welding_data:

set_on_monitoring_welding_data
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 621)

.. code-block:: cpp

    void set_on_monitoring_welding_data(TOnMonitoringWeldingDataCB pCallbackFunc)
    {
        _set_on_monitoring_welding_data(_rbtCtrl, pCallbackFunc);
    };

**Features**

This function registers a **callback** that receives **real-time welding monitoring data**  
from the lower-level robot controller. The callback function is invoked automatically  
whenever new welding information is available, allowing the upper-level application  
to monitor and process welding parameters such as **target voltage**, **current**,  
and **feed speed** in real time.

This mechanism is typically used in applications that require welding process monitoring,  
performance logging, or adaptive control based on live sensor feedback.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Field**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - pCallbackFunc
     - :ref:`TOnMonitoringWeldingDataCB <cb_TOnMonitoringWeldingDataCB>`
     - -
     - Function pointer called by the controller to deliver welding status data.

**Return** |br| 
None

**Example**

.. code-block:: cpp

    // Callback function to handle incoming welding monitoring data
    void MyWeldingDataCallback(const LPROBOT_WELDING_DATA pData)
    {
        std::cout << "Adj Available : " << static_cast<int>(pData->_bAdjAvail) << std::endl;
        std::cout << "Target Voltage : " << pData->_fTargetVolt << std::endl;
        std::cout << "Target Current : " << pData->_fTargetCur << std::endl;
        std::cout << "Actual Voltage : " << pData->_fActVolt << std::endl;
        std::cout << "Actual Current : " << pData->_fActCur << std::endl;
        std::cout << "Offset Y : " << pData->_fOffsetY << std::endl;
        std::cout << "Offset Z : " << pData->_fOffsetZ << std::endl;
        std::cout << "Gas On : " << static_cast<int>(pData->_bGasOn) << std::endl;
        std::cout << "Wire On : " << static_cast<int>(pData->_bWireOn) << std::endl;
        std::cout << "Teaching Plus : " << static_cast<int>(pData->_bTeachPlus) << std::endl;
        std::cout << "Teaching Minus : " << static_cast<int>(pData->_bTeachMinus) << std::endl;
        std::cout << "Status : " << static_cast<int>(pData->_iStatus) << std::endl;
    }

    int main()
    {
        // Register callback to receive welding monitoring data
        Drfl.set_on_monitoring_welding_data(MyWeldingDataCallback);
        return 0;
    }

In this example, `MyWeldingDataCallback` continuously receives live updates  
on welding parameters such as voltage, current, and wire feed rate during active welding.  
This allows integration of real-time process feedback into monitoring dashboards  
or adaptive control logic.
