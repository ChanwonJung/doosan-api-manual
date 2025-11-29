.. _struct_CONFIG_GENERAL_RANGE:

CONFIG_GENERAL_RANGE
====================

This is a structure information to set limits in force and consists of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_Normal``
     - :ref:`struct_GENERAL_RANGE`
     - -
     - Normal mode range configuration
   * - 4
     - ``_Reduced``
     - :ref:`struct_GENERAL_RANGE`
     - -
     - Reduced mode range configuration

Total size: 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_GENERAL_RANGE
   {
       /* normal mode */
       GENERAL_RANGE _Normal;
       /* reduced mode */
       GENERAL_RANGE _Reduced;
   } CONFIG_GENERAL_RANGE, *LPCONFIG_GENERAL_RANGE;
