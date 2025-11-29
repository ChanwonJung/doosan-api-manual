.. _set_on_monitoring_modbus:

set_on_monitoring_modbus
------------------------------------------
This function registers a callback that automatically monitors  
the current state of Modbus I/O channels configured in the robot controller.  
It is useful when Modbus-based external devices or sensors need to be monitored in real time.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 631)

.. code-block:: cpp

    void set_on_monitoring_modbus(TOnMonitoringModbusCB pCallbackFunc) { 
        _set_on_monitoring_modbus(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringModbusCB <cb_tonmonitoringmodbuscb>`
     - -
     - Callback function pointer for Modbus I/O monitoring

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringModbusCB(const LPMONITORING_MODBUS pModbus)
   {
       // Displays the Modbus I/O states
       cout << "modbus data" << endl;
       for (int i = 0; i < pModbus->_iRegCount; i++)
           cout << pModbus->_tRegCount[i]._szSymbol << ": " << pModbus->_tRegCount[i]._iValue << endl;
   }

   int main()
   {
       drfl.set_on_monitoring_modbus(OnMonitoringModbusCB);
   }

This example registers a **Modbus monitoring callback** that continuously prints  
the **symbol names and values** of each Modbus register in the controller.
