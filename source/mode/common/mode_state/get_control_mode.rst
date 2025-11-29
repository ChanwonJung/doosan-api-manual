.. _get_control_mode:

get_control_mode
------------------------------------------
This is a function for checking the current control space.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 699)

.. code-block:: cpp

    CONTROL_MODE get_control_mode() { return _get_control_mode(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`CONTROL_MODE <enum_control_mode>`
     - Refer to the Definition of Enumeration Type

**Example**

.. code-block:: cpp

   CONTROL_MODE mode = drfl.get_control_mode();
   cout << mode << endl;


This example obtains the robot’s **current control mode**  
and prints whether it is operating in joint or task space to the console.