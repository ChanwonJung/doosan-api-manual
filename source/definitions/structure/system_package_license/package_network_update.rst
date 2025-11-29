.. _struct_PACKAGE_NETWORK_UPDATE:

PACKAGE_NETWORK_UPDATE
======================

This structure defines parameters used for performing a **network-based package update** on the controller.  
It specifies the update targets, network type, server information, and file name for remote update operations.

.. list-table::
   :header-rows: 1
   :widths: 8 25 20 10 37

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTarget``
     - ``unsigned char[UPDATE_TARGET_LAST]``
     - -
     - **Update target flag array** |br|
       0: non-update, 1: update |br|  
       The number of elements is defined by ``UPDATE_TARGET_LAST``.
   * - 10
     - ``_iNetType``
     - ``unsigned char``
     - 0 ~ 1
     - **Network type selection** |br| 
       0: TFTP, 1: SAMBA
   * - 11
     - ``_szIpAddress``
     - ``char[16]``
     - -
     - TFTP or SAMBA server IP address
   * - 27
     - ``_szFileName``
     - ``char[MAX_STRING_SIZE]``
     - -
     - File name of the package to be updated

Total size: 283 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PACKAGE_NETWORK_UPDATE
   {
       /* 0: non-update, 1:  update */
       unsigned char                _iTarget[UPDATE_TARGET_LAST];
       /* ttfp: 0, samba: 1 */
       unsigned char                _iNetType;
       /* tftp server Ip address */
       char                         _szIpAddress[16];
       /* file name */
       char                         _szFileName[MAX_STRING_SIZE];

   } PACKAGE_NETWORK_UPDATE, *LPPACKAGE_NETWORK_UPDATE;
