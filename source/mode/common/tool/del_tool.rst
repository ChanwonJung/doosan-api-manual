.. _del_tool:

del_tool
------------------------------------------
This is a function for deleting information on a tool that has been registered in the robot controller in advance.  
Once deleted, the tool information cannot be used until it is re-registered using :ref:`add_tool <add_tool>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 891)

.. code-block:: cpp

    bool del_tool(string strSymbol) {
        return _del_tool(_rbtCtrl, strSymbol.c_str());
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
     - Name of the tool to delete. Must match a tool that has been previously registered.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to delete the tool 
   * - 1
     - Success — tool successfully deleted from memory

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float fCog[3]     = {10.f, 10.f, 10.f};
       float fInertia[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};

       // (1) Register and activate a new tool
       drfl.add_tool("tool#1", 5.3f, fCog, fInertia);
       drfl.set_tool("tool#1");

       // (2) Delete the registered tool
       drfl.del_tool("tool#1");
   }

This example registers a new tool ("tool#1"),  
activates it, and then deletes its registration data from the controller memory.
