.. _set_digital_output:

set_digital_output
------------------------------------------
This function outputs a digital signal to a specified output port  
on the **control box** of the robot. The signal can be turned **ON (1)** or **OFF (0)**  
using the digital output index provided as a parameter.

It is primarily used to control external equipment such as pneumatic valves,  
indicators, or other peripheral devices connected to the controller’s digital I/O interface.

**Version Note** |br|
- If **DRCF version = 2**, this function internally calls ``_set_digital_output()``. |br|
- If **DRCF version = 3**, it calls ``_set_digital_output_ex()`` for extended I/O support. |br|
Refer to the controller firmware version in :ref:`get_library_version <get_library_version>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 838/843)

.. code-block:: cpp

    #if DRCF_VERSION == 2
    bool set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX eGpioIndex, bool bOnOff) {
        return _set_digital_output(_rbtCtrl, eGpioIndex, bOnOff);
    };
    #elif DRCF_VERSION == 3
    bool set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX eGpioIndex, bool bOnOff) {
        return _set_digital_output_ex(_rbtCtrl, eGpioIndex, bOnOff);
    };
    #endif

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eGpioIndex
     - :ref:`GPIO_CTRLBOX_DIGITAL_INDEX <enum_gpio_ctrlbox_digital_index>`
     - -
     - Digital output port index on the control box.  
   * - bOnOff
     - bool
     - -
     - **Output state value** |br|
       `true (1)` : ON — output high signal |br| 
       `false (0)` : OFF — output low signal

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to output signal
   * - 1
     - Success — signal successfully output at target port

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Turn ON digital output #1 on the control box
       drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, true);

       // Wait for 2 seconds
       std::this_thread::sleep_for(std::chrono::seconds(2));

       // Turn OFF digital output #1
       drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, false);
   }

This example activates the digital output channel **#1** on the robot controller,  
holds the signal for 2 seconds, and then turns it off — demonstrating how to toggle  
a digital line for controlling external devices such as relays or actuators.
