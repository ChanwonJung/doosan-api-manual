.. _struct_CONFIG_NUDGE:

CONFIG_NUDGE
=============

This is a structure information to set the Nudge area, and consists of the following fields.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bEnable``
     - ``unsigned char``
     - -
     - Enable flag |br| 
       (0: Disable, 1: Enable)
   * - 1
     - ``_fInputForce``
     - ``float``
     - -
     - Input flag
   * - 5
     - ``_fDelayTime``
     - ``float``
     - -
     - Delay time

Total size : 9 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_NUDGE
   {
       /* enable/disable flag */
       unsigned char  _bEnable;
       /* input force threshold */
       float          _fInputForce;
       /* delay time before activation */
       float          _fDelayTime;

   } CONFIG_NUDGE, *LPCONFIG_NUDGE;