.. _get_tool_shape:

get_tool_shape
------------------------------------------
This function retrieves the **currently active tool shape** information that has been set in the robot controller.  
If no tool shape is currently active, an **empty string** is returned.  
This function is supported from **M2.4 version or higher**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 905)

.. code-block:: cpp

    string get_tool_shape() {
        return _get_tool_shape(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - string
     - Name of the currently active tool shape. |br| 
       Returns an empty string if no tool shape is selected.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Retrieve the name of the currently active tool shape
       string activeShape = drfl.get_tool_shape();

       if (activeShape.empty())
           printf("No tool shape is currently active.\n");
       else
           printf("Current tool shape: %s\n", activeShape.c_str());
   }

This example checks the currently active tool shape in the controller  
and prints its name to the console. If no shape is active, it displays a corresponding message.
