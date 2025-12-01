.. _flange_serial_read:

flange_serial_read
------------------------------------------
This is a function for receiving serial data from the **flange serial port** in the robot controller. |br|
The port parameter is **only available in the new flange version (v2).**

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 879)

.. code-block:: cpp

    LPFLANGE_SER_RXD_INFO_EX flange_serial_read(float fTimeout = -1, int nPort = 1)
    {
        return _flange_serial_read(_rbtCtrl, fTimeout, nPort);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTimeout
     - float
     - -1
     - Timeout value in seconds. |br|
       A value of **-1** means the function will **wait indefinitely** for incoming data.
   * - nPort
     - int
     - 1
     - **Port number for flange serial interface** |br|
       1: X1 |br|  
       2: X2 (supported only on M/H models)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`FLANGE_SER_RXD_INFO_EX <struct_flange_ser_rxd_info_ex>`
     - Refer to the Definition of Structure

**Example**

.. code-block:: cpp

    Drfl.flange_serial_open(115200);
    Drfl.flange_serial_write(8, "test123");

    LPFLANGE_SER_RXD_INFO_EX temp = Drfl.flange_serial_read(4.5);
    cout << "Serial read : " << temp->_pRxd << endl;
    cout << "Serial cnt  : " << (int)temp->_iSize << endl;

    Drfl.flange_serial_close(0);

This example opens the flange serial port, sends the string `"test123"`,  
waits up to **4.5 seconds** for a response, and prints the received data  
and byte count using the returned structure.
