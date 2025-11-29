.. _constants_flange_hw_utility:

2.1.8 Flange & Hardware Utility Macros
----------------------------------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **Name**
     - **Value**
     - **Description**
   * - MIN_FLANGE_AI
     - 2
     - Minimum index of flange analog input channels.
   * - MAX_FLANGE_AI
     - 4
     - Maximum index of flange analog input channels.
   * - IS_NEW_FLANGE_VERSION(f)
     - ((f[3] > '1') && ((f[2] == '0') || (f[2] == '1')))
     - Utility macro used to check whether the flange firmware corresponds to a new version  
       based on the provided version string array ``f``.