.. _del_modbus_signal:

del_modbus_signal
------------------------------------------
This is a function for deleting information on the Modbus I/O signal  
registered in the robot controller in advance.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 869)

.. code-block:: cpp

    bool del_modbus_signal(string strSymbol)
    {
        return _del_modbus_signal(_rbtCtrl, strSymbol.c_str());
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
     - Name of the registered Modbus signal to delete

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to delete Modbus registration.
   * - 1
     - Success — Modbus signal successfully removed.

**Example**

.. code-block:: cpp

    /*
     * If the Modbus I/O signal is registered as “di1” and “do1,”
     * and you want to delete this signal registration.
     */

    drfl.del_modbus_signal("di1");    // Deletes “di1” contact point registration
    drfl.del_modbus_signal("do1");    // Deletes “do1” contact point registration

This example demonstrates removing previously registered Modbus I/O points.  
After calling this function, the corresponding signal names are no longer available  
for read/write operations in the controller memory.
