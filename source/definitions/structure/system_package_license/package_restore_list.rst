.. _struct_PACKAGE_RESTORE_LIST:

PACKAGE_RESTORE_LIST
====================

This structure provides detailed information about the **available restore package versions** on the controller,  
including version names, installation dates, current version, and issue codes for recovery validation.

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
     - ``char[5][32]``
     - -
     - List of up to 5 stored version names. |br|
       Each version string has a maximum length of ``MAX_SYMBOL_SIZE`` (=32).
   * - 160
     - ``_szversDate``
     - ``char[5][32]``
     - -
     - Installation dates corresponding to each version name. |br|
       Each date string uses the same ``MAX_SYMBOL_SIZE``.
   * - 320
     - ``_szCurrVers``
     - ``char[32]``
     - -
     - Current active version name on the controller.
   * - 352
     - ``_iIssueCode``
     - ``unsigned char[5]``
     - 0 ~ 255
     - Recovery issue code for each version. |br|
       0: OK, 1~: Error code

Total size: 357 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PACKAGE_RESTORE_LIST
   {
       /* version name */
       char                        _szVersName[5][MAX_SYMBOL_SIZE];
       /* install date */
       char                        _szversDate[5][MAX_SYMBOL_SIZE];
       /* current version */
       char                        _szCurrVers[MAX_SYMBOL_SIZE];
       /* recovery issue : ok(0), error(1~) */
       unsigned char               _iIssueCode[5];

   } PACKAGE_RESTORE_LIST, *LPPACKAGE_RESTORE_LIST;
