.. _struct_CONFIG_TOOL_ORIENTATION_LIMIT_ZONE:

CONFIG_TOOL_ORIENTATION_LIMIT_ZONE
======================================

This structure defines the **tool orientation limitation zones** used in the safety configuration.  
Each zone defines a geometric safety object along with a corresponding tool orientation limit.  
It ensures the robot tool maintains a safe direction when operating within specific spatial regions.

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
     - Zone validity flag |br| 
       (0: invalid, 1: valid)
   * - 10
     - ``_tZone[10]``
     - :ref:`SAFETY_OBJECT <struct_SAFETY_OBJECT>`
     - -
     - Safety object definition for each tool orientation zone
   * - 2670
     - ``_tLimit[10]``
     - :ref:`SAFETY_TOOL_ORIENTATION_LIMIT <struct_SAFETY_TOOL_ORIENTATION_LIMIT>`
     - -
     - Orientation limit (direction and angle) for each zone

Total size: 2,830 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL_ORIENTATION_LIMIT_ZONE
   {
       /* Zone validity: 0(invalid), 1(valid) */
       unsigned char _iValidity[10];

       /* Safety object zone definitions */
       SAFETY_OBJECT _tZone[10];

       /* Orientation limits per zone */
       SAFETY_TOOL_ORIENTATION_LIMIT _tLimit[10];

   } CONFIG_TOOL_ORIENTATION_LIMIT_ZONE, *LPCONFIG_TOOL_ORIENTATION_LIMIT_ZONE;

.. note::
   - Each entry combines a **safety object** (e.g., sphere, cuboid, capsule)  
     with a corresponding **tool orientation restriction**.
   - Used in conjunction with :ref:`SAFETY_TOOL_ORIENTATION_LIMIT <struct_SAFETY_TOOL_ORIENTATION_LIMIT>`  
     to prevent tool misalignment within defined spatial boundaries.
