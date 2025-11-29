.. _enum_gpio_analog_type:

GPIO_ANALOG_TYPE
------------------------------------------
This is an enumeration type constant that refers to the input/output type of the GPIO analog input/output terminal installed in the control box of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - GPIO_ANALOG_TYPE_CURRENT
     - Current Input/Output

   * - 1
     - GPIO_ANALOG_TYPE_VOLTAGE
     - Voltage Input/Output

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       GPIO_ANALOG_TYPE_CURRENT = 0,
       GPIO_ANALOG_TYPE_VOLTAGE
   } GPIO_ANALOG_TYPE;
