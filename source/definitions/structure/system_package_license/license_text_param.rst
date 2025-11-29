.. _struct_LICENSE_TEXT_PARAM:

LICENSE_TEXT_PARAM
==================

This structure defines the **license key information** used by the robot controller.  
It specifies whether the license key is stored inside the controller and contains the license key string itself.

.. list-table::
   :widths: 10 25 15 15 35
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bLicenseInController``
     - ``unsigned char``
     - 0 or 1
     - Indicates whether the license key is stored in the controller |br|  
       0: external key, 1: internal key
   * - 1
     - ``_szLicenseKey``
     - ``unsigned char[48]``
     - License key string data
     - ASCII-encoded string of up to **48 bytes**,  
       used to verify the license authorization.

Total size: 49 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LICENSE_TEXT_PARAM
   {
       // position of license key
       unsigned char _bLicenseInController;
       // license key string data
       unsigned char _szLicenseKey[48];
   } LICENSE_TEXT_PARAM, *LPLICENSE_TEXT_PARAM;
