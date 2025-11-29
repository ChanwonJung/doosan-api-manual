.. _struct_CONFIG_INDUSTRIAL_ETHERNET:

CONFIG_INDUSTRIAL_ETHERNET
==========================

This is a structure information to store configuration parameters for **industrial Ethernet communication**.  
It contains IP and network settings for **EtherNet/IP** and **PROFINET** interfaces used in robot-controller communication.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szEtherNetIpIpAddress``
     - ``char[16]``
     - -
     - EtherNet/IP device IP address
   * - 16
     - ``_szProfinetIpAddress``
     - ``char[16]``
     - -
     - PROFINET device IP address
   * - 32
     - ``_szProfinetDeviceName``
     - ``char[240]``
     - -
     - PROFINET device name (UTF-8 string)
   * - 272
     - ``_szProfinetSubnetMask``
     - ``char[16]``
     - -
     - PROFINET subnet mask
   * - 288
     - ``_szProfinetGateway``
     - ``char[16]``
     - -
     - PROFINET gateway address

Total size: 304 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_INDUSTRIAL_ETHERNET
   {
       char  _szEtherNetIpIpAddress[16];
       char  _szProfinetIpAddress[16];
       char  _szProfinetDeviceName[240];
       char  _szProfinetSubnetMask[16];
       char  _szProfinetGateway[16];

   } CONFIG_INDUSTRIAL_ETHERNET, *LPCONFIG_INDUSTRIAL_ETHERNET;
