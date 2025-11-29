.. _get_analog_input:

get_analog_input
------------------------------------------
This function reads the **current analog input signal** from the specified analog port  
on the robot controller’s **control box**.  
Depending on the input mode (current or voltage), it returns the measured signal value  
in the corresponding physical unit.

It is mainly used for monitoring external sensors, potentiometers,  
or other analog devices connected to the robot controller.

**Version Note** |br|
- If **DRCF version = 2**, this function internally calls ``_get_analog_input()``.  |br|
- If **DRCF version = 3**, it calls ``_get_analog_input_ex()`` for extended analog precision and range support. |br|
Refer to :ref:`get_library_version <get_library_version>` for checking the current DRCF version.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 839/844)

.. code-block:: cpp

    #if DRCF_VERSION == 2
    float get_analog_input(GPIO_CTRLBOX_ANALOG_INDEX eGpioIndex) {
        return _get_analog_input(_rbtCtrl, eGpioIndex);
    };
    #elif DRCF_VERSION == 3
    float get_analog_input(GPIO_CTRLBOX_ANALOG_INDEX eGpioIndex) {
        return _get_analog_input_ex(_rbtCtrl, eGpioIndex);
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
   * - eGpioIndex
     - :ref:`GPIO_CTRLBOX_ANALOG_INDEX <enum_gpio_ctrlbox_analog_index>` 
     - -
     - Index of the analog input port on the control box.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - float
     - Analog input signal value. |br|
       - In **current mode**: 4.0 – 20.0 [mA] |br| 
       - In **voltage mode**: 0.0 – 10.0 [V]

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set analog input #1 mode to current (mA)
       drfl.set_mode_analog_output(GPIO_CTRLBOX_ANALOG_INDEX_1, GPIO_ANALOG_TYPE_CURRENT);

       // Read the current analog input value from channel #1
       float fCurrent = drfl.get_analog_input(GPIO_CTRLBOX_ANALOG_INDEX_1);

       printf("Analog input #1 current value: %.2f mA\n", fCurrent);
   }

This example sets the **analog input channel #1** to **current mode**  
and reads the live signal value (in milliamps) from the connected sensor.  
When in voltage mode, the function returns values in **volts (0.0–10.0 V)**.
