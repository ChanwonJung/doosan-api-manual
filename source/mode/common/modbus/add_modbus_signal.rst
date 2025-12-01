.. _add_modbus_signal:

add_modbus_signal
------------------------------------------
This is a function for using the Modbus I/O signal by registering it in advance.  
The modbus I/O signal registered using this function should be reset after rebooting,  
as it is stored in the memory. However, if it is registered in the T/P application,  
it can be reused, as it is added in the initialization process.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 867)

.. code-block:: cpp

    bool add_modbus_signal(string strSymbol,
                           string strIpAddress,
                           unsigned short nPort,
                           MODBUS_REGISTER_TYPE eRegType,
                           unsigned short iRegIndex,
                           unsigned short nRegValue = 0,
                           unsigned char nSlaiveId = 255)
    {
        return _add_modbus_signal(_rbtCtrl,
                                  strSymbol.c_str(),
                                  strIpAddress.c_str(),
                                  nPort,
                                  eRegType,
                                  iRegIndex,
                                  nRegValue,
                                  nSlaiveId);
    };

**Parameter**

.. list-table::
   :widths: 18 20 15 47
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strSymbol
     - string
     - -
     - Modbus signal name
   * - strIpAddress
     - string
     - -
     - Modbus module IP address
   * - nPort
     - unsigned short
     - -
     - Modbus module port number
   * - eRegType
     - :ref:`MODBUS_REGISTER_TYPE <enum_modbus_register_type>`
     - -
     - Modbus register type definitions
   * - iRegIndex
     - unsigned short
     - -
     - Index of the Modbus register to access
   * - nRegValue
     - unsigned short
     - 0
     - Output value when the type is ``MODBUS_REGISTER_TYPE_COILS`` or ``MODBUS_REGISTER_TYPE_HOLDING_REGISTER``  
       (ignored for other types)
   * - nSlaiveId
     - unsigned char
     - 255
     - Slave ID of the target Modbus device (default: broadcast)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to register Modbus signal
   * - 1
     - Success — Modbus signal successfully added

**Example**

.. code-block:: cpp

    // Example of connecting Modbus I/O and allocating context point
    // Modbus IP: 192.168.127.254
    // Add 2 points: "di1", "di2"

    drfl.add_modbus_signal("di1", "192.168.127.254", 502,
                           MODBUS_REGISTER_TYPE_DISCRETE_INPUTS, 0, 0);
    drfl.add_modbus_signal("di2", "192.168.127.254", 502,
                           MODBUS_REGISTER_TYPE_DISCRETE_INPUTS, 0, 0);

This example registers two Modbus digital input points named **di1** and **di2**  
on the external Modbus module connected via TCP at IP **192.168.127.254**, port **502**.  
Once registered, the signals can be monitored or controlled in subsequent API calls.
