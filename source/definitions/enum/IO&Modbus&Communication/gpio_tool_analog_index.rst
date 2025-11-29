.. _enum_gpio_tool_analog_index:

GPIO_TOOL_ANALOG_INDEX
------------------------------------------
This is an enumeration type constant that refers to GPIO analog input/output terminal installed in the edge of the robot, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - GPIO_TOOL_ANALOG_INDEX_1
     - Robot Edge GPIO No. 1 Input/Output Port

   * - 1
     - GPIO_TOOL_ANALOG_INDEX_2
     - Robot Edge GPIO No. 2 Input/Output Port

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       GPIO_TOOL_ANALOG_INDEX_1 = 0,
       GPIO_TOOL_ANALOG_INDEX_2,
   } GPIO_TOOL_ANALOG_INDEX;
