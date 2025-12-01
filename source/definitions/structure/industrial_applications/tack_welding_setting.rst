.. _struct_TACK_WELDING_SETTING:

TACK_WELDING_SETTING
====================

This structure defines **tack welding configuration**,  
which controls activation and welding signal type (analog or digital).  
It is used to configure short-duration spot welds for joining or positioning components.

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
     - 0 or 1
     - Tack welding activation flag |br|
       (0: Deactivated, 1: Activated)
   * - 1
     - ``_bWeldingType``
     - ``unsigned char``
     - 0 or 1
     - Welding signal type |br|
       (0: Analog, 1: Digital)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _TACK_WELDING_SETTING
   {
       /* Deactivate: 0, Activate: 1 */
       unsigned char _bEnable;

       /* Analog: 0, Digital: 1 */
       unsigned char _bWeldingType;

   } TACK_WELDING_SETTING, *LPTACK_WELDING_SETTING;

.. note::
   - ``_bEnable`` toggles tack welding behavior on/off.  
   - ``_bWeldingType`` defines the communication type for weld signal control.  
   - Commonly used for **spot tack weld operations** in robot welding sequences.