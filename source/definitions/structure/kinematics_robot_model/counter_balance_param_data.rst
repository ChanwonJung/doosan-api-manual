.. _struct_COUNTER_BALANCE_PARAM_DATA:

COUNTER_BALANCE_PARAM_DATA
==========================

This structure defines the **counterbalance mechanical parameters** used to model  
the spring-based gravity compensation mechanism in the robot arm.  
Each field describes a key physical property of the counterbalance system.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fK``
     - ``float``
     - -
     - Spring constant (**K**) of the counterbalance
   * - 4
     - ``_fIrod``
     - ``float``
     - -
     - Connecting rod length (Irod)
   * - 8
     - ``_fR``
     - ``float``
     - -
     - Distance between motor center and connecting rod center (**R**)
   * - 12
     - ``_fSi``
     - ``float``
     - -
     - Pre-load length of the spring (**Si**)

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _COUNTER_BALANCE_PARAM_DATA
   {
       /* Spring constant */
       float _fK;

       /* Connecting rod length */
       float _fIrod;

       /* Distance between motor center and connecting rod center */
       float _fR;

       /* Pre-load spring length */
       float _fSi;

   } COUNTER_BALANCE_PARAM_DATA, *LPCOUNTER_BALANCE_PARAM_DATA;