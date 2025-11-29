.. _set_on_mastering_need:

set_on_mastering_need
------------------------------------------
This is a function for registering the callback function that automatically checks  
if the robot’s axes have been twisted due to external force in the robot controller.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 651)

.. code-block:: cpp

    void set_on_mastering_need(TOnMasteringNeedCB pCallbackFunc) { 
        _set_on_mastering_need(_rbtCtrl, pCallbackFunc); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnMasteringNeedCB <cb_tonmasteringneedcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnMasteringNeedCB()
   {
       // Starts the homing mode for the alignment of the robot’s axes
       drfl.Homming(true);
   }

   int main()
   {
       drfl.set_on_mastering_need(OnMasteringNeedCB);
   }

When registered, this callback is executed automatically  
if the controller detects **axis misalignment caused by external force**.  
It triggers the **homing procedure** to realign all robot joints,  
ensuring proper position calibration before resuming normal operation.
