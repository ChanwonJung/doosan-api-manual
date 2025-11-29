.. _union_SAFETY_ZONE_PROPERTY_DATA:

SAFETY_ZONE_PROPERTY_DATA
=========================

This **union** defines a flexible data container for different types of **safety zone properties**.  
It allows storing either **space limit zone** or **local zone** configuration within the same memory region.  
This structure enables consistent access and transmission of zone property data to the robot controller.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tSpaceLimitZone``
     - :ref:`SAFETY_ZONE_PROPERTY_SPACE_LIMIT <struct_SAFETY_ZONE_PROPERTY_SPACE_LIMIT>`
     - -
     - Structure defining space limit properties |br|
       (e.g., body/TCP inspection, dynamic zone control).
   * - 0
     - ``_tLocalZone``
     - :ref:`SAFETY_ZONE_PROPERTY_LOCAL_ZONE <struct_SAFETY_ZONE_PROPERTY_LOCAL_ZONE>`
     - -
     - Structure defining local safety zone properties, |br|
       including joint, TCP, and collision overrides.
   * - 0
     - ``_iBuffer[200]``
     - ``unsigned char[200]``
     - -
     - Raw memory buffer (200 bytes). |br|
       Used for low-level serialization and communication.

Total size: 200 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef union _SAFETY_ZONE_PROPERTY_DATA
   {
       /* Space limit zone properties */
       SAFETY_ZONE_PROPERTY_SPACE_LIMIT _tSpaceLimitZone;

       /* Local zone properties (joint, TCP, speed, etc.) */
       SAFETY_ZONE_PROPERTY_LOCAL_ZONE _tLocalZone;

       /* Raw buffer for communication */
       unsigned char _iBuffer[200];

   } SAFETY_ZONE_PROPERTY_DATA, *LPSAFETY_ZONE_PROPERTY_DATA;