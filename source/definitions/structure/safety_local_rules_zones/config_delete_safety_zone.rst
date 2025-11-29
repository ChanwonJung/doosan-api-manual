.. _struct_CONFIG_DELETE_SAFETY_ZONE:

CONFIG_DELETE_SAFETY_ZONE
=========================

This structure defines the **data required to delete a safety zone**  
from the controller’s configuration using its unique identifier.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szIdentifier``
     - ``char[32]``
     - -
     - Unique identifier (UUID string) of the safety zone to delete

Total size: 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DELETE_SAFETY_ZONE
   {
       /* Unique identifier (UUID) of the safety zone to delete */
       char _szIdentifier[32];

   } CONFIG_DELETE_SAFETY_ZONE, *LPCONFIG_DELETE_SAFETY_ZONE;

.. note::
   - ``_szIdentifier`` must match the UUID used when the zone was created  
     (see :ref:`CONFIG_ADD_SAFETY_ZONE <struct_CONFIG_ADD_SAFETY_ZONE>`).  
   - Typically used with APIs such as ``delete_safety_zone()`` to remove a specific zone  
     from the active safety configuration.
