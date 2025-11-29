.. _enum_sub_program:

SUB_PROGRAM
------------------------------------------
This is an enumeration constant that means the operation of a sub-program in the robot controller and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SUB_PROGRAM_DELETE
     - Delete Sub Program

   * - 1
     - SUB_PROGRAM_SAVE
     - Save Sub Program

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum{
       SUB_PROGRAM_DELETE = 0,
       SUB_PROGRAM_SAVE,
   } SUB_PROGRAM;
