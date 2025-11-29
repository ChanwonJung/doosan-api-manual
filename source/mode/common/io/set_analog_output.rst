.. _set_analog_output:

set_analog_output
------------------------------------------
This function outputs an **analog signal** through the analog output port  
on the robot controller’s **control box**.  
Depending on the output mode (current or voltage), the analog signal value  
is transmitted in the range supported by the hardware.

It is mainly used to control external devices such as pneumatic regulators,  
servo amplifiers, or analog-driven instruments that require continuous voltage or current control.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 846)

.. code-block:: cpp

    bool set_analog_output(GPIO_CTRLBOX_ANALOG_INDEX eGpioIndex, float fValue) 
    { return _set_analog_output(_rbtCtrl, eGpioIndex, fValue); };

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
     - Index of the analog output port on the control box.
   * - fValue
     - float
     - -
     - Analog signal output value.  |br|
       - In **current mode**: 4.0 – 20.0 [mA] |br|  
       - In **voltage mode**: 0.0 – 10.0 [V]

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to output analog signal
   * - 1
     - Success — analog signal output successfully applied

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set analog output mode of channel #1 to current (mA)
       drfl.set_mode_analog_output(GPIO_CTRLBOX_ANALOG_INDEX_1, GPIO_ANALOG_TYPE_CURRENT);

       // Output 5.2 mA signal on analog output channel #1
       bool result = drfl.set_analog_output(GPIO_CTRLBOX_ANALOG_INDEX_1, 5.2f);

       if (result)
           printf("Analog output applied successfully.\n");
       else
           printf("Failed to output analog signal.\n");
   }

This example sets the **analog output #1** to **current mode** and sends  
a 5.2 mA signal to the connected device.  |br|
If **voltage mode** is configured instead, the same function can be used  
to output continuous voltages in the range of 0 – 10 V.
