.. _struct_SYSTEM_POWER:

SYSTEM_POWER
=============
This structure defines power control commands for the robot or controller system.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTarget``
     - ``unsigned char``
     - -
     - Target device (0: robot inverter, 1: control PC)
   * - 1
     - ``_iPower``
     - ``unsigned char``
     - -
     - Power command (0: shutdown, 1: restart)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_POWER
   {
       /* robot(inverter): 0, control pc: 1 */
       unsigned char _iTarget;
       /* shutdown: 0, restart: 1 */
       unsigned char _iPower;
   } SYSTEM_POWER, *LPSYSTEM_POWER;