.. _set_tool_digital_output_type:

set_tool_digital_output_type
------------------------------------------
This function sets the **output type** (PNP or NPN) for **digital output ports**  
on the **robot tool flange (end-effector side)**. |br|
The output type determines the **current flow direction** and how the output signal  
is electrically interfaced with external devices such as grippers, valves, or sensors.

This function is available **only on the new flange version (v2)**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 855)

.. code-block:: cpp

    bool set_tool_digital_output_type(int nPort, OUTPUT_TYPE eOutputType) 
    { return _set_tool_digital_output_type(_rbtCtrl, nPort, eOutputType); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - nPort
     - int
     - 1
     - Tool digital output port number (1–4 depending on model)
   * - eOutputType
     - :ref:`OUTPUT_TYPE <enum_output_type>`
     - OUTPUT_TYPE_PNP
     - Type of electrical output.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to apply the output type configuration.
   * - 1
     - Success — output type successfully updated.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Configure tool digital output port #1 to PNP type
       bool result = drfl.set_tool_digital_output_type(1, OUTPUT_TYPE_PNP);

       if (result)
           printf("Tool DO port #1 configured to PNP output type.\n");
       else
           printf("Failed to configure digital output type.\n");
   }

This example demonstrates how to change the **electrical output configuration**
of the tool-side digital output ports. 
The PNP/NPN setting ensures proper compatibility between the robot’s output  
and the connected **industrial I/O devices** (e.g., sensors, solenoids, actuators).
