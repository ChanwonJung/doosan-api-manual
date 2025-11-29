.. _set_welding_cockpit_setting:

set_welding_cockpit_setting
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1045)

.. code-block:: cpp

    bool set_welding_cockpit_setting(unsigned char bEnable, unsigned char bWeldingType)
    {
        return _set_welding_cockpit_setting(_rbtCtrl, bEnable, bWeldingType);
    };

**Features**

This function configures **tack welding parameters** such as welding mode, repetition count,  
tack welding duration, and interval time.  

By setting these parameters, users can define specific cockpit settings for repeated tack welding operations.  
It is typically used when precise control of short, repetitive welds is required (e.g., spot or tack welding applications).

**Arguments**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Field Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bEnable
     - unsigned char
     - -
     - **Activation flag for the welding cockpit setting** |br|
       0: Disable cockpit setting |br|
       1: Enable cockpit setting
   * - bWeldingType
     - unsigned char
     - -
     - Type of welding operation mode. |br|
       (e.g., tack, continuous, or special mode based on system configuration.)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failure (invalid parameter or system not ready.)
   * - 1
     - Success (welding cockpit setting applied successfully.)

**Example**

.. code-block:: cpp

    // Example: Enable tack welding cockpit mode
    unsigned char bEnable = 1;        // 1: Enable, 0: Disable
    unsigned char bWeldingType = 0;   // 0: Tack welding mode

    // Apply cockpit setting configuration
    bool result = Drfl.set_welding_cockpit_setting(bEnable, bWeldingType);

    if (result)
        std::cout << "Welding cockpit setting successfully applied." << std::endl;
    else
        std::cout << "Failed to apply welding cockpit setting." << std::endl;

In this example, the **cockpit setting** is enabled for **tack welding mode**.  
These settings allow control over parameters like tack count, weld time, and interval time,  
improving precision and repeatability during automated short weld sequences.
