.. _struct_FLANGE_SER_RXD_INFO_EX:

FLANGE_SER_RXD_INFO_EX
======================

This structure is used to receive the transmitted serial data value  
when using **Flange Serial (extended version)**.  
Compared to :ref:`FLANGE_SER_RXD_INFO <struct_FLANGE_SER_RXD_INFO>`,  
this version additionally includes a **target port number** field.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iSize``
     - ``short``
     - -
     - RX Data length
   * - 2
     - ``_cRxd``
     - ``unsigned char[256]``
     - -
     - 256bytes data value
   * - 258
     - ``_portNum``
     - ``unsigned char``
     - 0~N
     - Target port number (e.g., 0: X1, 1: X2)

Total size: 259 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _FLANGE_SER_RXD_INFO_EX
   {
       /* size of serial data */
       short          _iSize;     // max 256 bytes
       /* raw serial data */
       unsigned char  _cRxd[256];
       /* target port # */
       unsigned char  _portNum;
   } FLANGE_SER_RXD_INFO_EX, *LPFLANGE_SER_RXD_INFO_EX;