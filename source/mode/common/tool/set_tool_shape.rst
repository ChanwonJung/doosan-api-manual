.. _set_tool_shape:

set_tool_shape
------------------------------------------
This function activates a specific **tool shape configuration** among those registered in the Teach Pendant.  
It allows the robot to recognize the physical geometry of the mounted tool for collision detection or simulation purposes.  
This feature is available only in **M2.4 version or higher**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 903)

.. code-block:: cpp

    bool set_tool_shape(string strSymbol) {
        return _set_tool_shape(_rbtCtrl, strSymbol.c_str());
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strSymbol
     - string
     - -
     - The name of the tool shape to activate. |br| 
       Must correspond to one of the tool shapes registered in the Teach Pendant.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed — the specified tool shape was not found or activation failed.
   * - 1
     - Success — the tool shape has been successfully activated.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Activate a pre-registered tool shape
       drfl.set_tool_shape("tool_shape#1");
   }

This example activates the tool shape named `"tool_shape#1"`  
that was previously registered in the Teach Pendant,  
allowing the controller to apply the correct geometric model of the mounted tool.
