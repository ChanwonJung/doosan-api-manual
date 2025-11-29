.. _set_digital_welding_signal_output:

set_digital_welding_signal_output
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1047)

.. code-block:: cpp

    bool set_digital_welding_signal_output(unsigned char cDataType, float fData)
    {
        return _set_digital_welding_signal_output(_rbtCtrl, cDataType, fData);
    };

**Features**

This function sends a **digital welding control signal** to the welder through the robot controller.  
It allows the user to set or modify specific output data types such as **voltage**, **current**,  
**feed rate**, or **correction factors** depending on the digital welding interface configuration.  

The function is typically used to command real-time welding output parameters  
while performing automatic or adaptive welding control tasks.

**Arguments**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - cDataType
     - unsigned char
     - -
     - Specifies the type of welding signal to output. |br|
       (e.g., voltage, current, speed, or user-defined digital output.)
   * - fData
     - float
     - None
     - The numeric value of the welding parameter to be sent to the welder.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error occurred while sending signal.
   * - 1
     - Successfully transmitted the digital welding output signal.

**Example**

.. code-block:: cpp

    // Example: Set a digital welding signal output for voltage control
    unsigned char dataType = 1;   // Example type code for voltage
    float voltageValue = 25.5f;   // Desired voltage setting

    bool result = Drfl.set_digital_welding_signal_output(dataType, voltageValue);
    if (result)
        std::cout << "Digital welding signal sent successfully." << std::endl;
    else
        std::cout << "Failed to send digital welding signal." << std::endl;

In this example, the function transmits a command to set the welding signal output.  
The parameter `dataType` defines the signal type (e.g., voltage or current),  
and `fData` defines the actual numeric value sent to the welding interface.  
A return value of **true (1)** indicates successful signal transmission.
