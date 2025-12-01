.. _set_tool_digital_output_level:

set_tool_digital_output_level
------------------------------------------
This function sets the **output voltage level** for **digital output signals**  
on the **robot tool flange (end-effector side)**.  |br|
By adjusting the voltage level, users can match the output signal to the requirements  
of the connected peripheral device (e.g., grippers, solenoid valves, sensors).

This function is available **only on the new flange version (v2)**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 854)

.. code-block:: cpp

    bool set_tool_digital_output_level(int nLv) 
    { return _set_tool_digital_output_level(_rbtCtrl, nLv); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - nLv
     - int
     - 12
     - **The voltage level to be output to the tool digital output port** |br| 
       0: Output disabled |br|  
       12: 12 V output |br|
       24: 24 V output |br| 
       *(Default: 12 V)*

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — Failed to set the tool output voltage level.
   * - 1
     - Success — Voltage level successfully updated.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set tool flange digital output voltage level to 24V
       bool result = drfl.set_tool_digital_output_level(24);

       if (result)
           printf("Tool digital output voltage set to 24V.\n");
       else
           printf("Failed to set digital output voltage.\n");
   }

This example demonstrates how to configure the **output power level**  
for the robot’s **tool-side digital output pins**. |br|
Adjusting the voltage allows compatibility with different **external actuators**  
or **electronic modules** that require specific operating voltages.
