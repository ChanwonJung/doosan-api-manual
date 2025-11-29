.. _struct_SYSTEM_DISKSIZE:

SYSTEM_DISKSIZE
================
This structure provides information about the controller's storage capacity and usage.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTotalDiskSize``
     - ``unsigned int``
     - -
     - Total disk size (in MB)
   * - 4
     - ``_iUsedDiskSize``
     - ``unsigned int``
     - -
     - Used disk size (in MB)

Total size: 8 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_DISKSIZE
   {
       /* total disk size */
       unsigned int _iTotalDiskSize;
       /* used disk size */
       unsigned int _iUsedDiskSize;
   } SYSTEM_DISKSIZE, *LPSYSTEM_DISKSIZE;