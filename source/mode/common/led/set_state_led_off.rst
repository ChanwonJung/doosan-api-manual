.. _set_state_led_off:

set_state_led_off
------------------------------------------
This function turns **OFF** the state LED on the robot arm.  
It disables the LED light completely, regardless of its previously set color or rule configuration.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 995)

.. code-block:: cpp

    bool set_state_led_off()
    {
        return _set_state_led_off(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Fail — failed to turn off the LED
   * - 1
     - Success — LED successfully turned off

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Set LED to red to indicate an active warning state
        Drfl.set_state_led_color(1, 0, 0);  // Red color
        std::cout << "LED set to red: warning active." << std::endl;

        // Simulate a few seconds of system alert
        std::this_thread::sleep_for(std::chrono::seconds(2));

        // Turn off all LED lights (e.g., entering standby or power-save mode)
        Drfl.set_state_led_off();
        std::cout << "LED lights turned off for standby mode." << std::endl;

        // Wait and then reset LED to system default when resuming operation
        std::this_thread::sleep_for(std::chrono::seconds(2));
        Drfl.state_led_reset();
        std::cout << "LED restored to default system color." << std::endl;

        return 0;
    }

This example demonstrates how to **turn off the robot arm's LED lights**  
when entering a standby or power-save mode.  
After displaying a red warning state, all LEDs are turned off using  
`set_state_led_off()`, and later restored to the default system configuration.
