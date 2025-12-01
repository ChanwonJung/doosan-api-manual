.. _struct_MESSAGE_INPUT:

MESSAGE_INPUT
==============

This is a structure for providing user input related information  
is composed of the following fields when a robot controller needs to receive and process user input when executing a DRL program.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**

   * - 0
     - ``_szText``
     - ``char[MAX_STRING_SIZE]``
     - -
     - 256-byte string message information

   * - 256
     - ``_iType``
     - ``unsigned char``
     - 0~3
     - **Expected input type** |br|
       0: int, 1: float, 2: string, 3: bool

Total size: 257 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MESSAGE_INPUT
   {
       char          _szText[MAX_STRING_SIZE];  /* message string */
       unsigned char _iType;                    /* int:0, float:1, string:2, bool:3 */
   } MESSAGE_INPUT, *LPMESSAGE_INPUT;

   typedef MESSAGE_INPUT MONITORING_INPUT;