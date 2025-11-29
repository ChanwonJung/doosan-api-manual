.. _struct_MACHINE_TENDING_FOCAS_DISCONNECT:

MACHINE_TENDING_FOCAS_DISCONNECT
================================

This structure defines the **disconnection command and response**  
for FOCAS communication. It includes the error code and connection handle  
used to close the active FOCAS session.

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
     - Disconnection error code (0 indicates success)
   * - 2
     - ``_hHandle``
     - ``unsigned short``
     - -
     - Connection handle identifier used to close FOCAS communication

Total size: 4 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_FOCAS_DISCONNECT
   {
       short          _ErrorCode;   /* 0: success, non-zero: error */
       unsigned short _hHandle;     /* FOCAS connection handle */
   } MACHINE_TENDING_FOCAS_DISCONNECT, *LPMACHINE_TENDING_FOCAS_DISCONNECT;