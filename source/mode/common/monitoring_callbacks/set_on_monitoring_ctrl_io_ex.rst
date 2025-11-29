.. _set_on_monitoring_ctrl_io_ex:

set_on_monitoring_ctrl_io_ex
------------------------------------------
This is a function for registering an **extended callback** that monitors  
the I/O state of the control box installed in the robot controller.  
The function interface differs depending on whether the controller is **V2** or **V3**,  
and it is available only in **M2.5 version or higher**.  
To activate this feature, the monitoring version must be set to **1** using `set_up_monitoring_version()`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 627)

.. code-block:: cpp

    #if DRCF_VERSION == 2
        void set_on_monitoring_ctrl_io_ex(TOnMonitoringCtrlIOExCB pCallbackFunc) { 
            _set_on_monitoring_ctrl_io_ex(_rbtCtrl, pCallbackFunc); 
        };
    #elif DRCF_VERSION == 3
        // Latest version — callback activated after setup_monitoring_version(1)
        void set_on_monitoring_ctrl_io_ex(TOnMonitoringCtrlIOEx2CB pCallbackFunc) { 
            _set_on_monitoring_ctrl_io_ex2(_rbtCtrl, pCallbackFunc); 
        };
    #endif

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnMonitoringCtrlIOExCB <cb_tonmonitoringctrliioexcb>` / :ref:`TOnMonitoringCtrlIOEx2CB <cb_tonmonitoringctrliioex2cb>`
     - - 
     - Extended callback function pointer for monitoring control I/O signals |br|
       The structure varies depending on controller version (`DRCF_VERSION` 2 or 3)

**Return** |br|
None

**Example**

.. code-block:: cpp

   #if DRCF_VERSION == 2
   void OnMonitoringCtrlIOExCB(const LPMONITORING_CTRLIO_EX pCtrlIO)
   {
       cout << "gpio data" << endl;
       for (int i = 0; i < NUM_DIGITAL; i++)
           cout << "DIO[" << i << "]: " << pCtrlIO->_tInput._iActualDI[i] << endl;
   }
   #elif DRCF_VERSION == 3
   void OnMonitoringCtrlIOExCB(const LPMONITORING_CTRLIO_EX2 pCtrlIO)
   {
       cout << "gpio data" << endl;
       for (int i = 0; i < NUM_DIGITAL; i++)
           cout << "DIO[" << i << "]: " << pCtrlIO->_tInput._iActualDI[i] << endl;
   }
   #endif

   int main()
   {
       drfl.set_on_monitoring_ctrl_io_ex(OnMonitoringCtrlIOExCB);
   }

This example registers an **extended I/O monitoring callback**  
that continuously prints the **digital input states** from the controller.  
The callback interface differs depending on the defined controller version (`V2` or `V3`).
