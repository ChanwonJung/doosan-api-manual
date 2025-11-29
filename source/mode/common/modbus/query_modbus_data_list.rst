.. _query_modbus_data_list:

query_modbus_data_list
------------------------------------------
This function queries all currently registered Modbus data (TCP / RTU) information  
stored in the controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 871)

.. code-block:: cpp

    LPMODBUS_DATA_LIST query_modbus_data_list()
    {
        return _query_modbus_data_list(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`MODBUS_DATA_LIST <struct_MODBUS_DATA_LIST>`
     - Refer to the Definition of Structure

**Example**

.. code-block:: cpp

    LPMODBUS_DATA_LIST pParam = Drfl.query_modbus_data_list();

    for (int i = 0; i < pParam->_nCount; i++) {
        if (pParam->_tRegister[i]._iType == 0) {     // TCP : 0
            cout << pParam->_tRegister[i]._tData._tcp._iRegValue << endl;
        }
        else {                                       // RTU : 1
            cout << pParam->_tRegister[i]._tData._rtu._iRegValue << endl;
        }
    }

This example retrieves all Modbus register information currently registered in the controller,  
distinguishing between **TCP (type = 0)** and **RTU (type = 1)** connections.  
Each Modbus register’s data value can be accessed from the structure fields  
depending on the communication type.
