.. _struct_CONFIG_DIGITAL_WELDING_MODE:

CONFIG_DIGITAL_WELDING_MODE
===========================

This structure defines the **digital welding mode control** used to start or stop  
a digital welding process.  
It is typically issued through a fieldbus or digital I/O command interface.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bMode``
     - ``unsigned char``
     - 0 or 1
     - **Welding mode flag** |br|
       0: Stop welding |br|
       1: Start welding

Total size: 1 byte

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_MODE
   {
       unsigned char _bMode;   // 0: Stop, 1: Start
   } CONFIG_DIGITAL_WELDING_MODE, *LPCONFIG_DIGITAL_WELDING_MODE;

.. note::
   - Provides a simple **start/stop control mechanism** for digital welding.  
   - Used together with :ref:`CONFIG_DIGITAL_WELDING_CONDITION <struct_CONFIG_DIGITAL_WELDING_CONDITION>`  
     to define the active process parameters.