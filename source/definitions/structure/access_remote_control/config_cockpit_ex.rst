.. _struct_CONFIG_COCKPIT_EX:

CONFIG_COCKPIT_EX
==================

This is a structure information for cockpit setting and consists of the following fields.

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
     - Enable flag for Cockpit mode |br|
       (0: Disable, 1: Enable)
   * - 1
     - ``_iButton[2]``
     - ``unsigned char[2]``
     - -
     - **Defines the function mapping for Cockpit buttons** |br| 
       0: Direct Teach |br| 
       1: TCP-Z |br| 
       2: TCP-XY  |br|
       3: Orientation Only |br| 
       4: Position Only
   * - 3
     - ``_bRecoveryTeach``
     - ``unsigned char``
     - -
     - Enables or disables Recovery Teach mode |br|  
       (0: Disable, 1: Enable)

Total size: 4 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_COCKPIT_EX
   {
       /* disable: 0, enable: 1 */
       unsigned char  _bEnable;
       /* Direct Teach: 0, TCP-Z: 1, TCP-XY: 2, Orientation Only: 3, Position Only: 4 */
       unsigned char  _iButton[2];
       /* disable: 0, enable: 1 */
       unsigned char  _bRecoveryTeach;
   } CONFIG_COCKPIT_EX, *LPCONFIG_COCKPIT_EX;