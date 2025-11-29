.. _manual_get_state_led_rule:

get_state_led_rule (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_state_led_rule <get_state_led_rule>` during **Manual (Teach)** operations.  
This function retrieves the **current LED rule index** applied to the controller.  
It is useful when verifying LED behavior or restoring controller defaults after manual override.

**Typical usage**

- Check which LED rule is currently active before or after manual color control.  
- Use to synchronize external UI indicators with the robot’s LED behavior.  
- Log LED rule index for diagnostics during teaching operations.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;
       drfl.open_connection("192.168.137.100");

       unsigned char rule = drfl.get_state_led_rule();
       cout << "[LED] Current LED rule index: " << (int)rule << endl;

       if (rule == 0)
           cout << "LED rule: Default system-managed behavior\n";
       else
           cout << "LED rule: Custom or user-defined behavior\n";

       return 0;
   }

This function provides insight into **the LED control state currently managed by the controller**,  
helping users maintain consistent visual feedback policies in teaching workflows.

**Tips**

- Useful for verifying whether LEDs are in **manual** or **controller-managed** mode.  
- Combine with :ref:`state_led_reset <state_led_reset>` to restore the default LED rule if needed.  
- Helps ensure consistent LED behavior between **manual** and **auto** modes.