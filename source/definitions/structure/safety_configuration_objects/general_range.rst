.. _struct_GENERAL_RANGE:

GENERAL_RANGE
=============

This structure defines the **global physical safety limits** of the robot,  
including allowable maximum force, power, speed, and momentum values.  
It is used within :ref:`CONFIG_GENERAL_RANGE <struct_CONFIG_GENERAL_RANGE>`  
to configure overall safety thresholds applied during motion execution.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fMaxForce``
     - ``float``
     - -
     - Maximum allowable external force (N)
   * - 4
     - ``_fMaxPower``
     - ``float``
     - -
     - Maximum power limit (W)
   * - 8
     - ``_fMaxSpeed``
     - ``float``
     - -
     - Maximum speed limit (mm/s)
   * - 12
     - ``_fMaxMomentum``
     - ``float``
     - -
     - Maximum momentum limit (kg·m/s)

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _GENERAL_RANGE
   {
       /* Maximum allowable external force (N) */
       float _fMaxForce;

       /* Maximum power limit (W) */
       float _fMaxPower;

       /* Maximum robot speed (mm/s) */
       float _fMaxSpeed;

       /* Maximum momentum (kg·m/s) */
       float _fMaxMomentum;

   } GENERAL_RANGE, *LPGENERAL_RANGE;

.. note::
   - This structure is typically used inside :ref:`CONFIG_GENERAL_RANGE <struct_CONFIG_GENERAL_RANGE>`.  
   - The defined limits apply globally across all robot motions and tasks.  
   - These values are essential for **safety certification** and **compliance verification**.
