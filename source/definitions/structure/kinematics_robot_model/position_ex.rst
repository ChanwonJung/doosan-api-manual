.. _struct_POSITION_EX:
.. _struct_CONFIG_TCP_EX:

POSITION_EX
============

This structure defines an **extended robot position representation**  
that supports both **joint space (posj)** and **task space (posx)** formats.  
It extends the standard position structure by adding orientation type,  
solution space, and multi-turn information for advanced kinematic representation.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_posj._pos``
     - ``float[NUMBER_OF_JOINT]``
     - [deg]
     - Joint position data for all robot joints |br|
       (used when position type = ``posj``)
   * - 0
     - ``_posx._pos``
     - ``float[NUMBER_OF_TASK_EX]``
     - [mm, deg]
     - Cartesian task position (X, Y, Z, Rx, Ry, Rz, …)
   * - 24
     - ``_posx._ori_type``
     - ``unsigned char``
     - 0-5
     - Orientation type |br|
       0: Euler ZYZ, 1: Euler ZYX, 2: Euler XYZ |br|
       3: Fixed XYZ, 4: Axis-Angle, 5: Quaternion 
   * - 25
     - ``_posx._sol_space``
     - ``unsigned char``
     - 0-7, 255
     - Solution space configuration |br| 
       0-7: fixed, 255: automatic
   * - 26
     - ``_posx._multi_turn``
     - ``unsigned char``
     - 0-255
     - Multi-turn joint setting (255 = automatic)
   * - 27
     - ``_pos_type``
     - ``unsigned char``
     - -
     - Position type indicator |br|  
       0: posx, 1: posj

Total size: 28 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _POSITION_EX
   {
       union {
           /* Joint-space position (posj) */
           struct {
               float _pos[NUMBER_OF_JOINT];  /* Joint position [deg] */
           } _posj;

           /* Task-space position (posx) */
           struct {
               float         _pos[NUMBER_OF_TASK_EX]; /* Task position [mm, deg] */
               unsigned char _ori_type;   /* 0: ZYZ, 1: ZYX, 2: XYZ, 3: Fixed XYZ, 4: Axis-Angle, 5: Quaternion */
               unsigned char _sol_space;  /* 0~7: fixed, 255: auto */
               unsigned char _multi_turn; /* 255: auto */
           } _posx;
       };

       unsigned char _pos_type;  /* Position type (0: posx, 1: posj) */

   } POSITION_EX, *LPPOSITION_EX;  // SUPPORT_ORIENTATION_TYPE

    typedef POSITION_EX CONFIG_TCP_EX, *LPCONFIG_TCP_EX; // SUPPORT_ORIENTATION_TYPE