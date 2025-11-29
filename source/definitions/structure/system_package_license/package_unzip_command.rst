.. _struct_PACKAGE_UNZIP_COMMAND:

PACKAGE_UNZIP_COMMAND
=====================

This structure defines the file information used when performing a **package unzip** or **local SVM update** operation on the controller.  
It contains the name of the compressed update file to be extracted or installed locally.

.. list-table::
   :header-rows: 1
   :widths: 8 25 20 10 37

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szFileName``
     - ``char[256]``
     - -
     - File name of the update package to unzip or install. |br|
       The maximum string length is defined by ``MAX_STRING_SIZE``.

Total size: 256 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PACKAGE_UNZIP_COMMAND
   {
       /* file name */
       char                        _szFileName[MAX_STRING_SIZE];

   } PACKAGE_UNZIP_COMMAND, *LPACKAGE_UNZIP_COMMAND;

   typedef PACKAGE_UNZIP_COMMAND
       SVM_LOCAL_UPDATE, *LPSVM_LOCAL_UPDATE;
