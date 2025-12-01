.. _set_tool_digital_output:

set_tool_digital_output
------------------------------------------
This function outputs a **digital signal** at the **tool-side contact point**  
mounted on the **robot arm** (end-effector side), through the robot controller. |br|
It is mainly used to control external devices attached to the flange or wrist,  
such as grippers, valves, or end-effector sensors.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 831)

.. code-block:: cpp

    bool set_tool_digital_output(GPIO_TOOL_DIGITAL_INDEX eGpioIndex, bool bOnOff) 
    { return _set_tool_digital_output(_rbtCtrl, eGpioIndex, bOnOff); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eGpioIndex
     - :ref:`GPIO_TOOL_DIGITAL_INDEX <enum_gpio_tool_digital_index>`
     - -
     - Index of the tool-side digital output pin
   * - bOnOff
     - bool
     - -
     - **Data to output** |br|
       1: ON (set high) |br|
       0: OFF (set low)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to output digital signal
   * - 1
     - Success — digital output signal sent successfully

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Activate the digital output #1 pin on the tool-side connector
       drfl.set_tool_digital_output(GPIO_TOOL_DIGITAL_INDEX_1, true);

       // Turn off the same pin
       drfl.set_tool_digital_output(GPIO_TOOL_DIGITAL_INDEX_1, false);
   }

This example shows how to control the **digital output pin on the robot tool flange**,  
typically used to operate external actuators such as **pneumatic grippers** or **tool LEDs**.
