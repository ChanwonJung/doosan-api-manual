.. _struct_PACKAGE_LOCAL_UPDATE:

PACKAGE_LOCAL_UPDATE
====================

This structure defines parameters used for performing a **local package update** on the controller.

.. list-table::
   :header-rows: 1
   :widths: 8 25 20 10 37

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTarget``
     - ``unsigned char[10]``
     - -
     - **Update target flag array** |br|
       0: non-update |br|
       1: update |br|  
       The number of elements is defined by ``UPDATE_TARGET_LAST``.
   * - 10
     - ``_szDirName``
     - ``char[256]``
     - -
     - Directory path for the local update package. |br|  
       The maximum string length is defined by ``MAX_STRING_SIZE``.

Total size: 266 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PACKAGE_LOCAL_UPDATE
   {
       /* 0: non-update, 1: update */
       unsigned char  _iTarget[UPDATE_TARGET_LAST];
       /* update path */
       char           _szDirName[MAX_STRING_SIZE];

   } PACKAGE_LOCAL_UPDATE, *LPPACKAGE_LOCAL_UPDATE;
