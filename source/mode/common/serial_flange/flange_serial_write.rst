.. _flange_serial_write:

flange_serial_write
------------------------------------------
This is a function for sending serial data through the **flange serial port** in the robot controller. |br|
The port parameter is **only available in the new flange version (v2).**

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 878)

.. code-block:: cpp

    bool flange_serial_write(int nSize, char* pSendData, int nPort = 1)
    {
        return _flange_serial_write(_rbtCtrl, nSize, pSendData, nPort);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - nSize
     - int
     - -
     - Size of the transmission buffer (RX data size).
   * - pSendData
     - char*
     - -
     - Pointer to the data buffer to be sent.  
       Maximum supported size: **256 bytes**.
   * - nPort
     - int
     - 1
     - Port number for flange serial interface. |br|
       1: X1 |br|
       2: X2 (supported only on M/H models)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to transmit data.
   * - 1
     - Success — data successfully transmitted.

**Example**

.. code-block:: cpp

    Drfl.flange_serial_open(115200);
    Drfl.flange_serial_write(8, "test123");

    LPFLANGE_SER_RXD_INFO temp = Drfl.flange_serial_read(4, 5);
    cout << "Serial read : " << temp->_pRxd << endl;
    cout << "Serial cnt  : " << (int)temp->_iSize << endl;

    Drfl.flange_serial_close(0);

This example opens the flange serial port, sends an 8-byte test message,  
reads back received data using `flange_serial_read()`, and finally closes the port.  
It demonstrates basic **send/receive flow** for flange serial communication.
