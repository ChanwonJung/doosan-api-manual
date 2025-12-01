.. _set_auto_servo_off:

set_auto_servo_off
------------------------------------------
This function enables or disables the **automatic servo-off** transition feature  
in the robot controller. When enabled, the controller will automatically  
turn off the servo power if the robot remains idle for a specified duration.

This feature is useful for improving **safety and energy efficiency**,  
especially when the robot is not in continuous operation.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 914)

.. code-block:: cpp

    bool set_auto_servo_off(bool bFuncEnable, float fElapseTime) {
        return _set_auto_servo_off(_rbtCtrl, bFuncEnable, fElapseTime);
    };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bFuncEnable
     - bool
     - -
     - **Enables or disables the auto servo-off feature** |br|
       false (0): Disable auto servo-off |br|
       true (1): Enable auto servo-off
   * - fElapseTime
     - float
     - -
     - Duration (in **minutes**) of inactivity before servo power is turned off.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to configure the auto servo-off setting
   * - 1
     - Success — setting successfully applied

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Enable the auto servo-off function after 3 minutes of inactivity
        if (Drfl.set_auto_servo_off(true, 3.0f))
            std::cout << "Auto servo-off enabled (timeout: 3 minutes)\n";
        else
            std::cerr << "Failed to set auto servo-off behavior.\n";

        // Later, disable the function to keep servo always active
        Drfl.set_auto_servo_off(false, 0.0f);

        return 0;
    }

This example enables the **auto servo-off** function,  
causing the robot’s servo power to shut down automatically  
after **3 minutes of inactivity**. The feature can later be disabled  
by calling the function again with `bFuncEnable = false`.
