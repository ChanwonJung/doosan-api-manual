.. _set_modbus_output:

set_modbus_output
------------------------------------------
This is a function for outputting a signal at the Modbus I/O contact point  
in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 863)

.. code-block:: cpp

    bool set_modbus_output(string strSymbol, unsigned short nValue)
    {
        return _set_modbus_output(_rbtCtrl, strSymbol.c_str(), nValue);
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
     - Modbus signal name registered in the controller.
   * - nValue
     - unsigned short
     - -
     - Output value for the Modbus signal:  |br|
       - For **Modbus Digital I/O**: `0` (OFF) or `1` (ON) |br|  
       - For **Modbus Analog I/O**: Data value to be transmitted.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to output Modbus signal.
   * - 1
     - Success — Modbus signal successfully output.

**Example**

.. code-block:: cpp

    // When the Modbus digital I/O is connected and registered as “do1” and “do2”
    drfl.set_modbus_output("do1", 1);    // Turn ON output “do1”
    drfl.set_modbus_output("do2", 0);    // Turn OFF output “do2”

This example controls two Modbus output points, **do1** and **do2**,  
by sending ON/OFF digital signals through the Modbus interface  
previously registered using :ref:`add_modbus_signal <add_modbus_signal>`.
