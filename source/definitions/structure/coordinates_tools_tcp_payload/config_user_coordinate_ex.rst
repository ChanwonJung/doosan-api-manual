.. _struct_CONFIG_USER_COORDINATE_EX:

CONFIG_USER_COORDINATE_EX
=========================
This structure is used to define a **user coordinate frame**,  
specifying the reference coordinate system, target position, and user-defined ID.  
It is typically used to register or modify a user coordinate in the robot controller.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetRef``
     - ``unsigned char``
     - -
     - Base: 0 / World: 2 (Coordinate Reference)
   * - 1
     - ``_fTargetPos``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Target position in task coordinates
   * - 25
     - ``_iUserID``
     - ``unsigned char``
     - -
     - Unified user coordinate ID

Total size: 26 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_USER_COORDINATE_EX
   {
       /* base: 0, world: 2 */
       unsigned char _iTargetRef;
       /* task position */
       float _fTargetPos[NUMBER_OF_JOINT];
       /* unified id */
       unsigned char _iUserID;
   } CONFIG_USER_COORDINATE_EX, *LPCONFIG_USER_COORDINATE_EX;