.. _set_palletizing_mode:

set_palletizing_mode
------------------------------------------
During palletizing application motion, **path tracking** and **velocity** can be maintained  
around the wrist singularity point using this function.  
There is no instability in the wrist singular region when the **B-axis** of the robot is  
commanded to 0° or 180°.

This mode improves motion smoothness and precision during repetitive pick-and-place  
or stacking operations in palletizing applications.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 916)

.. code-block:: cpp

    bool set_palletizing_mode(unsigned char iMode)
    {
        return _set_palletizing_mode(_rbtCtrl, iMode);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iMode
     - unsigned char
     - -
     - **Sets palletizing mode**  |br|
       0: disable palletizing mode |br|  
       1: enable palletizing mode |br|

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - fail — function call unsuccessful
   * - 1
     - success — palletizing mode changed successfully

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <thread>
    #include <chrono>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Enable palletizing mode
        // This stabilizes wrist motion near 0° or 180° to prevent singularities
        Drfl.set_palletizing_mode(1);

        // Move to the starting position of palletizing task
        float startPos[6] = {600, 0, 300, 180, 0, 180};
        float vel[2] = {50, 50};
        float acc[2] = {60, 60};
        // Drfl.movej(startPos, vel, acc);

        // Simulate repetitive stacking motion (pseudo-code)
        for (int i = 0; i < 3; ++i) {
            float placePos[6] = {600, i * 100.0f, 150, 180, 0, 180};
            // Drfl.movel(placePos, vel, acc);
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }

        // Disable palletizing mode after stacking operation
        Drfl.set_palletizing_mode(0);

        return 0;
    }

This example enables palletizing mode to stabilize wrist motion  
around singular angles (0° or 180°) during repetitive stacking tasks.  
After completing the operation, palletizing mode is disabled to  
return the robot to normal motion behavior.
