.. _set_safety_mode:

set_safety_mode
------------------------------------------
This function sets the **safety state** in the robot controller.  
It is used to change the robot’s operating mode (e.g., Manual / Auto)  
or to trigger specific safety-related events defined by the controller.

The function allows fine-grained control over the robot’s motion authorization,  
useful when switching between **teaching**, **manual**, or **automatic** operation modes.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 913)

.. code-block:: cpp

    bool set_safety_mode(SAFETY_MODE eSafetyMode, SAFETY_MODE_EVENT eSafetyEvent) {
        return _set_safety_mode(_rbtCtrl, eSafetyMode, eSafetyEvent);
    };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eSafetyMode
     - :ref:`SAFETY_MODE <enum_SAFETY_MODE>` 
     - -
     - Safety operation mode to set. 
   * - eSafetyEvent
     - :ref:`SAFETY_MODE_EVENT <enum_SAFETY_MODE_EVENT>`
     - -
     - Safety event type associated with the mode change.
     
**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to change the safety mode
   * - 1
     - Success — safety mode successfully updated

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Switch the robot into Manual Mode
        // with a motion event trigger to allow controlled movement.
        if (Drfl.set_safety_mode(SAFETY_MODE_MANUAL, SAFETY_MODE_EVENT_MOVE))
            std::cout << "Safety mode successfully set to MANUAL.\n";
        else
            std::cerr << "Failed to set safety mode.\n";

        return 0;
    }

This example demonstrates how to switch the robot’s safety state  
to **Manual Mode** with a **Move Event**, allowing motion under manual supervision.  
Such configurations are commonly used during **teaching or calibration** phases,  
where operators interact with the robot under controlled safety limits.
