.. _app_weld_enable_digital:

app_weld_enable_digital
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1035)

.. code-block:: cpp

    bool app_weld_enable_digital(unsigned char bMode)
    {
        return _app_weld_enable_digital(_rbtCtrl, bMode);
    };

**Features**

This function activates the **digital welding function** using the communication interface.  
Only the **EtherNet/IP-based digital interface** is supported for this command.  
Once activated, the robot controller begins communication with the external welder device  
based on previously configured interface settings (e.g., process, mode, test, condition).

To deactivate the welding interface, call the corresponding disable command.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bMode
     - unsigned char
     - -
     - **Digital welding mode setting** |br|
       0: Deactivate (Disable communication) |br|
       1: Activate (Enable EtherNet/IP welding interface)

**Return**

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

    // Activate digital welding interface mode
    unsigned char bMode = 1;   // 1: Activated
    bool result = Drfl.app_weld_enable_digital(bMode);

    if(result)
        printf("Digital welding interface activated successfully.\n");
    else
        printf("Failed to enable digital welding mode.\n");

This example enables the **EtherNet/IP-based digital welding interface**,  
allowing the robot controller to communicate with the welder for real-time process control.
