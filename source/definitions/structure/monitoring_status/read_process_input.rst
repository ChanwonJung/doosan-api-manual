.. _struct_READ_PROCESS_INPUT:

READ_PROCESS_INPUT
==================

This structure provides **process button input** data for **small models**,  
mapping up to four digital On/Off inputs in the reserved space of  
:ref:`struct_MONITORING_CTRLIO_EX`.

.. list-table::
   :widths: 10 32 18 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualDI``
     - ``unsigned char[4]``
     - 0x00~0x01
     - Digital **input states** (4 channels)

Total size: 4 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_PROCESS_INPUT
   {
       unsigned char _iActualDI[4];   /* Digital Input data (4 channels) */
   } READ_PROCESS_INPUT, *LPREAD_PROCESS_INPUT;

.. note::
   - Located within the **Reserved Space** (24 B) of :ref:`struct_MONITORING_CTRLIO_EX` and :ref:`struct_MONITORING_CTRLIO_EX2`.
   - Provides **process button On/Off** information for compact or educational robot models.
   - Each bit corresponds to a digital input channel (0–3).
