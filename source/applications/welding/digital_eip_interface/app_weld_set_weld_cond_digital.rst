.. _app_weld_set_weld_cond_digital:

app_weld_set_weld_cond_digital
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1039)

.. code-block:: cpp

    bool app_weld_set_weld_cond_digital(CONFIG_DIGITAL_WELDING_CONDITION pConfigdigitalweldingcondition)
    {
        return _app_weld_set_weld_cond_digital(_rbtCtrl, pConfigdigitalweldingcondition);
    };

**Features**

This function sets the **digital welding conditions** for communication-based welders.  
These conditions are only valid within the section defined from **activation**  
(:ref:`app_weld_enable_digital <app_weld_enable_digital>`)  
to **deactivation** (:ref:`app_weld_disable_digital <app_weld_disable_digital>`).  
Executing this function outside of the welding activation state will cause an error.

The items that can be set as welding conditions are limited to those for which communication interface settings with the welder have been completed using the following commands:
- :ref:`app_weld_set_interface_eip_r2m_mode <app_weld_set_interface_eip_r2m_mode>`
- :ref:`app_weld_set_interface_eip_r2m_condition <app_weld_set_interface_eip_r2m_condition>`
- :ref:`app_weld_set_interface_eip_r2m_option <app_weld_set_interface_eip_r2m_option>`

Only one welding condition is allowed within a single welding section. During welding, you can adjust these conditions using the
:ref:`app_weld_adj_welding_cond_digital <app_weld_adj_welding_cond_digital>`  
command, or adjust the voltage correction/dynamic factor adjustment/feeding speed/speed (and weave offset) from the welding condition adjustment popup on the teaching pendant. However, adjusting welding conditions from the teaching pendant is only possible when the welding condition adjustment state is RESET.

**Note**

- **Voltage correction**: Adjusts the arc length.  
- **Dynamic factor adjustment**: Adjusts the arc characteristics.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldingcondition
     - :ref:`CONFIG_DIGITAL_WELDING_CONDITION <struct_CONFIG_DIGITAL_WELDING_CONDITION>`
     - -
     - Digital welding condition settings structure.

**Return**

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

    // Define and set digital welding condition parameters
    CONFIG_DIGITAL_WELDING_CONDITION weldCond;

    weldCond._fTargetVel  = 110.0;  // Target feed speed
    weldCond._fOffsetY    = 10.0;   // Weave offset Y (mm)
    weldCond._fOffsetZ    = 6.0;    // Weave offset Z (mm)
    weldCond._fWidthRate  = 1.2;    // Weaving width ratio
    weldCond._fDynamicCor = 0.8;    // Dynamic factor (arc characteristic)
    weldCond._fVoltageCor = 2.0;    // Voltage correction (arc length)
    weldCond._nJobNumber  = 1;      // Job number
    weldCond._nSynergicID = 1;      // Synergic welding ID

    bool result = Drfl.app_weld_set_weld_cond_digital(weldCond);

    if(result)
        printf("Digital welding condition successfully applied.\n");
    else
        printf("Failed to set digital welding condition.\n");

This example sets the EtherNet/IP-based **digital welding condition parameters**,  
which determine how the robot communicates target feed rate, arc dynamics,  
and voltage correction factors to the external welder.
