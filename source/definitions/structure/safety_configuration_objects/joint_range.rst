.. _struct_JOINT_RANGE:

JOINT_RANGE
===========

This structure defines the **motion limits for each robot joint**,  
including maximum velocity, upper range, and lower range values.  
It is typically used as a substructure within :ref:`CONFIG_JOINT_RANGE <struct_CONFIG_JOINT_RANGE>`  
to specify joint limits in **Normal Mode** and **Reduced Mode**.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fMaxVelocity``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Maximum allowable joint velocity (°/s)
   * - 24
     - ``_fMaxRange``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Maximum angular position limit for each joint (°)
   * - 48
     - ``_fMinRange``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Minimum angular position limit for each joint (°)

Total size: 72 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _JOINT_RANGE
   {
       /* Maximum joint velocity (deg/s) */
       float _fMaxVelocity[NUMBER_OF_JOINT];

       /* Maximum joint angle (deg) */
       float _fMaxRange[NUMBER_OF_JOINT];

       /* Minimum joint angle (deg) */
       float _fMinRange[NUMBER_OF_JOINT];

   } JOINT_RANGE, *LPJOINT_RANGE;

.. note::
   - Each array contains 6 elements corresponding to the 6 robot joints.  
   - The velocity and range limits are used internally to enforce  
     safe motion boundaries during **joint-space control**.  
   - This structure is embedded within :ref:`CONFIG_JOINT_RANGE <struct_CONFIG_JOINT_RANGE>`  
     for mode-specific (Normal / Reduced) configurations.
