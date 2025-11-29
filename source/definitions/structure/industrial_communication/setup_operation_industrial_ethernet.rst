.. _struct_SETUP_OPERARION_INDUSTRIAL_ETHERNET:

SETUP_OPERARION_INDUSTRIAL_ETHERNET
===================================

This is a structure information to define the **operational setup for industrial Ethernet communication**.  
It specifies the EtherNet/IP operation mode and embeds a full :ref:`CONFIG_INDUSTRIAL_ETHERNET <struct_CONFIG_INDUSTRIAL_ETHERNET>`  
structure for detailed network configuration.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_nEtherNetIP_OpMode``
     - ``unsigned char``
     - 0 / 1
     - **Operation mode** |br|
       0: Monitoring & GPR (476 bytes) |br|
       1: Only GPR (32 bytes)
   * - 1
     - ``tConfig``
     - :ref:`CONFIG_INDUSTRIAL_ETHERNET <struct_CONFIG_INDUSTRIAL_ETHERNET>`
     - -
     - Network configuration structure for EtherNet/IP and PROFINET

Total size: 305 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SETUP_OPERARION_INDUSTRIAL_ETHERNET
   {
       /* 0 : Monitoring&GPR (476 bytes), 1 : Only GPR (32 bytes) */
       unsigned char      _nEtherNetIP_OpMode;
       /* Industrial Ethernet configuration */
       CONFIG_INDUSTRIAL_ETHERNET tConfig;

   } SETUP_OPERARION_INDUSTRIAL_ETHERNET, *LPSETUP_OPERARION_INDUSTRIAL_ETHERNET;
