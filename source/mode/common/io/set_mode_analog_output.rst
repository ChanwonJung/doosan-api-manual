.. _set_mode_analog_output:

set_mode_analog_output
------------------------------------------
This function sets the **output channel mode** for an analog output port  
mounted on the robot controller’s **control box**. |br|
Each analog output channel can be configured to output either  
a **current (mA)** or **voltage (V)** signal depending on the external device requirements.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 851)

.. code-block:: cpp

    bool set_mode_analog_output(GPIO_CTRLBOX_ANALOG_INDEX eGpioIndex,
                                GPIO_ANALOG_TYPE eAnalogType = GPIO_ANALOG_TYPE_CURRENT) 
    { return _set_mode_analog_output(_rbtCtrl, eGpioIndex, eAnalogType); };

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
   * - eAnalogType
     - :ref:`GPIO_ANALOG_TYPE <enum_gpio_analog_type>`
     - GPIO_ANALOG_TYPE_CURRENT
     - Type of analog output mode.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to configure the analog output mode
   * - 1
     - Success — mode configuration applied successfully

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set analog output #1 to current mode (4–20 mA)
       drfl.set_mode_analog_output(GPIO_CTRLBOX_ANALOG_INDEX_1, GPIO_ANALOG_TYPE_CURRENT);

       // Set analog output #2 to voltage mode (0–10 V)
       drfl.set_mode_analog_output(GPIO_CTRLBOX_ANALOG_INDEX_2, GPIO_ANALOG_TYPE_VOLTAGE);
   }

This example configures **analog output #1** to operate in **current mode**  
and **analog output #2** in **voltage mode**, enabling the robot controller  
to generate output signals compatible with various external control devices.
