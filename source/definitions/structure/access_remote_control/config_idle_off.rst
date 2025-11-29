.. _struct_CONFIG_IDLE_OFF:

CONFIG_IDLE_OFF
================
This is a structure information for setting auto Servo Off function, and consists of the following fields.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bFuncEnable``
     - ``unsigned char``
     - -
     - Enable flag for Auto Servo-Off |br|
       (0: Disable, 1: Enable)
   * - 1
     - ``_fElapseTime``
     - ``float``
     - -
     - Elapsed idle time (in seconds)  

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_IDLE_OFF
   {
       /* function enable */
       unsigned char  _bFuncEnable;
       /* elapse time (seconds) */
       float          _fElapseTime;

   } CONFIG_IDLE_OFF, *LPCONFIG_IDLE_OFF;