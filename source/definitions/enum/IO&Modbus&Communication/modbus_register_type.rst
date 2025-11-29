.. _enum_modbus_register_type:

MODBUS_REGISTER_TYPE
------------------------------------------
This is an enumeration type constant about the modbus register type that can be registered in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MODBUS_REGISTER_TYPE_DISCRETE_INPUTS
     - Discrete Input

   * - 1
     - MODBUS_REGISTER_TYPE_COILS
     - Coils

   * - 2
     - MODBUS_REGISTER_TYPE_INPUT_REGISTER
     - Input Register

   * - 3
     - MODBUS_REGISTER_TYPE_HOLDING_REGISTER
     - Holding Register

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MODBUS_REGISTER_TYPE_DISCRETE_INPUTS = 0,
       MODBUS_REGISTER_TYPE_COILS,
       MODBUS_REGISTER_TYPE_INPUT_REGISTER,
       MODBUS_REGISTER_TYPE_HOLDING_REGISTER,
   } MODBUS_REGISTER_TYPE;
