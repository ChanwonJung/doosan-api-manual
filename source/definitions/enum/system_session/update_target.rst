.. _enum_update_target:

UPDATE_TARGET
------------------------------------------
This is an enumeration type constant defines the target modules that can be updated in the robot controller system.

.. list-table:: 
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - UPDATE_TARGET_FIRST
     - Represents the first update target index. |br|
       Alias of ``UPDATE_TARGET_INVETER_1``.

   * - 1
     - UPDATE_TARGET_INVETER_1
     - Inverter board of Joint #1.

   * - 2
     - UPDATE_TARGET_INVETER_2
     - Inverter board of Joint #2.

   * - 3
     - UPDATE_TARGET_INVETER_3
     - Inverter board of Joint #3.

   * - 4
     - UPDATE_TARGET_INVETER_4
     - Inverter board of Joint #4.

   * - 5
     - UPDATE_TARGET_INVETER_5
     - Inverter board of Joint #5.

   * - 6
     - UPDATE_TARGET_INVETER_6
     - Inverter board of Joint #6.

   * - 7
     - UPDATE_TARGET_INVETER_LAST
     - Represents the last inverter board index. |br| 
       Alias of ``UPDATE_TARGET_INVETER_6``.

   * - 8
     - UPDATE_TARGET_SAFETYBD
     - Safety board module of the controller.

   * - 9
     - UPDATE_TARGET_CONTROLLER
     - Main controller board (CPU board).

   * - 10
     - UPDATE_TARGET_SVM
     - Smart Vision Module (SVM) or external vision processing unit.

   * - 11
     - UPDATE_TARGET_LAST
     - Internal end marker of the UPDATE_TARGET enumeration. |br|  
       Used to define the total number of update targets and  |br|
       for iteration or boundary checking within the firmware.


**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum
   {
       UPDATE_TARGET_FIRST      = 0,
       UPDATE_TARGET_INVETER_1  = UPDATE_TARGET_FIRST,
       UPDATE_TARGET_INVETER_2  = 1,
       UPDATE_TARGET_INVETER_3  = 2,
       UPDATE_TARGET_INVETER_4  = 3,
       UPDATE_TARGET_INVETER_5  = 4,
       UPDATE_TARGET_INVETER_6  = 5,
       UPDATE_TARGET_INVETER_LAST = UPDATE_TARGET_INVETER_6,
       UPDATE_TARGET_SAFETYBD   = 6,
       UPDATE_TARGET_CONTROLLER = 7,
       UPDATE_TARGET_SVM        = 8,
       UPDATE_TARGET_LAST       = 9,
   } UPDATE_TARGET;