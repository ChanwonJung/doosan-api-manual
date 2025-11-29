.. _struct_ROBOT_VEL:

ROBOT_VEL
==========

This is a structure for expressing velocity information of the robot controller, and is composed of the following fields.

.. list-table::
   :widths: 15 28 18 8 31
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fVelocity``
     - ``float[NUM_JOINT]``
     - Six Velocity Information Items
     - Velocity Information (X, Y, Z, RX, RY, RZ)

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_VEL
   {
       float _fVelocity[NUM_JOINT];  /* current velocity: six components */
   } ROBOT_VEL, *LPROBOT_VEL;
