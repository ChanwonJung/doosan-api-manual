.. _struct_PACKAGE_RESTORE:

PACKAGE_RESTORE
================

This structure defines the version information used for performing a **package restore** operation on the controller.

.. list-table::
   :header-rows: 1
   :widths: 8 25 20 10 37

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szVersName``
     - ``char[32]``
     - -
     - Version name string used to identify the restore package. |br|
       The maximum string length is defined by ``MAX_SYMBOL_SIZE``.

Total size: 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PACKAGE_RESTORE
   {
       /* version name */
       char                         _szVersName[MAX_SYMBOL_SIZE];

   } PACKAGE_RESTORE, *LPPACKAGE_RESTORE;
