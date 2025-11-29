.. _struct_CONFIG_ENCODER_POLARITY:

CONFIG_ENCODER_POLARITY
=======================
This structure defines the **encoder polarity configuration** for each encoder channel.  
It allows the user to specify the channel index and set polarity inversion flags for the encoder signals.  
This configuration is typically used in encoder calibration or motion direction correction processes.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iChannel``
     - ``unsigned char``
     - 0~1
     - Encoder channel index
   * - 1
     - ``_iPolarity``
     - ``unsigned char[ENCORDER_POLARITY_LAST]``
     - 0 or 1
     - Encoder polarity configuration |br|
       (0: Normal, 1: Inverted)

Total size: 7 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_ENCODER_POLARITY
   {
       /* Encoder channel: 0~1 */
       unsigned char _iChannel;

       /* Encoder polarity: 0(normal), 1(inverted) */
       unsigned char _iPolarity[ENCORDER_POLARITY_LAST];

   } CONFIG_ENCODER_POLARITY, *LPCONFIG_ENCODER_POLARITY;
