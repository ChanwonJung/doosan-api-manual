.. _get_digital_input:

get_digital_input
------------------------------------------
This function reads the **current signal state** of a digital input port  
on the robot controller’s **control box**.  
It is used to check whether the specified input port is currently receiving  
a **high (ON)** or **low (OFF)** signal.

This function is typically used for monitoring external sensors, switches,  
or safety interlocks connected to the robot’s digital input terminals.

**Version Note** |br|
- If **DRCF version = 2**, this function internally calls ``_get_digital_input()``. |br|
- If **DRCF version = 3**, it calls ``_get_digital_input_ex()`` for extended I/O compatibility. |br|
Refer to :ref:`get_library_version <get_library_version>` for checking the current DRCF version.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 837/842)

.. code-block:: cpp

    #if DRCF_VERSION == 2
    bool get_digital_input(GPIO_CTRLBOX_DIGITAL_INDEX eGpioIndex) {
        return _get_digital_input(_rbtCtrl, eGpioIndex);
    };
    #elif DRCF_VERSION == 3
    bool get_digital_input(GPIO_CTRLBOX_DIGITAL_INDEX eGpioIndex) {
        return _get_digital_input_ex(_rbtCtrl, eGpioIndex);
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
     - Index of the digital input port on the control box.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - OFF — no signal detected (input is low)
   * - 1
     - ON — signal detected (input is high)

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Read the current signal of digital input #1
       bool bSignal = drfl.get_digital_input(GPIO_CTRLBOX_DIGITAL_INDEX_1);

       if (bSignal)
           printf("Digital input #1 is currently ON\n");
       else
           printf("Digital input #1 is currently OFF\n");
   }

This example checks whether **digital input #1** is currently active  
and prints the corresponding state to the console.  
It can be used to monitor signals from limit switches, sensors, or emergency stop circuits.
