.. _struct_ROBOT_LED_CONFIG:

ROBOT_LED_CONFIG
================

This structure defines the LED behavior configuration for the robot controller.  
It determines the LED color rules and mappings according to different safety states.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szLedRule``
     - ``unsigned char``
     - -
     - LED control rule indicator (used to define LED operation mode)
   * - 1
     - ``_szStateColor[SAFETY_STATE_LAST][2]``
     - ``unsigned char[19][2]``
     - -
     - LED color mapping table for each safety state. |br|
       The first dimension (19) corresponds to :ref:`SAFETY_STATE_LAST <enum_SAFETY_STATE>` |br|
       The second dimension defines two alternating colors per state: |br|
       [][0] → Color 1, [][1] → Color 2
   * - 39
     - ``_szCommandColor``
     - ``unsigned char``
     - -
     - LED color setting used for command or override state

Total size: 40 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_LED_CONFIG
   {
       unsigned char _szLedRule;                                  /* LED control rule */
       unsigned char _szStateColor[SAFETY_STATE_LAST][2];         /* [state][0]: color1, [state][1]: color2 */
       unsigned char _szCommandColor;                             /* LED color for command state */
   } ROBOT_LED_CONFIG, *LPROBOT_LED_CONFIG;