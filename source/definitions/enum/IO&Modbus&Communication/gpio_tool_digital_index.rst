.. _enum_gpio_tool_digital_index:

GPIO_TOOL_DIGITAL_INDEX
------------------------------------------
This is an enumeration type constant that refers to the GPIO digital input/output terminal installed in the edge of the robot, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - GPIO_TOOL_DIGITAL_INDEX_1
     - Robot Edge GPIO No. 1 Input/Output Port

   * - 1
     - GPIO_TOOL_DIGITAL_INDEX_2
     - Robot Edge GPIO No. 2 Input/Output Port

   * - 2
     - GPIO_TOOL_DIGITAL_INDEX_3
     - Robot Edge GPIO No. 3 Input/Output Port

   * - 3
     - GPIO_TOOL_DIGITAL_INDEX_4
     - Robot Edge GPIO No. 4 Input/Output Port

   * - 4
     - GPIO_TOOL_DIGITAL_INDEX_5
     - Robot Edge GPIO No. 5 Input/Output Port

   * - 5
     - GPIO_TOOL_DIGITAL_INDEX_6
     - Robot Edge GPIO No. 6 Input/Output Port

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       GPIO_TOOL_DIGITAL_INDEX_1 = 0,
       GPIO_TOOL_DIGITAL_INDEX_2,
       GPIO_TOOL_DIGITAL_INDEX_3,
       GPIO_TOOL_DIGITAL_INDEX_4,
       GPIO_TOOL_DIGITAL_INDEX_5,
       GPIO_TOOL_DIGITAL_INDEX_6,
   } GPIO_TOOL_DIGITAL_INDEX;
