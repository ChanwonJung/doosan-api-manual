.. _struct_CONFIG_TOOL:

CONFIG_TOOL
============

This structure defines the **tool parameters** used in the robot controller,  
including its mass, center of mass, and inertia for dynamic compensation.  
It is typically applied when setting or modifying a tool attached to the robot flange.

.. list-table::
   :widths: 10 25 20 8 37
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fWeight``
     - ``float``
     - [kg]
     - Tool mass
   * - 4
     - ``_fXYZ``
     - ``float[3]``
     - [m]
     - Tool center of mass position (X, Y, Z)
   * - 16
     - ``_fInertia``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Tool inertia tensor values per joint

Total size: 40 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL
   {
       /* Tool mass [kg] */
       float _fWeight;
       /* Center of mass [m]: X, Y, Z */
       float _fXYZ[3];
       /* Tool inertia for each joint */
       float _fInertia[NUMBER_OF_JOINT];

   } CONFIG_TOOL, *LPCONFIG_TOOL;
