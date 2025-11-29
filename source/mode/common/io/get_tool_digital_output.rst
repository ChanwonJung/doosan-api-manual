.. _get_tool_digital_output:

get_tool_digital_output
------------------------------------------
This function checks the **current output signal state** of a **tool-side digital contact point**  
mounted on the **robot arm** (end-effector side), through the robot controller. |br|
It allows users to verify whether a tool digital output pin is currently ON or OFF.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 834)

.. code-block:: cpp

    bool get_tool_digital_output(GPIO_TOOL_DIGITAL_INDEX eGpioIndex) 
    { return _get_tool_digital_output(_rbtCtrl, eGpioIndex); };

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
     - Index of the tool-side digital output pin to read. 

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - **OFF** — Digital output signal is currently low (0 V)
   * - 1
     - **ON** — Digital output signal is currently high (24 V)

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Read current status of tool-side digital output #1
       bool bOutputState = drfl.get_tool_digital_output(GPIO_TOOL_DIGITAL_INDEX_1);

       if (bOutputState) {
           printf("Tool output #1 is ON.\\n");
       } else {
           printf("Tool output #1 is OFF.\\n");
       }
   }

This example shows how to **monitor the ON/OFF state** of a digital output pin  
mounted on the robot tool flange — typically used for actuating **grippers, valves**,  
or other peripheral devices controlled via tool-side I/O.
