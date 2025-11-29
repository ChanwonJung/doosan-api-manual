.. _struct_USER_COORDINATE:

USER_COORDINATE
===============

This is a structure for displaying the current user coordinate system information  
for the get_user_cart_coord command in the robot controller and consists of the following fields.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iReqId``
     - ``uchar``
     - 101~120
     - ID: 101~120 (Request ID)
   * - 1
     - ``_iTargetRef``
     - ``uchar``
     - 0x00, 0x02
     - Base: 0 / World: 2 (Coordinate Reference)
   * - 2
     - ``_fTargetPos[NUM_TASK]``
     - ``float``
     - -
     - Location Information

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _USER_COORDINATE
   {
       unsigned char _iReqId;           /* user coordinate ID: 101~120 */
       unsigned char _iTargetRef;       /* reference coordinate: base(0), world(2) */
       float         _fTargetPos[NUM_TASK]; /* coordinate pose (X, Y, Z, Rx, Ry, Rz) */
   } USER_COORDINATE, *LPUSER_COORDINATE;