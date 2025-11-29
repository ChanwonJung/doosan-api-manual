.. _app_weld_reset_interface:

app_weld_reset_interface
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1033)

.. code-block:: cpp

    bool app_weld_reset_interface(unsigned char bReset)
    {
        return _app_weld_reset_interface(_rbtCtrl, bReset);
    };

**Features**

This function resets the **welding communication interface** to its **initial state**.  
It clears all EtherNet/IP configuration data, welding condition parameters,  
and signal mappings previously set using EtherNet/IP interface setup functions.  

Use this function when you need to **reinitialize or clear** all welding interface settings  
before reconfiguring new digital welding communication conditions.

**Arguments** |br|
None

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

    // Reset all EtherNet/IP welding interface configurations
    unsigned char bReset = 1;
    bool result = Drfl.app_weld_reset_interface(bReset);

    if(result)
        printf("Welding interface successfully reset to default state.\n");
    else
        printf("Failed to reset welding interface.\n");

This example resets all configured EtherNet/IP welding interface settings,  
returning the robot controller’s welding communication state to factory defaults.
