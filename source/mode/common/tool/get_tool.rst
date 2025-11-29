.. _get_tool:

get_tool
------------------------------------------
This is a function for retrieving the tool information currently set in the robot controller.  
When there is no currently set tool, an empty character string is returned.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 887)

.. code-block:: cpp

    string get_tool() { return string(_get_tool(_rbtCtrl)); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - string
     - Name of the currently selected tool. |br| 
       If no tool is active, returns an empty string `""`.

**Example**

.. code-block:: cpp

   string strTool = drfl.get_tool();

   // Check the currently mounted tool
   if (strTool != "tool#1") {
       drfl.set_tool("tool#1");
   }

This example checks the currently mounted tool name using `get_tool()`,  
and sets the active tool to `"tool#1"` if it is not already selected.
