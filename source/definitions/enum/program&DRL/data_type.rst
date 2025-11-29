.. _enum_data_type:

DATA_TYPE
------------------------------------------
This is an enumeration constant that means the data type of the variable to be monitored by the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - DATA_TYPE_BOOL
     - boolean

   * - 1
     - DATA_TYPE_INT
     - integer

   * - 2
     - DATA_TYPE_FLOAT
     - float

   * - 3
     - DATA_TYPE_STRING
     - string

   * - 4
     - DATA_TYPE_POSJ
     - posj

   * - 5
     - DATA_TYPE_POSX
     - posx

   * - 6
     - DATA_TYPE_UNKNOWN
     - unknown

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum{
       DATA_TYPE_BOOL = 0,
       DATA_TYPE_INT,
       DATA_TYPE_FLOAT,
       DATA_TYPE_STRING,
       DATA_TYPE_POSJ,
       DATA_TYPE_POSX,
       DATA_TYPE_UNKNOWN,
   } DATA_TYPE;
