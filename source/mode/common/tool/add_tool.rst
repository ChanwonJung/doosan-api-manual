.. _add_tool:

add_tool
------------------------------------------
This is a function for registering tool information that will be mounted on the flange of the robot.  
The tool information includes **name, weight, center of gravity, and inertia**, and is stored in the robot controller’s memory.  
The data remains available until reboot, unless saved and restored through the T/P initialization process.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 889)

.. code-block:: cpp

    bool add_tool(string strSymbol, float fWeight, float fCog[3], float fInertia[NUM_TASK]) {
        return _add_tool(_rbtCtrl, strSymbol.c_str(), fWeight, fCog, fInertia);
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
     - Tool name (unique identifier for registration).
   * - fWeight
     - float
     - -
     - Tool weight in kilograms.
   * - fCog
     - float[3]
     - -
     - Center of gravity of the tool in millimeters.
   * - fInertia
     - float[6]
     - -
     - Inertia tensor values (Ixx, Iyy, Izz, Ixy, Ixz, Iyz).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to register the tool
   * - 1
     - Success — tool successfully registered in memory

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float fCog[3]     = {10.f, 10.f, 10.f};
       float fInertia[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};

       // (1) Register a new tool
       bool success = drfl.add_tool("tool#1", 5.3f, fCog, fInertia);

       // (2) Set it as the active tool
       if (success)
           drfl.set_tool("tool#1");

       // (3) Remove the tool registration
       drfl.del_tool("tool#1");
   }

This example registers a new tool (“tool#1”) with its weight,  
center of gravity, and inertia data, then activates it and finally deletes the registration.
