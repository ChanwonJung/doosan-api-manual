.. _enum_variable_type:

VARIABLE_TYPE
------------------------------------------
It is an enumeration constant that means the type of variable to be monitored by the robot controller and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - VARIABLE_TYPE_INSTALL
     - Installation Variable

   * - 1
     - VARIABLE_TYPE_GLOBAL
     - Global Variable

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum{
       VARIABLE_TYPE_INSTALL = 0,
       VARIABLE_TYPE_GLOBAL,    
   } VARIABLE_TYPE;
