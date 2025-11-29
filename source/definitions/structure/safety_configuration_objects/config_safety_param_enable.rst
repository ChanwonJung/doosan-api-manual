.. _struct_CONFIG_SAFETY_PARAM_ENABLE:

CONFIG_SAFETY_PARAM_ENABLE
==========================

This structure defines the **enable flag and reference checksum** information  
used for validating or updating safety parameter configurations in the controller.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_wPreviousCmdid``
     - ``unsigned short``
     - -
     - Previous command ID related to the last safety parameter change.
   * - 2
     - ``_iRefCrc32``
     - ``unsigned int``
     - -
     - CRC32 reference checksum used for integrity validation.

Total size: 6 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_SAFETY_PARAM_ENABLE 
   {
       unsigned short _wPreviousCmdid;  /* Previous command ID */
       unsigned int   _iRefCrc32;       /* CRC32 reference checksum */
   } CONFIG_SAFETY_PARAM_ENABLE, *LPCONFIG_SAFETY_PARAM_ENABLE;
