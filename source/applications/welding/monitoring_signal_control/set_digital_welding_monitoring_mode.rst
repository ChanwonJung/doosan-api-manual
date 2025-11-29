.. _set_digital_welding_monitoring_mode:

set_digital_welding_monitoring_mode
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1049)

.. code-block:: cpp

    bool set_digital_welding_monitoring_mode(unsigned char bEnable)
    {
        return _set_digital_welding_monitoring_mode(_rbtCtrl, bEnable);
    };

**Features**

This function **activates or deactivates the digital welding monitoring mode**  
for real-time supervision of welding parameters.  

When activated, the robot controller continuously transmits welding-related process data  
(e.g., current, voltage, feed rate, or error state) through the digital communication interface.  
When deactivated, monitoring is stopped, and no further updates are received.

It is typically used to toggle the digital monitoring state before starting or after completing a weld process.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Field Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bEnable
     - unsigned char
     - -
     - **Digital welding monitoring mode status** |br|
       0: Deactivated |br|
       1: Activated

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error (failed to change monitoring state.)
   * - 1
     - Success (monitoring mode successfully updated.)

**Example**

.. code-block:: cpp

    // Enable the digital welding monitoring mode
    unsigned char bEnable = 1;   // 1: activated, 0: deactivated

    // Call the function to toggle monitoring mode
    bool result = Drfl.set_digital_welding_monitoring_mode(bEnable);

    if (result)
        std::cout << "Digital welding monitoring mode activated." << std::endl;
    else
        std::cout << "Failed to activate digital welding monitoring mode." << std::endl;

In this example, the function enables real-time digital welding monitoring.  
When `bEnable` is set to 1, the controller starts broadcasting welding process data.  
Setting it to 0 stops monitoring and suspends data transmission.
