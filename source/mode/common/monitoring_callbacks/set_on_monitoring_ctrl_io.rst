.. _set_on_monitoring_ctrl_io:

set_on_monitoring_ctrl_io
------------------------------------------
This is a function for registering a callback that automatically monitors  
the current state of the I/O modules installed in the robot controller’s control box.  
It is typically used for tracking digital input/output changes in real time.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 617)

.. code-block:: cpp

    void set_on_monitoring_ctrl_io(TOnMonitoringCtrlIOCB pCallbackFunc) { 
        _set_on_monitoring_ctrl_io(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnMonitoringCtrlIOCB <cb_tonmonitoringctrliocb>` 
     - -
     - Callback function pointer for I/O state monitoring

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMonitoringCtrlIOCB(const LPMONITORING_CTRLIO pCtrlIO)
   {
       // Displays the digital input GPIO state data
       cout << "gpio data" << endl;
       for (int i = 0; i < NUM_DIGITAL; i++)
           cout << "DIO[" << i << "]: " << pCtrlIO->_tInput._iActualDI[i] << endl;
   }

   int main()
   {
       drfl.set_on_monitoring_ctrl_io(OnMonitoringCtrlIOCB);
   }

This example registers an **I/O monitoring callback**  
that continuously prints the **digital input signal states** detected from the robot controller.
