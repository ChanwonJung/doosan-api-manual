.. _flange_serial_close:

flange_serial_close
------------------------------------------
This is a function for closing the **flange serial transfer port** in the robot controller.
This command is **not available in the new flange version (v2).**

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 877)

.. code-block:: cpp

    bool flange_serial_close(int nPort)
    {
        return _flange_serial_close(_rbtCtrl, nPort);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - nPort
     - int
     - -
     - Serial port index: |br|
       0: x1 |br|
       1: x2

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to close serial port.
   * - 1
     - Success — serial port successfully closed.

**Example**

.. code-block:: cpp

    Drfl.flange_serial_open(115200, 0);
    Drfl.flange_serial_write(0, "test123");

    LPFLANGE_SER_RXD_INFO temp = Drfl.flange_serial_read(4, 5);
    cout << "Serial read : " << temp->_pRxd << endl;
    cout << "Serial cnt  : " << (int)temp->_iSize << endl;

    Drfl.flange_serial_close(0);

This example first opens the flange serial port, sends test data,  
reads incoming data using `flange_serial_read()`, and finally closes the connection  
using `flange_serial_close()` to safely release the port resource.
