.. _struct_CONFIG_TCP:

CONFIG_TCP
===========

This is a structure for setting or representing the **Tool Center Point (TCP)** configuration  
in the robot controller and consists of the following field.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - Target Pose
     - ``float[NUM_JOINT]``
     - -
     - TCP position and orientation (X, Y, Z, Rx, Ry, Rz)

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TCP
   {
       /* TCP pose: X, Y, Z, Rx, Ry, Rz */
       float _fTargetPos[NUM_JOINT];   /* target pose */
   } CONFIG_TCP, *LPCONFIG_TCP;