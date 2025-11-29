.. _struct_SAFETY_TOOL_ORIENTATION_LIMIT:

SAFETY_TOOL_ORIENTATION_LIMIT
=============================

This is a structure information to set the limitation of tool orientation, and consists of the following fields. 
It restricts the allowable direction and angular deviation of the tool to ensure safe operation.  
Typically used in :ref:`config_tool_orientation_limit_zone <struct_CONFIG_TOOL_ORIENTATION_LIMIT_ZONE>` to constrain tool movement within a defined direction range.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tTargetDir``
     - :ref:`POINT_3D <struct_POINT_3D>`
     - -
     - Reference direction vector for tool orientation (X, Y, Z)
   * - 12
     - ``_fTargetAng``
     - ``float``
     - -
     - Target Angle

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_TOOL_ORIENTATION_LIMIT
   {
       /* Direction vector of the tool (unit vector form) */
       POINT_3D _tTargetDir;

       /* Allowable angle deviation (degrees) */
       float _fTargetAng;
   } SAFETY_TOOL_ORIENTATION_LIMIT, *LPSAFETY_TOOL_ORIENTATION_LIMIT;

.. note::
   - This structure is used to limit the **orientation of the tool** during motion or within safety zones.  
   - Commonly applied in collaborative robot setups to restrict tool orientation in sensitive workspaces.  
   - For full zone configuration, see :ref:`config_tool_orientation_limit_zone <struct_CONFIG_TOOL_ORIENTATION_LIMIT_ZONE>`.
