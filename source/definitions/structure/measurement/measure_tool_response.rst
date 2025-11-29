.. _struct_MEASURE_TOOL_RESPONSE:

MEASURE_TOOL_RESPONSE
=====================

This is a structure for providing measurement results of the tool  
(typically used in tool parameter auto-measurement functions),  
and consists of the following fields.


.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fWeight``
     - ``float``
     - -
     - Tool mass (kg)
   * - 4
     - ``_fXYZ``
     - ``float[3]``
     - -
     - Tool center of gravity position (X, Y, Z) (m)

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_TOOL_RESPONSE
   {
       float _fWeight;    /* mass (kg) */
       float _fXYZ[3];    /* center of mass (x, y, z) */
   } MEASURE_TOOL_RESPONSE, *LPMEASURE_TOOL_RESPONSE;