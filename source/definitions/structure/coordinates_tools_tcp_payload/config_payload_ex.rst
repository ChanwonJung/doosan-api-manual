.. _struct_CONFIG_PAYLOAD_EX:

CONFIG_PAYLOAD_EX
=================
This structure defines the payload configuration including mass, center of gravity, and transition parameters.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fWeight``
     - ``float``
     - -
     - Payload mass (kg)
   * - 4
     - ``_fXYZ``
     - ``float[3]``
     - -
     - Center of gravity position (X, Y, Z)
   * - 16
     - ``_iCogReference``
     - ``unsigned short``
     - -
     - COG reference frame
   * - 18
     - ``_iAddUp``
     - ``unsigned short``
     - -
     - Add-up flag
   * - 20
     - ``_fStartTime``
     - ``float``
     - -
     - Start time (sec)
   * - 24
     - ``_fTransitionTime``
     - ``float``
     - -
     - Transition time (sec)
   * - 28
     - ``_iReserved``
     - ``unsigned char[32]``
     - -
     - Reserved for future use

Total size: 60 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_PAYLOAD_EX
   {
       /* mass(kg) */
       float _fWeight;
       /* center of mass */
       float _fXYZ[3];
       /* COG Reference */
       unsigned short _iCogReference;
       /* Add Up */
       unsigned short _iAddUp;
       /* timing parameters */
       float _fStartTime;
       float _fTransitionTime;
       /* reserved */
       unsigned char _iReserved[32];
   } CONFIG_PAYLOAD_EX, *LPCONFIG_PAYLOAD_EX;