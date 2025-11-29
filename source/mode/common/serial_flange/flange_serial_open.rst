.. _flange_serial_open:

flange_serial_open
------------------------------------------
This is a function for opening the **flange serial transfer port** in the robot controller. |br|
This command is **not available in the new flange version (v2).**

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 876)

.. code-block:: cpp

    bool flange_serial_open(
        int nPort,
        int baudrate = 115200,
        BYTE_SIZE eByteSize = BYTE_SIZE_EIGHTBITS,
        PARITY_CHECK eParity = PARITY_CHECK_NONE,
        STOP_BITS eStopBits = STOPBITS_ONE)
    {
        return _flange_serial_open(_rbtCtrl, nPort, baudrate, eByteSize, eParity, eStopBits);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - baudrate
     - int
     - 115200
     - Baudrate setting for serial communication. |br|
       Supported values: 2400, 4800, 9600, 19200, 38400, 57600, 115200, etc.
   * - nPort
     - int
     - -
     - Serial port index:  
       - `0` : x1  
       - `1` : x2
   * - eByteSize
     - :ref:`BYTE_SIZE <enum_byte_size>`
     - BYTE_SIZE_EIGHTBITS
     - Data bit length
   * - eParity
     - :ref:`PARITY_CHECK <enum_parity_check>`
     - PARITY_CHECK_NONE
     - Parity configuration
   * - eStopBits
     - :ref:`STOP_BITS <enum_stop_bits>`
     - STOPBITS_ONE
     - Stop bit configuration

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to open serial port.
   * - 1
     - Success — serial port successfully opened.

**Example**

.. code-block:: cpp

    Drfl.flange_serial_open(115200, 0);

    Drfl.flange_serial_write(0, "test123");

    LPFLANGE_SER_BD_PARAM temp = Drfl.flange_serial_read(4, 5);
    cout << "Serial read S = " << temp->_pSnd << endl;
    cout << "Serial read R = " << (int)temp->_iSize << endl;

    Drfl.flange_serial_close(0);

This example opens the flange serial port (channel 0) at **115200 baud**,  
sends a test string, reads back a response buffer, and closes the serial connection.
