.. _struct_ENABLE_SAFE_ZONE:

ENABLE_SAFE_ZONE
================

This is a structure information to enable the safety zone, and consists of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iRegion[3]``
     - ``unsigned char[3]``
     - -
     - Activation status for up to **3 safety zones** |br|
       Each byte corresponds to one zone |br|
       (0: Disabled, 1: Enabled)

Total size: 3 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ENABLE_SAFE_ZONE
   {
       /* region enable flags (0: disable, 1: enable) */
       unsigned char _iRegion[3];
   } ENABLE_SAFE_ZONE, *LPENABLE_SAFE_ZONE;