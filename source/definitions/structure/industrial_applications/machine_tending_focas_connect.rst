.. _struct_MACHINE_TENDING_FOCAS_CONNECT:

MACHINE_TENDING_FOCAS_CONNECT
=============================

This structure defines the **connection configuration and response**  
for FOCAS communication in Machine Tending applications.  
It includes IP address, port number, connection handle, and timeout parameters.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_ErrorCode``
     - ``short``
     - -
     - Connection error code (0 indicates success)
   * - 2
     - ``_szIpAddr``
     - ``char[16]``
     - IPv4 address string
     - Target CNC or FOCAS server IP (null-terminated)
   * - 18
     - ``_iPort``
     - ``unsigned short``
     - 0–65535
     - Network port number used for connection
   * - 20
     - ``_hHandle``
     - ``unsigned short``
     - -
     - Connection handle identifier assigned by the FOCAS API
   * - 22
     - ``_fTimeOut``
     - ``float``
     - seconds
     - Timeout value for connection or communication

Total size: 26 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_FOCAS_CONNECT
   {
       short          _ErrorCode;           /* 0: success, non-zero: error */
       char           _szIpAddr[16];        /* target IP address */
       unsigned short _iPort;               /* TCP port */
       unsigned short _hHandle;             /* connection handle */
       float          _fTimeOut;            /* timeout (sec) */
   } MACHINE_TENDING_FOCAS_CONNECT, *LPMACHINE_TENDING_FOCAS_CONNECT;