.. _struct_MACHINE_TENDING_FOCAS_CNC_PARAM:

MACHINE_TENDING_FOCAS_CNC_PARAM
===============================

FOCAS **CNC parameter access descriptor**: identifies the parameter and access shape.

.. list-table::
   :widths: 12 30 18 10 30
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_hHandle``
     - ``unsigned short``
     - -
     - Active FOCAS session handle
   * - 2
     - ``_iParamNumber``
     - ``short``
     - -
     - CNC parameter number
   * - 4
     - ``_iAxisNumber``
     - ``short``
     - -
     - Axis index (0 for common/global)
   * - 6
     - ``_iDataLength``
     - ``short``
     - bytes
     - Parameter data length to read/write

Total size: 8 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_FOCAS_CNC_PARAM
   {
       unsigned short _hHandle;      /* FOCAS session handle */
       short          _iParamNumber; /* parameter number */
       short          _iAxisNumber;  /* axis index (0: global) */
       short          _iDataLength;  /* length in bytes */
   } MACHINE_TENDING_FOCAS_CNC_PARAM, *LPMACHINE_TENDING_FOCAS_CNC_PARAM;