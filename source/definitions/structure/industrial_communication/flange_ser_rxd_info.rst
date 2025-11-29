.. _struct_FLANGE_SER_RXD_INFO:

FLANGE_SER_RXD_INFO
===================

This structure stores the **received serial data information** from the robot flange port.  
It contains both the size of the received data and the corresponding raw byte buffer.

.. list-table::
   :widths: 10 28 20 8 34
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
     - Total size of the received serial data (maximum 256 bytes)
   * - 2
     - ``_cRxd``
     - ``unsigned char[256]``
     - -
     - Raw serial data buffer

Total size: 258 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _FLANGE_SER_RXD_INFO
   {
       /* Size of received serial data (max 256 bytes) */
       short          _iSize;
       /* Raw serial data buffer */
       unsigned char  _cRxd[256];

   } FLANGE_SER_RXD_INFO, *LPFLANGE_SER_RXD_INFO;
