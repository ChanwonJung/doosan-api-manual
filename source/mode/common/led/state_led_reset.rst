.. _state_led_reset:

state_led_reset
------------------------------------------
This function resets the robot's **state LED** to its default configuration and color.  
It clears any previously set LED state or user-defined color and restores  
the LED behavior defined by the default controller settings.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 994)

.. code-block:: cpp

    bool state_led_reset()
    {
        return _state_led_reset(_rbtCtrl);
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
     - Fail — LED reset request failed.
   * - 1
     - Success — LED successfully reset to default state.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Indicate that the robot is in "operation" mode by setting LED to green
        Drfl.set_state_led_color(0, 1, 0);  // Green color
        std::cout << "LED set to green: robot in operation mode." << std::endl;

        // Simulate task execution (e.g., motion or pick & place)
        std::this_thread::sleep_for(std::chrono::seconds(3));

        // Indicate task completion by setting LED to blue
        Drfl.set_state_led_color(0, 0, 1);  // Blue color
        std::cout << "LED set to blue: task complete." << std::endl;

        // After finishing all operations, reset LED to default system color
        Drfl.state_led_reset();
        std::cout << "LED reset to default system color." << std::endl;

        return 0;
    }

This example simulates LED usage for visual task indication.  
The LED is set to **green** during operation, changed to **blue** upon completion,  
and finally reset to its default color configuration using `state_led_reset()`.
