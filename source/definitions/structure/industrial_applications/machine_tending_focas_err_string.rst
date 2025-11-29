.. _struct_MACHINE_TENDING_FOCAS_ERR_STRING:

MACHINE_TENDING_FOCAS_ERR_STRING
================================

This structure defines the **error information** returned from the FOCAS interface  
used in Machine Tending operations. It includes the communication handle,  
error code, and descriptive error message string.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_hHandle``
     - ``unsigned short``
     - -
     - FOCAS communication handle identifier
   * - 2
     - ``_ErrorCode``
     - ``short``
     - -
     - Error code value returned by the FOCAS interface
   * - 4
     - ``_szErrorString``
     - ``char[256]``
     - -
     - Null-terminated string describing the error details

Total size: 260 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_FOCAS_ERR_STRING
   {
       unsigned short _hHandle;              /* FOCAS handle identifier */
       short          _ErrorCode;            /* Error code value */
       char           _szErrorString[256];   /* Error description string */
   } MACHINE_TENDING_FOCAS_ERR_STRING, *LPMACHINE_TENDING_FOCAS_ERR_STRING;