.. _struct_READ_FLANGE_SERIAL_EX:

READ_FLANGE_SERIAL_EX
=====================

This structure provides information on whether data that can be received  
exists in the **Flange Serial buffer** (extended version).  
Unlike :ref:`READ_FLANGE_SERIAL <struct_READ_FLANGE_SERIAL>`,  
this version supports **multiple ports** (e.g., ``X1``, ``X2``).

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bRecvFlag[2]``
     - ``unsigned char[2]``
     - 0~1
     - Data receive flag for each port |br| 
       (0: Non-receive, 1: Received)


Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_FLANGE_SERIAL_EX
   {
       // check ready to read for multiple ports
       unsigned char _bRecvFlag[2];   // 0: non-receive, 1: received
   } READ_FLANGE_SERIAL_EX, *LPREAD_FLANGE_SERIAL_EX;

.. note::
   - ``_bRecvFlag[0]`` → Port 0 (e.g., **X1**)  
   - ``_bRecvFlag[1]`` → Port 1 (e.g., **X2**)  
   - Used when the robot flange supports **multi-port serial communication**.