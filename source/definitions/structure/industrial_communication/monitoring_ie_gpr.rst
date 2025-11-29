.. _struct_MONITORING_IE_GPR:

MONITORING_IE_GPR
=================

This is a structure information to store **Industrial Ethernet (IE) General Purpose Register (GPR) monitoring data**.  
It contains a raw byte array representing the total GPR packet data received from the industrial Ethernet interface.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_nGpr``
     - ``unsigned char[464]``
     - -
     - GPR monitoring packet data |br|
       (Defined by **IE_MONITORING_PACKET_TOTAL_DATA**)

Total size: 464 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_IE_GPR
   {
       /* IE_MONITORING_PACKET_TOTAL_DATA */
       unsigned char  _nGpr[464];

   } MONITORING_IE_GPR;
