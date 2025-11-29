.. _get_state_led_rule:

get_state_led_rule
------------------------------------------
This function retrieves the **current LED color rule**  
that is applied to the robot arm’s state LED.

The return value represents the currently active LED color index  
according to the predefined LED color configuration.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 997)

.. code-block:: cpp

    unsigned char get_state_led_rule()
    {
        return _get_state_led_rule(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 20 60
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Off
   * - 1
     - Red
   * - 2
     - Green
   * - 3
     - Yellow
   * - 4
     - Blue
   * - 5
     - Magenta
   * - 6
     - Cyan
   * - 7
     - White

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Get the current LED color rule (0–7)
        unsigned char ledRule = Drfl.get_state_led_rule();

        // Display the meaning of the LED rule
        switch (ledRule) {
            case 1: std::cout << "LED indicates: GREEN — normal operation.\n"; break;
            case 2: std::cout << "LED indicates: YELLOW — caution or waiting state.\n"; break;
            case 4: std::cout << "LED indicates: BLUE — system ready.\n"; break;
            case 7: std::cout << "LED indicates: RED — error or protective stop.\n"; break;
            default: std::cout << "LED indicates: UNKNOWN or custom rule (" << (int)ledRule << ").\n"; break;
        }

        return 0;
    }

This example retrieves the **current LED rule value** using `get_state_led_rule()`  
and prints a corresponding message describing the robot’s current LED status.  
It allows the user to interpret the LED color state, such as **green for normal**  
or **red for error**, for quick visual diagnostics.
