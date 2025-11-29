.. _auto_add_tool:

add_tool (Auto Mode)
------------------------------------------
This section explains how to use :ref:`add_tool <add_tool>`  
in **Auto (Run)** operations or initialization routines to register a **new tool**  
(end-effector) on the robot controller.  

A tool definition includes weight, center of gravity (CoG), and inertia information,  
all of which are necessary for accurate trajectory generation and force estimation.
Once registered, a tool can be activated using :ref:`set_tool <set_tool>`.

**Typical usage**

- Register a new gripper, probe, or custom end-effector.  
- Load tool data measured from Smart Setup or CAD specifications.  
- Prepare multiple tool configurations for automated tool-changing processes.  
- Initialize tool definitions during system startup or commissioning.

.. Note::

    - ``strSymbol`` must be unique across all tool names.  
    - Weight and CoG values should match the physical tool as closely as possible.  
    - Tool registration is typically performed once—not every cycle.

**Example: Registering a New Tool Configuration**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float cog[3]     = {0.f, 0.f, 40.f};       // in mm relative to flange/TCP
       float inertia[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};

       // Register a new tool
       if (drfl.add_tool("NEW_END_EFFECTOR", 1.2f, cog, inertia)) {
           printf("Tool registered successfully.\n");
       } else {
           printf("Failed to register tool.\n");
           return -1;
       }

       // Select the new tool for Auto Mode operation
       drfl.set_tool("NEW_END_EFFECTOR");

       return 0;
   }

In this example, a new tool is created and then enabled for  
subsequent Auto Mode motion using ``set_tool()``.

**Tips**

- Register all tools during initialization, then switch tools using ``set_tool``.  
- Use accurate mass/CoG values to ensure safe motion and torque estimation.  
- Store tool symbols in a central recipe table for multi-tool automation.
