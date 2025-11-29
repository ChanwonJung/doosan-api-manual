.. _set_state_led_color:

set_state_led_color
------------------------------------------
This function sets the **LED color state** of the robot arm by defining  
the intensity of each RGB (Red, Green, Blue) component.

Each color channel can be either **ON (1)** or **OFF (0)**,  
allowing for a combination of up to seven distinct LED colors.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 996)

.. code-block:: cpp

    bool set_state_led_color(int red, int green, int blue)
    {
        return _set_state_led_color(_rbtCtrl, red, green, blue);
    };

**Parameter**

.. list-table::
   :widths: 20 15 15 50
   :header-rows: 1

   * - **Parameter Name**
     - **Type**
     - **Default**
     - **Description**
   * - red
     - int
     - -
     - Red LED state (0 or 1)
   * - green
     - int
     - -
     - Green LED state (0 or 1)
   * - blue
     - int
     - -
     - Blue LED state (0 or 1)

**Color Combination Table**

.. list-table::
   :widths: 10 10 10 10 60
   :header-rows: 1

   * - **Enum #**
     - **R**
     - **G**
     - **B**
     - **Color**
   * - 0
     - 0
     - 0
     - 0
     - Off (no light)
   * - 1
     - 1
     - 0
     - 0
     - **RED**
   * - 2
     - 0
     - 1
     - 0
     - **GREEN**
   * - 3
     - 1
     - 1
     - 0
     - **YELLOW**
   * - 4
     - 0
     - 0
     - 1
     - **BLUE**
   * - 5
     - 1
     - 0
     - 1
     - **MAGENTA**
   * - 6
     - 0
     - 1
     - 1
     - **CYAN**
   * - 7
     - 1
     - 1
     - 1
     - **WHITE**

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Fail — LED color could not be set.
   * - 1
     - Success — LED color successfully changed.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Indicate robot initialization state — set LED to blue
        Drfl.set_state_led_color(0, 0, 1);  
        std::this_thread::sleep_for(std::chrono::seconds(2));

        // Indicate robot active/motion state — set LED to red
        Drfl.set_state_led_color(1, 0, 0);
        std::this_thread::sleep_for(std::chrono::seconds(3));

        // Indicate process completion — set LED to green
        Drfl.set_state_led_color(0, 1, 0);

        // Reset to default LED configuration
        Drfl.state_led_reset();

        return 0;
    }

This example demonstrates how to use the **state LED** to indicate different robot operation phases.  
The LED first turns **blue** during initialization, then **red** while in motion, and finally **green** when the process completes.  
Such color cues are useful for providing **visual feedback** about the robot’s operational state  
in collaborative or human-interactive environments.
