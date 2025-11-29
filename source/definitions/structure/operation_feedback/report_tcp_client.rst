.. _struct_REPORT_TCP_CLIENT:

REPORT_TCP_CLIENT
=================

This structure defines information about a TCP client connected to the robot controller.  
It is used to monitor or manage multiple TCP client connections,  
including their unique identifiers and total connection count.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iId``
     - ``unsigned char``
     - 0~255
     - Unique identifier assigned to the TCP client
   * - 1
     - ``_iCount``
     - ``unsigned char``
     - 0~255
     - Total number of active TCP clients connected to the controller

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _REPORT_TCP_CLIENT
   {    
       unsigned char _iId;      /* unique client ID */
       unsigned char _iCount;   /* number of connected clients */
   } REPORT_TCP_CLIENT, *LPREPORT_TCP_CLIENT;
