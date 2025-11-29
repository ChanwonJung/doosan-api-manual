.. _enum_gpio_ctrlbox_digital_index:

GPIO_CTRLBOX_DIGITAL_INDEX
------------------------------------------
This is an enumeration type constant that refers to the GPIO digital input/output terminal installed in the control box of the robot controller, and is defined as follows.

v2 controller : 0–15 |br|
v3 controller : 0–31  

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - GPIO_CTRLBOX_DIGITAL_INDEX_1
     - Control Box GPIO No. 1 Input/Output Port
   * - 1
     - GPIO_CTRLBOX_DIGITAL_INDEX_2
     - Control Box GPIO No. 2 Input/Output Port
   * - 2
     - GPIO_CTRLBOX_DIGITAL_INDEX_3
     - Control Box GPIO No. 3 Input/Output Port
   * - 3
     - GPIO_CTRLBOX_DIGITAL_INDEX_4
     - Control Box GPIO No. 4 Input/Output Port
   * - 4
     - GPIO_CTRLBOX_DIGITAL_INDEX_5
     - Control Box GPIO No. 5 Input/Output Port
   * - 5
     - GPIO_CTRLBOX_DIGITAL_INDEX_6
     - Control Box GPIO No. 6 Input/Output Port
   * - 6
     - GPIO_CTRLBOX_DIGITAL_INDEX_7
     - Control Box GPIO No. 7 Input/Output Port
   * - 7
     - GPIO_CTRLBOX_DIGITAL_INDEX_8
     - Control Box GPIO No. 8 Input/Output Port
   * - 8
     - GPIO_CTRLBOX_DIGITAL_INDEX_9
     - Control Box GPIO No. 9 Input/Output Port
   * - 9
     - GPIO_CTRLBOX_DIGITAL_INDEX_10
     - Control Box GPIO No. 10 Input/Output Port
   * - 10
     - GPIO_CTRLBOX_DIGITAL_INDEX_11
     - Control Box GPIO No. 11 Input/Output Port
   * - 11
     - GPIO_CTRLBOX_DIGITAL_INDEX_12
     - Control Box GPIO No. 12 Input/Output Port
   * - 12
     - GPIO_CTRLBOX_DIGITAL_INDEX_13
     - Control Box GPIO No. 13 Input/Output Port
   * - 13
     - GPIO_CTRLBOX_DIGITAL_INDEX_14
     - Control Box GPIO No. 14 Input/Output Port
   * - 14
     - GPIO_CTRLBOX_DIGITAL_INDEX_15
     - Control Box GPIO No. 15 Input/Output Port
   * - 15
     - GPIO_CTRLBOX_DIGITAL_INDEX_16
     - Control Box GPIO No. 16 Input/Output Port
   * - 16
     - GPIO_CTRLBOX_DIGITAL_INDEX_17
     - Control Box GPIO No. 17 Input/Output Port
   * - 17
     - GPIO_CTRLBOX_DIGITAL_INDEX_18
     - Control Box GPIO No. 18 Input/Output Port
   * - 18
     - GPIO_CTRLBOX_DIGITAL_INDEX_19
     - Control Box GPIO No. 19 Input/Output Port
   * - 19
     - GPIO_CTRLBOX_DIGITAL_INDEX_20
     - Control Box GPIO No. 20 Input/Output Port
   * - 20
     - GPIO_CTRLBOX_DIGITAL_INDEX_21
     - Control Box GPIO No. 21 Input/Output Port
   * - 21
     - GPIO_CTRLBOX_DIGITAL_INDEX_22
     - Control Box GPIO No. 22 Input/Output Port
   * - 22
     - GPIO_CTRLBOX_DIGITAL_INDEX_23
     - Control Box GPIO No. 23 Input/Output Port
   * - 23
     - GPIO_CTRLBOX_DIGITAL_INDEX_24
     - Control Box GPIO No. 24 Input/Output Port
   * - 24
     - GPIO_CTRLBOX_DIGITAL_INDEX_25
     - Control Box GPIO No. 25 Input/Output Port
   * - 25
     - GPIO_CTRLBOX_DIGITAL_INDEX_26
     - Control Box GPIO No. 26 Input/Output Port
   * - 26
     - GPIO_CTRLBOX_DIGITAL_INDEX_27
     - Control Box GPIO No. 27 Input/Output Port
   * - 27
     - GPIO_CTRLBOX_DIGITAL_INDEX_28
     - Control Box GPIO No. 28 Input/Output Port
   * - 28
     - GPIO_CTRLBOX_DIGITAL_INDEX_29
     - Control Box GPIO No. 29 Input/Output Port
   * - 29
     - GPIO_CTRLBOX_DIGITAL_INDEX_30
     - Control Box GPIO No. 30 Input/Output Port
   * - 30
     - GPIO_CTRLBOX_DIGITAL_INDEX_31
     - Control Box GPIO No. 31 Input/Output Port
   * - 31
     - GPIO_CTRLBOX_DIGITAL_INDEX_32
     - Control Box GPIO No. 32 Input/Output Port

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   // V2 : Input 16, Output 16
   // V3 : Input 20, Output 16 
   typedef enum {
       GPIO_CTRLBOX_DIGITAL_INDEX_1 = 0,
       GPIO_CTRLBOX_DIGITAL_INDEX_2,
       GPIO_CTRLBOX_DIGITAL_INDEX_3,
       GPIO_CTRLBOX_DIGITAL_INDEX_4,
       GPIO_CTRLBOX_DIGITAL_INDEX_5,
       GPIO_CTRLBOX_DIGITAL_INDEX_6,
       GPIO_CTRLBOX_DIGITAL_INDEX_7,
       GPIO_CTRLBOX_DIGITAL_INDEX_8,
       GPIO_CTRLBOX_DIGITAL_INDEX_9,
       GPIO_CTRLBOX_DIGITAL_INDEX_10,
       GPIO_CTRLBOX_DIGITAL_INDEX_11,
       GPIO_CTRLBOX_DIGITAL_INDEX_12,
       GPIO_CTRLBOX_DIGITAL_INDEX_13,
       GPIO_CTRLBOX_DIGITAL_INDEX_14,
       GPIO_CTRLBOX_DIGITAL_INDEX_15,
       GPIO_CTRLBOX_DIGITAL_INDEX_16,
       GPIO_CTRLBOX_DIGITAL_INDEX_17,
       GPIO_CTRLBOX_DIGITAL_INDEX_18,
       GPIO_CTRLBOX_DIGITAL_INDEX_19,
       GPIO_CTRLBOX_DIGITAL_INDEX_20,
       GPIO_CTRLBOX_DIGITAL_INDEX_21,
       GPIO_CTRLBOX_DIGITAL_INDEX_22,
       GPIO_CTRLBOX_DIGITAL_INDEX_23,
       GPIO_CTRLBOX_DIGITAL_INDEX_24,
       GPIO_CTRLBOX_DIGITAL_INDEX_25,
       GPIO_CTRLBOX_DIGITAL_INDEX_26,
       GPIO_CTRLBOX_DIGITAL_INDEX_27,
       GPIO_CTRLBOX_DIGITAL_INDEX_28,
       GPIO_CTRLBOX_DIGITAL_INDEX_29,
       GPIO_CTRLBOX_DIGITAL_INDEX_30,
       GPIO_CTRLBOX_DIGITAL_INDEX_31,
       GPIO_CTRLBOX_DIGITAL_INDEX_32,
   } GPIO_CTRLBOX_DIGITAL_INDEX;
