.. _servo_off:

servo_off
------------------------------------------
This function turns off the **motor and brake power** of the robot (i.e., robot power off).  
It is typically used to safely stop the robot by cutting servo power, either through  
a **quick stop** or a **normal stop**, depending on the specified stop type.

This command is essential in both **emergency** and **controlled shutdown** situations  
to ensure mechanical safety and prevent undesired motion after program termination.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 909)

.. code-block:: cpp

    int servo_off(STOP_TYPE eStopType) {
        return _servo_off(_rbtCtrl, eStopType);
    };

**Parameter**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eStopType
     - :ref:`STOP_TYPE <enum_stop_type>`
     - -
     - Refer to the Definition of Enumeration Type

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to power off the servo
   * - 1
     - Success — servo power successfully turned off

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Perform a quick servo-off for immediate motion stop
        if (Drfl.servo_off(STOP_TYPE_QUICK))
            std::cout << "Servo power OFF (quick stop)\n";
        else
            std::cerr << "Failed to execute quick stop.\n";

        // Optional: perform slow servo-off for smooth deceleration
        Drfl.servo_off(STOP_TYPE_SLOW);

        return 0;
    }

This example demonstrates two different servo-off scenarios:  
(1) an **emergency quick stop** that immediately halts robot motion, and  
(2) a **controlled slow stop** that gradually decelerates the robot before cutting power.  
Both modes ensure safe power shutdown based on the robot’s current operation state.
