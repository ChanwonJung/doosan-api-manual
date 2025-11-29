.. _struct_GPIO_PORT:

GPIO_PORT
==========

This structure defines a single **GPIO (General-Purpose Input/Output) port** entry,  
representing both the port’s index and its corresponding data value.  
It is primarily used as an element within burst operations such as  
:ref:`WRITE_SERIAL_BURST <struct_WRITE_SERIAL_BURST>` or  
:ref:`GPIO_SETOUTPUT_BURST <struct_WRITE_SERIAL_BURST>`.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iIndex``
     - ``unsigned char``
     - 0 ~ N
     - Index number of the GPIO port. |br|
       Specifies which port this entry refers to.
   * - 1
     - ``_fValue``
     - ``float``
     - 0.0 or 1.0
     - Current port value or output state. |br| 
       0.0: Low (OFF) |br|
       1.0: High (ON)

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _GPIO_PORT
   {
       /* Port index (0~N) */
       unsigned char _iIndex;

       /* Port value (0.0: low, 1.0: high) */
       float _fValue;

   } GPIO_PORT, *LPGPIO_PORT;

.. note::
   - This structure acts as the **basic data unit** for GPIO operations in burst or single mode.  
   - ``_iIndex`` determines which GPIO channel is targeted,  
     and ``_fValue`` specifies the desired output level.  
   - Used in both **digital output control** and **burst transmission structures**.
