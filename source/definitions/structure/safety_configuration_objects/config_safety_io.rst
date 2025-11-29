.. _struct_CONFIG_SAFETY_IO:

CONFIG_SAFETY_IO
================

This structure defines the **safety I/O configuration map** used by the robot’s safety controller.  
It specifies the logical mapping and current state of all safety-related **input/output ports**  
and consists of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iIO[TYPE_LAST][NUM_SAFETY]``
     - ``unsigned char[2][8]``
     - -
     - 16 safety controller I/O ports

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_SAFETY_IO
   {
       /* Safety I/O state map
          [0] : Input channel set (8 ports)
          [1] : Output channel set (8 ports)
       */
       unsigned char _iIO[TYPE_LAST][NUM_SAFETY];
   } CONFIG_SAFETY_IO, *LPCONFIG_SAFETY_IO;