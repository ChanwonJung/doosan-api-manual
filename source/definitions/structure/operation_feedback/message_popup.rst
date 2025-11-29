.. _struct_MESSAGE_POPUP:

MESSAGE_POPUP
==============

This is a structure for providing typographic message related information  
is composed of the following fields when a program created through a typographic application is executed in a robot controller.

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
     - 256-byte message string

   * - 256
     - ``_iLevel``
     - ``unsigned char``
     - 0~2
     - Message level |br|
       0: Message, 1: Warning, 2: Alarm

   * - 257
     - ``_iBtnType``
     - ``unsigned char``
     - 0~1
     - Button type |br|
       0: Resume & Stop, 1: OK

Total size: 258 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MESSAGE_POPUP
   {
       char          _szText[MAX_STRING_SIZE];  /* message string */
       unsigned char _iLevel;                   /* Message: 0, Warning: 1, Alarm: 2 */
       unsigned char _iBtnType;                 /* Resume&Stop: 0, OK: 1 */
   } MESSAGE_POPUP, *LPMESSAGE_POPUP;
   
   typedef MESSAGE_POPUP MONITORING_POPUP;