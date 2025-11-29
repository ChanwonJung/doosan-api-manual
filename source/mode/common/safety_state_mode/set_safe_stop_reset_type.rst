.. _set_safe_stop_reset_type:

set_safe_stop_reset_type
------------------------------------------
This function defines the **motion reset behavior** after a **Safe Stop** condition  
occurs in the robot controller.  

When the robot enters the **SAFE_STOP** state, this setting determines whether  
the robot should **automatically replay**, **hold**, or **wait for a manual reset**  
after recovery from the stop condition.

If the robot is in **automatic mode**, this setting is applied and motion replay  
can be defined. However, in **manual mode**, this configuration is ignored.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 741)

.. code-block:: cpp

    bool set_safe_stop_reset_type(SAFE_STOP_RESET_TYPE eResetType = SAFE_STOP_RESET_TYPE_DEFAULT) {
        return _set_safe_stop_reset_type(_rbtCtrl, eResetType);
    }

**Parameter**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eResetType
     - :ref:`SAFE_STOP_RESET_TYPE <enum_safe_stop_reset_type>`
     - SAFE_STOP_RESET_TYPE_DEFAULT
     - Type of reset motion after a Safe Stop.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to set reset type
   * - 1
     - Success — successfully updated safe stop reset behavior

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // When a Safe Stop occurs, define the post-stop behavior
        // Option 1: Resume the paused DRL program automatically
        if (Drfl.set_safe_stop_reset_type(SAFE_STOP_RESET_TYPE_PROGRAM_RESUME))
            std::cout << "Safe stop reset type set to PROGRAM_RESUME.\n";
        else
            std::cerr << "Failed to configure safe stop reset type.\n";

        // Option 2: Default stop — manual restart required
        Drfl.set_safe_stop_reset_type(SAFE_STOP_RESET_TYPE_DEFAULT);

        return 0;
    }

This example sets the robot’s **safe stop reset type** to  
`SAFE_STOP_RESET_TYPE_PROGRAM_RESUME`, enabling the robot to  
**automatically resume motion** after recovering from a safe stop.  
If manual confirmation is preferred, use `SAFE_STOP_RESET_TYPE_DEFAULT` instead.
