.. _set_on_monitoring_digital_welding_data:

set_on_monitoring_digital_welding_data
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 623)

.. code-block:: cpp

    void set_on_monitoring_digital_welding_data(TOnMonitoringDigitalWeldingDataCB pCallbackFunc)
    {
        _set_on_monitoring_digital_welding_data(_rbtCtrl, pCallbackFunc);
    };

**Features**

This function registers a **callback** to receive **digital welding monitoring data**  
from a lower-level robot controller. It is used to monitor real-time welding process parameters  
such as current, voltage, feed rate, offset, and error states from a digital welding interface  
(e.g., EtherNet/IP).

This function is especially useful for systems performing **process verification**,  
**error tracking**, or **dynamic quality adjustment** during automated welding.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Field**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - pCallbackFunc
     - :ref:`TOnMonitoringDigitalWeldingDataCB <cb_TOnMonitoringDigitalWeldingDataCB>`
     - -
     - Function pointer called by the lower-level controller to deliver digital welding status data. 

**Return** |br|
None

**Example**

.. code-block:: cpp

    // Callback function for digital welding monitoring
    void DigitalWeldingDataCallback(const LPROBOT_DIGITAL_WELDING_DATA pData)
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
        std::cout << "Feed Velocity : " << pData->_fFeedVel << std::endl;
        std::cout << "Error No : " << pData->_iErrorNo << std::endl;
        std::cout << "Program Active : " << static_cast<int>(pData->_bProgActive) << std::endl;
        std::cout << "Voltage Correction : " << pData->_fVoltageCorrection << std::endl;
        std::cout << "Dynamic Correction : " << pData->_fDynamicCorrection << std::endl;
    }

    int main()
    {
        // Register callback for digital welding data monitoring
        Drfl.set_on_monitoring_digital_welding_data(DigitalWeldingDataCallback);
        return 0;
    }

In this example, `DigitalWeldingDataCallback` continuously receives live welding metrics  
from the controller’s digital interface, including target and actual values for voltage/current,  
feed velocity, and dynamic arc corrections.  
This callback is typically used to visualize or record welding performance data  
in real-time monitoring systems or SCADA dashboards.
