.. _set_welding_cockpit_setting_time_setting:

set_welding_cockpit_setting_time_setting
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1053)

.. code-block:: cpp

    void set_welding_cockpit_setting_time_setting(int time)
    {
        return _set_welding_cockpit_setting_time_setting(_rbtCtrl, time);
    };

**Features**

This function sets or updates the **time configuration value** for the welding cockpit.  
The time parameter defines the **duration of the tack welding cycle** or **interval** depending on the active cockpit setting.  
The input value must be provided in **seconds**.

This function is typically used when fine-tuning the **repetition rate** or **hold time** during welding operations  
to ensure consistent results in short, repetitive welds or automated sequences.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Field**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - time
     - int
     - -
     - Time setting value for the welding cockpit, specified in **seconds (s)**. 

**Return** |br|
None

**Example**

.. code-block:: cpp

    // Set the welding cockpit time setting to 5 seconds
    int time = 5;  // Unit: seconds

    // Apply the cockpit time configuration
    Drfl.set_welding_cockpit_setting_time_setting(time);

    std::cout << "Welding cockpit time set to " << time << " seconds." << std::endl;

In this example, the function adjusts the **time parameter** of the welding cockpit to 5 seconds.  
This allows for precise control over the **duration of tack welding or timing intervals**  
within a programmed welding sequence.
