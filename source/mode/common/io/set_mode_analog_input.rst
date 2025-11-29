.. _set_mode_analog_input:

set_mode_analog_input
------------------------------------------
This function sets the **input channel mode** for an analog input port on the  
robot controller’s **control box**. |br|
Depending on the configuration, each analog input channel can operate  
either in **current mode (mA)** or **voltage mode (V)**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 849)

.. code-block:: cpp

    bool set_mode_analog_input(GPIO_CTRLBOX_ANALOG_INDEX eGpioIndex,
                               GPIO_ANALOG_TYPE eAnalogType = GPIO_ANALOG_TYPE_CURRENT) 
    { return _set_mode_analog_input(_rbtCtrl, eGpioIndex, eAnalogType); };

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
   * - eAnalogType
     - :ref:`GPIO_ANALOG_TYPE <enum_gpio_analog_type>`
     - GPIO_ANALOG_TYPE_CURRENT
     - Type of analog input mode. 

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to configure the analog input mode
   * - 1
     - Success — mode configuration applied successfully

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set analog input #1 to current mode (4–20 mA)
       drfl.set_mode_analog_input(GPIO_CTRLBOX_ANALOG_INDEX_1, GPIO_ANALOG_TYPE_CURRENT);

       // Set analog input #2 to voltage mode (0–10 V)
       drfl.set_mode_analog_input(GPIO_CTRLBOX_ANALOG_INDEX_2, GPIO_ANALOG_TYPE_VOLTAGE);
   }

This example configures **analog input #1** to operate in **current mode**  
and **analog input #2** in **voltage mode**, enabling the robot controller  
to read sensor values in both electrical signal formats.
