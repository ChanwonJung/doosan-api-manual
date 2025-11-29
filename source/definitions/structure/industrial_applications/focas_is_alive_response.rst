.. _struct_FOCAS_IS_ALIVE_RESPONSE:

FOCAS_IS_ALIVE_RESPONSE
=======================

This structure reports the **communication status** between the robot controller and the CNC via FOCAS.  
It is used as a lightweight heartbeat or connectivity check response.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``handle``
     - ``unsigned short``
     - -
     - FOCAS connection handle ID
   * - 2
     - ``response``
     - ``unsigned short``
     - 0 or 1
     - 0: Offline |br| 1: Online (CNC connection alive)

Total size: 4 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _FOCAS_IS_ALIVE_RESPONSE
   {
       unsigned short handle;    /* FOCAS handle ID */
       unsigned short response;  /* 0: offline, 1: online */
   } FOCAS_IS_ALIVE_RESPONSE, *LPFOCAS_IS_ALIVE_RESPONSE;