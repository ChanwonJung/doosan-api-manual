.. _struct_READ_FLANGE_SERIAL:

READ_FLANGE_SERIAL
==================

This is a structure information to check whether data that can be received exists in the buffer when using Flange Serial is composed of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bRecvFlag``
     - ``unsigned char``
     - 0~1
     - **Data flag** |br|
       (0: Non-receive, 1: Received)

Total size: 1 byte

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_FLANGE_SERIAL
   {
       // check ready to read
       unsigned char _bRecvFlag;   // 0: non-receive, 1: received
   } READ_FLANGE_SERIAL, *LPREAD_FLANGE_SERIAL;