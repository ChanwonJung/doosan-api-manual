.. _get_tool_digital_input:

get_tool_digital_input
------------------------------------------
This function reads a **digital input signal** from the **tool-side contact point**  
mounted on the **robot arm** (end-effector side), through the robot controller. |br|
It is mainly used to detect external signals from sensors or switches attached to the tool flange.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 833)

.. code-block:: cpp

    bool get_tool_digital_input(GPIO_TOOL_DIGITAL_INDEX eGpioIndex) 
    { return _get_tool_digital_input(_rbtCtrl, eGpioIndex); };

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
     - Index of the tool-side digital input pin

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - **OFF** — No signal detected (Low level)
   * - 1
     - **ON** — Signal detected (High level)

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Check digital input #1 on the tool-side connector
       bool bSignal = drfl.get_tool_digital_input(GPIO_TOOL_DIGITAL_INDEX_1);

       if (bSignal) {
           // Example: sensor detected or gripper limit switch triggered
           printf("Tool input signal is ON.\\n");
       } else {
           printf("Tool input signal is OFF.\\n");
       }
   }

This example demonstrates how to monitor **tool-side input pins** on the robot arm,  
which are commonly used to read signals from **proximity sensors**, **gripper switches**,  
or other external digital devices mounted on the tool flange.
