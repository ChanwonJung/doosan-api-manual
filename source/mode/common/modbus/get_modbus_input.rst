.. _get_modbus_input:

get_modbus_input
------------------------------------------
This function reads the value of a Modbus I/O register  
previously configured and registered in the robot controller.  
It is primarily used to retrieve Modbus digital or analog input data in **Manual Mode** or during I/O feedback monitoring.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 865)

.. code-block:: cpp

    // get modbus register
    unsigned short get_modbus_input(string strSymbol)
    {
        return _get_modbus_input(_rbtCtrl, strSymbol.c_str());
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strSymbol
     - string
     - -
     - The name of the Modbus signal registered in the controller. |br| 
       This name must match one defined via :ref:`add_modbus_signal <add_modbus_signal>`.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - unsigned short
     - The current value of the Modbus input register. |br|
       - For **digital inputs**: `0` (OFF) or `1` (ON) |br|
       - For **analog inputs**: The actual register value read from the Modbus device.

**Example**

.. code-block:: cpp

    // When the Modbus digital inputs are connected and registered as “di1” and “di2”
    unsigned short input1 = drfl.get_modbus_input("di1");
    unsigned short input2 = drfl.get_modbus_input("di2");

    cout << "DI1 state: " << input1 << endl;
    cout << "DI2 state: " << input2 << endl;

This example reads the current states of two Modbus input points, **di1** and **di2**,  
and prints their ON/OFF status to the console.  
The signals must be registered beforehand using :ref:`add_modbus_signal <add_modbus_signal>`.
