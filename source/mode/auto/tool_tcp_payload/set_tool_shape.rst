.. _auto_set_tool_shape:

set_tool_shape (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_tool_shape <set_tool_shape>`  
during **Auto (Run)** operations or system setup to define the  
**geometric shape** of the tool attached to the robot.  

Tool shape information is used by the controller for collision checks,  
workspace monitoring, simulation alignment, and improved motion planning.

**Typical usage**

- Register the tool’s 3D profile for workspace/layered safety monitoring.  
- Improve collision avoidance accuracy in complex environments.  
- Match virtual tool geometry in simulators (DART Platform, OEM software).  
- Update geometry when changing gripper fingers or tool attachments.

.. Note::

    - :ref:`TOOL_SHAPE <struct_config_tool_shape>` data typically includes size, dimensions, and shape type.  
    - Shape definition must correspond to the active tool set via ``set_tool``.  
    - Updating shape during motion is not recommended; apply at safe poses.  

**Example: Setting the Shape for a Parallel Gripper**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       TOOL_SHAPE shape;
       shape.eShape = TOOL_SHAPE_TYPE_BOX;
       shape.fSize[0] = 60.f;   // X (mm)
       shape.fSize[1] = 40.f;   // Y (mm)
       shape.fSize[2] = 120.f;  // Z (mm)

       // Apply the shape to the active tool
       if (!drfl.set_tool_shape(shape)) {
           printf("Failed to set tool shape.\n");
           return -1;
       }

       printf("Tool shape updated successfully.\n");
       return 0;
   }

In this example, a box-type tool shape is defined and applied  
to improve workspace monitoring accuracy in Auto Mode operations.
