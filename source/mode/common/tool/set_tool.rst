.. _set_tool:

set_tool
------------------------------------------
This is a function for setting the information on the tool currently mounted among the tool information registered in the robot controller in advance.  
When there is currently no tool mounted, if an empty character string is delivered, the currently set information is initialized.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 885)

.. code-block:: cpp

    bool set_tool(string strSymbol) {
        return _set_tool(_rbtCtrl, strSymbol.c_str());
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
     - Tool name to activate. Must match a pre-registered tool.  |br|
       If an empty string `""` is passed, current tool information is cleared. |br|


**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to select the tool 
   * - 1
     - Success — tool selection completed

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float fCog[3] = {10.0f, 10.0f, 10.0f};     // Center of gravity
       float fInertia[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};

       // (1) Register a new tool
       drfl.add_tool("tool#1", 5.3f, fCog, fInertia);

       // (2) Select that tool for use
       bool success = drfl.set_tool("tool#1");
       if (success)
           printf("Tool successfully set to tool#1\n");

       // (3) Remove tool registration
       drfl.del_tool("tool#1");
   }

This example registers a new tool ("tool#1"),
sets it as the active tool in the controller,
and then optionally clears or deletes the tool information.

.. note::
   If you call ``set_tool()`` and ``set_workpiece_weight()`` consecutively,  
   you **must insert a delay** using :ref:`mwait <mwait>` for at least ``transition_time`` seconds  
   to ensure the weight update is processed correctly.  
   Otherwise, the workpiece weight data may not be applied properly.
