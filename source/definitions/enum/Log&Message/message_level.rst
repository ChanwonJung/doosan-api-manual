.. _enum_message_level:

MESSAGE_LEVEL
------------------------------------------
This is an enumeration constant that means the type of message to be provided to the user.  
It is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MESSAGE_LEVEL_INFO
     - Information

   * - 1
     - MESSAGE_LEVEL_WARN
     - Warning

   * - 2
     - MESSAGE_LEVEL_ALARM
     - Error

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MESSAGE_LEVEL_INFO,
       MESSAGE_LEVEL_WARN,
       MESSAGE_LEVEL_ALARM
   } MESSAGE_LEVEL;
