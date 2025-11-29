.. _struct_MEASURE_TCP_RESPONSE:

MEASURE_TCP_RESPONSE
====================

This is a structure for providing the **measured TCP (Tool Center Point)** information  
obtained from the robot controller’s auto-measurement process, and consists of the following fields.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tTCP``
     - :ref:`CONFIG_TCP <struct_CONFIG_TCP>`
     - -
     - Measured TCP position and orientation (6D pose)
   * - 24
     - ``_fError``
     - ``float``
     - -
     - Measurement error value (deviation in mm or degrees)

Total size: 28 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_TCP_RESPONSE
   {
       CONFIG_TCP _tTCP;   /* measured TCP pose */
       float       _fError; /* measurement error */
   } MEASURE_TCP_RESPONSE, *LPMEASURE_TCP_RESPONSE;