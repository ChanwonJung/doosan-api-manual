.. _app_weld_adj_welding_cond_digital:

app_weld_adj_welding_cond_digital
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1041)

.. code-block:: cpp

    bool app_weld_adj_welding_cond_digital(CONFIG_DIGITAL_WELDING_ADJUST pConfigdigitalweldingadjust)
    {
        return _app_weld_adj_welding_cond_digital(_rbtCtrl, pConfigdigitalweldingadjust);
    };

**Features**

This function adjusts **digital welding and weaving conditions** during a welding process  
with a communication-based welder. It is typically used immediately before executing motion commands  
such as ``movej()``, ``movel()``, ``movec()``, ``movesx()`` to update welding parameters for each section  
in a continuous path.

When adjustment parameters are sent with this command, the corresponding welding and weaving conditions  
are updated in real time. However, note that **welding/weaving parameters cannot be modified from the TP (Teaching Pendant)**  
while this command is active.

To revert to the original welding/weaving settings defined by  
:ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>` or  
:ref:`app_weld_weave_cond_trapezoidal <app_weld_weave_cond_trapezoidal>`,  
execute the command with ``flag_reset = 1``.  
When the reset flag is active, the system restores the final TP-adjusted condition (such as ``ww_width_ratio``).  
Once reset, real-time parameter adjustment from the TP becomes available again.

**Arguments**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigdigitalweldingadjust
     - :ref:`CONFIG_DIGITAL_WELDING_ADJUST <struct_CONFIG_DIGITAL_WELDING_ADJUST>`
     - -
     - Digital welding condition adjustment settings structure.

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

    // Define and adjust digital welding parameters in real-time
    CONFIG_DIGITAL_WELDING_ADJUST adjustData;

    adjustData._bRealTime   = 1;     // 1: Real-time adjustment
    adjustData._bResetFlag  = 0;     // 0: Maintain current settings
    adjustData._fTargetVel  = 110.0; // Target speed (mm/s)
    adjustData._fOffsetY    = 12.0;  // Weave offset Y (mm)
    adjustData._fOffsetZ    = 6.0;   // Weave offset Z (mm)
    adjustData._fWidthRate  = 1.2;   // Weaving width ratio (0–2)
    adjustData._fDynamicCor = 0.8;   // Arc dynamic correction factor
    adjustData._fVoltageCor = 2.0;   // Voltage correction factor
    adjustData._nJobNumber  = 1;     // Job number
    adjustData._nSynergicID = 1;     // Synergic setting ID

    bool result = Drfl.app_weld_adj_welding_cond_digital(adjustData);

    if(result)
        printf("Digital welding condition adjusted successfully.\n");
    else
        printf("Failed to adjust welding condition.\n");

This example shows how to modify **digital welding parameters** such as feed speed,  
arc correction, and weaving offset during active EtherNet/IP-based welding operation.  
Real-time control allows adaptive correction of arc performance and welding path consistency.
