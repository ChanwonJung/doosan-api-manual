.. _struct_MONITORING_CTRLIO:

MONITORING_CTRLIO
=================

This structure provides the current I/O state information installed in the **control box** of the robot controller,  
aggregating both input and output sections. It is used to monitor the robot controller’s I/O interfaces.

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tInput``
     - :ref:`READ_CTRLIO_INPUT <struct_READ_CTRLIO_INPUT>`
     - -
     - Controller I/O **inputs**
   * - 39
     - ``_tOutput``
     - :ref:`READ_CTRLIO_OUTPUT <struct_READ_CTRLIO_OUTPUT>`
     - -
     - Controller I/O **outputs**

Total size: 63 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_CTRLIO
   {
       READ_CTRLIO_INPUT  _tInput;   /* input data  */
       READ_CTRLIO_OUTPUT _tOutput;  /* output data */
   } MONITORING_CTRLIO, *LPMONITORING_CTRLIO;

**I/O Information mapping**

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - **I/O Information**
     - **Description**
   * - (#1) at BYTE 0
     - Information on 16 digital inputs attached to the control box
   * - (#2) at BYTE 16
     - Information on two analog inputs attached to the control box
   * - (#3) at BYTE 24
     - Information on the state of three switches attached to the control box and T/P such as the direct teaching button
   * - (#4) at BYTE 27
     - Information on two safety-related inputs attached to the control box
   * - (#5) at BYTE 29
     - Information on two encoder-related inputs attached to the control box
   * - (#6) at BYTE 31
     - Information on two encoder-related raw data attached to the control box
   * - (#7) at BYTE 39
     - Information on 16 digital outputs attached to the control box
   * - (#8) at BYTE 55
     - Information on two analog outputs attached to the control box
