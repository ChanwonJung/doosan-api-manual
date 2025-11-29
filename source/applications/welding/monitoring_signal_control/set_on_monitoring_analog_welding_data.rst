.. _set_on_monitoring_analog_welding_data:

set_on_monitoring_analog_welding_data
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 622)

.. code-block:: cpp

    void set_on_monitoring_analog_welding_data(TOnMonitoringAnalogWeldingDataCB pCallbackFunc)
    {
        _set_on_monitoring_analog_welding_data(_rbtCtrl, pCallbackFunc);
    };

**Features**

This function registers a **callback** to receive **analog welding monitoring data**  
from a lower-level robot controller. It enables the upper-level controller or host system  
to monitor analog-based welding parameters—such as **voltage, current, and feed rate**—in real time  
through a callback mechanism.

It is typically used in systems that require detailed analog feedback for process tuning,  
data logging, or welding performance visualization.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Field**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - pCallbackFunc
     - :ref:`TOnMonitoringAnalogWeldingDataCB <cb_TOnMonitoringAnalogWeldingDataCB>`
     - -
     - Function pointer called by the controller to deliver analog welding status data.

**Return** |br|
None 

**Example**

.. code-block:: cpp

    // Callback function to handle incoming analog welding monitoring data
    void AnalogWeldingDataCallback(const LPROBOT_ANALOG_WELDING_DATA pData)
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
        std::cout << "Welding Velocity : " << pData->_fFeedVel << std::endl;
    }

    int main()
    {
        // Register callback for analog welding data monitoring
        Drfl.set_on_monitoring_analog_welding_data(AnalogWeldingDataCallback);
        return 0;
    }

In this example, `AnalogWeldingDataCallback` continuously receives analog welding feedback  
such as target/actual current and voltage, offsets, and process states.  
This function is essential for real-time process supervision or adaptive welding control  
using analog feedback signals from the welding interface.
