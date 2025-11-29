.. _struct_PACKAGE_UNZIP_RESPONSE:

PACKAGE_UNZIP_RESPONSE
======================

This structure represents the **response data** after performing a package unzip operation on the controller.  
It contains the result status and the directory name where the package was extracted.

.. list-table::
   :header-rows: 1
   :widths: 8 25 20 10 37

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iResult``
     - ``unsigned char``
     - 0 ~ 1
     - **Result of the unzip operation** |br| 0: Fail, 1: Success
   * - 1
     - ``_szDirName``
     - ``char[256]``
     - -
     - Directory name or path where the package was extracted. |br|
       The maximum string length is defined by ``MAX_STRING_SIZE``.

Total size: 257 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PACKAGE_UNZIP_RESPONSE
   {
       /* 0: fail, 1:  success */
       unsigned char               _iResult;
       /* file name */
       char                        _szDirName[MAX_STRING_SIZE];

   } PACKAGE_UNZIP_RESPONSE, *LPACKAGE_UNZIP_RESPONSE;
