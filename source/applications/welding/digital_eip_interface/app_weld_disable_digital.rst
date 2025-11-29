.. _app_weld_disable_digital:

app_weld_disable_digital
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1037)

.. code-block:: cpp

    bool app_weld_disable_digital(unsigned char bMode)
    {
        return _app_weld_disable_digital(_rbtCtrl, bMode);
    };

**Features**

This function **deactivates** the digital welding function that was previously enabled using  
:ref:`app_weld_enable_digital <app_weld_enable_digital>`.  
When disabled, the communication between the robot controller and the welder via **EtherNet/IP**  
is terminated, and all ongoing welding operations using the digital interface are stopped.

Use this function to **safely stop** or **reset** the digital welding mode before modifying welding configurations  
or performing system reinitialization.

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
     - **Digital welding mode control flag** |br|
       0: Deactivate (turn off EtherNet/IP welding communication) |br|
       1: Reserved (no action)

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

    // Disable digital welding communication mode
    unsigned char bMode = 0;   // 0: deactivate
    bool result = Drfl.app_weld_disable_digital(bMode);

    if(result)
        printf("Digital welding interface disabled successfully.\n");
    else
        printf("Failed to disable digital welding interface.\n");

This example disables the **EtherNet/IP-based digital welding interface**,  
returning the robot to a non-welding communication state.
