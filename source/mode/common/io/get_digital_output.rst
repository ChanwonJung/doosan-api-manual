.. _get_digital_output:

get_digital_output
------------------------------------------
This function reads the **current signal state** of a digital output port  
on the robot controller’s **control box**. It is used to check whether the  
specified digital output is currently **ON (1)** or **OFF (0)**.

This function is useful for verifying signal states before sending commands,  
or for debugging I/O operations during automated sequences.

**Version Note** |br|
- If **DRCF version = 2**, this function internally calls ``_get_digital_output()``. |br|
- If **DRCF version = 3**, it calls ``_get_digital_output_ex()`` for extended I/O access. |br|
Refer to :ref:`get_library_version <get_library_version>` for checking the current DRCF version.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 836/841)

.. code-block:: cpp

    #if DRCF_VERSION == 2
    bool get_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX eGpioIndex) {
        return _get_digital_output(_rbtCtrl, eGpioIndex);
    };
    #elif DRCF_VERSION == 3
    bool get_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX eGpioIndex) {
        return _get_digital_output_ex(_rbtCtrl, eGpioIndex);
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
     - Index of the digital output port on the control box.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - OFF — output signal is currently low (inactive)
   * - 1
     - ON — output signal is currently high (active)

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Check the state of digital output #1
       bool bSignal = drfl.get_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1);

       if (bSignal)
           printf("Digital output #1 is currently ON\n");
       else
           printf("Digital output #1 is currently OFF\n");
   }

This example reads the state of **digital output #1** on the control box  
and prints whether the port is currently active (ON) or inactive (OFF).
