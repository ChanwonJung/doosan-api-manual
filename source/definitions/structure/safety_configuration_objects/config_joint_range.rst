.. _struct_CONFIG_JOINT_RANGE:

CONFIG_JOINT_RANGE
==================

This structure defines **joint motion limits** in two operation modes:  
**Normal Mode** and **Reduced Mode**.  
This is a structure information to set limits in joint space and consists of the following fields.

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
     - :ref:`struct_JOINT_RANGE`
     - -
     - Joint range settings for **Normal Mode**
   * - 72
     - ``_Reduced``
     - :ref:`struct_JOINT_RANGE`
     - -
     - Joint range settings for **Reduced Mode**

Total size: 144 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_JOINT_RANGE
   {
       /* normal mode */
       JOINT_RANGE _Normal;
       /* reduced mode */
       JOINT_RANGE _Reduced;
   } CONFIG_JOINT_RANGE, *LPCONFIG_JOINT_RANGE;