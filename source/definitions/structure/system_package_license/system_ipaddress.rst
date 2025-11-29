.. _struct_SYSTEM_IPADDRESS:

SYSTEM_IPADDRESS
================
This structure defines network configuration parameters including IP, subnet mask, gateway, and DNS information.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iUsage``
     - ``unsigned char``
     - -
     - IP usage (internal/external or enable/disable depending on compilation flag)
   * - 1
     - ``_iIpType``
     - ``unsigned char``
     - -
     - IP type (0: dynamic, 1: static)
   * - 2
     - ``_szHotsIp``
     - ``char[16]``
     - -
     - Host IP address
   * - 18
     - ``_szSubnet``
     - ``char[16]``
     - -
     - Subnet mask address
   * - 34
     - ``_szGateway``
     - ``char[16]``
     - -
     - Default gateway address
   * - 50
     - ``_szDNS``
     - ``char[2][16]``
     - -
     - Primary and secondary DNS addresses


Total size: 82 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_IPADDRESS
   {
   #ifndef USE_ONE_IP
       /* internal use: 0, external link: 1 */
   #else
       /* Disable: 0, Enable: 1 */
   #endif
       unsigned char _iUsage;
       /* dynamic ip: 0, static ip: 1 */
       unsigned char _iIpType;
       /* ip address */
       char _szHotsIp[16];
       /* subnet mask address */
       char _szSubnet[16];
       /* default gateway address */
       char _szGateway[16];
       /* primary/secondary dns address */
       char _szDNS[2][16];
   } SYSTEM_IPADDRESS, *LPSYSTEM_IPADDRESS;