.. _setup_monitoring_version:

setup_monitoring_version
------------------------------------------
This is a function for setting version information of monitoring information transmitted from the robot controller.

This function is only available in M2.5 version or higher.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 991)

.. code-block:: cpp

    bool setup_monitoring_version(int iVersion) { 
        return _setup_monitoring_version(_rbtCtrl, iVersion); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iVersion
     - int
     - -
     - Version information |br|
       (0: version 0, 1: version 1)

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Failed
   * - 1
     - int
     - Success

**Example**

.. code-block:: cpp

   drfl.setup_monitoring_version(1);   // Set monitoring data version information to 1

Setting the monitoring version to **1** enables use of the **extended monitoring data functions**,  
such as `set_on_monitoring_data_ex()` and `set_on_monitoring_ctrl_io_ex()`,  
which provide higher-resolution and additional state information from the controller.
