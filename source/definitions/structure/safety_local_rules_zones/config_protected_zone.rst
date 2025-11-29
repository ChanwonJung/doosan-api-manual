.. _struct_CONFIG_PROTECTED_ZONE:

CONFIG_PROTECTED_ZONE
=====================

This structure defines the **protected zone configuration** for safe workspace settings.  
Each protected zone represents an area that the robot must not enter or move beyond,  
typically used for creating virtual barriers around sensitive equipment or human workspaces.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iValidity[10]``
     - ``unsigned char[10]``
     - 0 or 1
     - Field validity flag |br| 
       (0: invalid, 1: valid)
   * - 10
     - ``_tZone[10]``
     - :ref:`SAFETY_OBJECT <struct_SAFETY_OBJECT>`
     - -
     - Definition of protected zone geometry and type

Total size: 1,030 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_PROTECTED_ZONE
   {
       /* Validity of each protected zone: 0(invalid), 1(valid) */
       unsigned char _iValidity[10];

       /* Safety object zone definitions */
       SAFETY_OBJECT _tZone[10];

   } CONFIG_PROTECTED_ZONE, *LPCONFIG_PROTECTED_ZONE;
