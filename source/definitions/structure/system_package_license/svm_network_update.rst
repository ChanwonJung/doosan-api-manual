.. _struct_SVM_NETWORK_UPDATE:

SVM_NETWORK_UPDATE
==================

This structure defines parameters used for performing a **network update of the Smart Vision Module (SVM)**.  
It includes network type selection, server IP address, and file name for the update package.

.. list-table::
   :header-rows: 1
   :widths: 8 25 20 10 37

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iNetType``
     - ``unsigned char``
     - 0 ~ 1
     - Network type selection |br| 0: TFTP, 1: SAMBA
   * - 1
     - ``_szIpAddress``
     - ``char[16]``
     - -
     - IP address of the TFTP or SAMBA server.
   * - 17
     - ``_szFileName``
     - ``char[256]``
     - -
     - File name of the SVM update package. |br|
       The maximum string length is defined by ``MAX_STRING_SIZE``.

Total size: 273 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SVM_NETWORK_UPDATE
   {
       /* ttfp: 0, samba: 1 */
       unsigned char               _iNetType;
       /* tftp server Ip address */
       char                        _szIpAddress[16];
       /* file name */
       char                        _szFileName[MAX_STRING_SIZE];

   } SVM_NETWORK_UPDATE, *LPSVM_NETWORK_UPDATE;
