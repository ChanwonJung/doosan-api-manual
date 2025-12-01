.. _struct_INVERSE_KINEMATIC_RESPONSE:

INVERSE_KINEMATIC_RESPONSE
==========================
This structure provides the **calculation result of inverse kinematics**,  
returning both the computed joint angles and the validity status of the solution.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Information on six current joint angles
   * - 32
     - ``_iStatus``
     - ``int``
     - 0~2
     - **Availability status** |br|
       0: Normal return |br|
       1: Out of operation area |br|  
       2: Wrist axis singularity

Total size: 28 bytes        

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _INVERSE_KINEMATIC_RESPONSE
   {
       /* target pose */
       float _fTargetPos[NUMBER_OF_JOINT];
       /* status */
       int   _iStatus;
   } INVERSE_KINEMATIC_RESPONSE, *LPINVERSE_KINEMATIC_RESPONSE;

.. note::
   - ``_fTargetPos`` contains the **joint-space solution** obtained from  
     the inverse kinematics calculation.
   - ``_iStatus`` indicates the **validity of the IK solution**: |br|
     - ``0``: Normal solution found |br|
     - ``1``: Out of operation area |br|
     - ``2``: Wrist singularity detected |br|