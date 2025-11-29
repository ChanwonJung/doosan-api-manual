.. _open_connection:

open_connection
------------------------------------------
This is a function for connecting with the robot controller using TCP/IP communication. As TCP/IP is internally fixed, there is no need to designate it separately. When two or more robot controllers are used, the IP address should be changed in the T/P application.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 572)

.. code-block:: cpp

    bool open_connection(string strIpAddr = "192.168.137.100", unsigned int usPort= 12345) { return _open_connection(_rbtCtrl, strIpAddr.c_str(), usPort); };


**Parameter** 

.. list-table::
   :widths: 20 15 25 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strIpAddr
     - string
     - "192.168.137.100"
     - Controller IP address to connect.

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to establish a TCP/IP connection.
   * - 1
     - int
     - Success — successfully connected to the controller.

**Example**

.. code-block:: cpp

   CDRFLEx drfl;

   bool bConnected = drfl.open_connection("192.168.137.100");
   if (bConnected) {
       SYSTEM_VERSION tSysVerion = { '\0', };
       DrFl.get_system_version(&tSysVerion);
       cout << "System version: " << tSysVerion._szController << endl;
   }

This example connects the external PC to the robot controller using its IP address.  
When the connection is successful, it retrieves and prints the controller’s system version information.