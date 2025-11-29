.. _struct_CONFIG_CONFIGURABLE_IO_EX:

CONFIG_CONFIGURABLE_IO_EX
=========================

This structure extends :ref:`CONFIG_CONFIGURABLE_IO <struct_CONFIG_CONFIGURABLE_IO>`  
by adding trigger-level configurations for each I/O port.  
It allows more fine-grained control over I/O logic states and safety signals.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iIO``
     - ``unsigned char[TYPE_LAST][NUM_DIGITAL * 2]``
     - -
     - Mapping of configurable Safety I/O ports. 
   * - 2
     - ``_bLevel``
     - ``unsigned char[TYPE_LAST][NUM_DIGITAL]``
     - -
     - Trigger level configuration for each I/O port |br| 
       (0: Low active, 1: High active)

Total size: 64 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_CONFIGURABLE_IO_EX
   {
       /* Safety I/O mapping table
          TYPE_LAST : number of I/O categories
          NUM_DIGITAL : number of channels per category
          (×2 for extended configuration area)
       */
       unsigned char _iIO[TYPE_LAST][NUM_DIGITAL * 2];

       /* Optional: Trigger level configuration (future use)
       unsigned char _bLevel[TYPE_LAST][NUM_DIGITAL];
       */

   } CONFIG_CONFIGURABLE_IO_EX, *LPCONFIG_CONFIGURABLE_IO_EX;

.. note::
   - Extends :ref:`CONFIG_CONFIGURABLE_IO <struct_CONFIG_CONFIGURABLE_IO>` to double the mapping space.  
   - Allows customization for both safety-critical and user-defined I/O functions.  
   - Future versions may enable the ``_bLevel`` parameter for polarity configuration (active-low/high).  
   - Typically used with system setup commands in the controller’s I/O configuration module.