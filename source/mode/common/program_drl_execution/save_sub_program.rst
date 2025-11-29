.. _save_sub_program:

save_sub_program
------------------------------------------
This function saves a **DRL sub-program** into the controller with the specified file name  
and DRL script content. Sub-programs can be invoked from a main DRL program or managed  
independently for modular and reusable task configuration.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 984)

.. code-block:: cpp

    bool save_sub_program(int iTargetType, string strFileName, string strDrlProgram) {
        return _save_sub_program(_rbtCtrl, iTargetType, strFileName.c_str(), strDrlProgram.c_str());
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iTargetType
     - int
     - -
     - Specifies the target type for saving the sub-program.
   * - strFileName
     - string
     - -
     - 256-byte file name of the DRL sub-program file to be saved.  
   * - strDrlProgram
     - string
     - -
     - The DRL script content to be saved as a sub-program.

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Failed — failed to save the sub-program to the controller.
   * - 1
     - int
     - Success — the sub-program was successfully saved.

**Example**

.. code-block:: cpp

   // Define DRL script to save as a sub-program
   string strSubDrl =
       "def sub_task():\n"
       "    movej([0, 0, 0, 0, 0, 0])\n"
       "end\n";

   // Save the DRL sub-program into the controller
   bool bSaved = drfl.save_sub_program(0, "sub_task.drl", strSubDrl);

   if (bSaved) {
       // Successfully saved
       // The sub-program can now be called from a main DRL program
   } else {
       // Handle failure
   }

This example stores a reusable DRL sub-program on the controller,  
allowing modular composition of DRL task sequences.
