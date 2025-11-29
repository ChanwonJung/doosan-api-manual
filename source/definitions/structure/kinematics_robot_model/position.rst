.. _struct_POSITION:
.. _struct_vector_6d:
.. _struct_position_addto_response:

POSITION
========

This structure defines a **basic Cartesian or joint-space position representation**  
used throughout motion, measurement, and calibration APIs.  
It stores a single pose as six floating-point values representing position and orientation.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[6]``
     - [mm, deg]
     - Target pose represented as (X, Y, Z, Rx, Ry, Rz)

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _POSITION
   {
       /* Target pose: X, Y, Z, Rx, Ry, Rz */
       float _fTargetPos[NUMBER_OF_JOINT];

   } POSITION, *LPPOSITION;

   typedef POSITION VECTOR6D, *LPVECTOR6D; 
   typedef POSITION POSITION_ADDTO_RESPONSE, *LPPOSITION_ADDTO_RESPONSE;
